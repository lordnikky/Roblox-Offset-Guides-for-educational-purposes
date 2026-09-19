# ida plugin to search multiple strings instead of one, uhh, thats all, assigned to q by default so if u wanna use it just remove q keybind in ida or just change keybind to whatever you want

import ida_idaapi
import ida_strlist
import idautils
import idc
import ida_kernwin

ACTION_NAME = "custom:multi_search"

def run_search():
    user_input = ida_kernwin.ask_str("", 0, "enter strings, separate thru commas")
    if user_input:
        targets = [t.strip() for t in user_input.split(",") if t.strip()]
        
        if ida_strlist.get_strlist_qty() == 0:
            ida_strlist.build_strlist()
            
        string_hit_sets = [set() for _ in targets]

        for i in range(ida_strlist.get_strlist_qty()):
            si = ida_strlist.string_info_t()
            if not ida_strlist.get_strlist_item(si, i):
                continue
                
            raw_bytes = idc.get_strlit_contents(si.ea, si.length, si.type)
            if not raw_bytes:
                continue
                
            current_str = raw_bytes.decode('utf-8', errors='ignore')
            
            for idx, target in enumerate(targets):
                if target in current_str:
                    for xref in idautils.XrefsTo(si.ea):
                        func_ea = idc.get_func_attr(xref.frm, idc.FUNCATTR_START)
                        if func_ea != idc.BADADDR:
                            string_hit_sets[idx].add(func_ea)

        matches = set.intersection(*string_hit_sets) if string_hit_sets and all(string_hit_sets) else set()
        
        print(f"Results for: {', '.join(targets)}")
        if matches:
            word = "function" if len(matches) == 1 else "functions"
            print(f"found {len(matches)} matching {word}:")
            for func_ea in matches:
                print(f"  {idc.get_func_name(func_ea)} ({hex(func_ea)})")
        else:
            print("no functions with these strings found")

class SearchActionHandler(ida_kernwin.action_handler_t):
    def activate(self, ctx):
        run_search()
        return 1

    def update(self, ctx):
        return ida_kernwin.AST_ENABLE_ALWAYS

class MultiStringSearchPlugin(ida_idaapi.plugin_t):
    flags = ida_idaapi.PLUGIN_HIDE
    comment = "take a wild fucking guess from the name"
    help = ""
    wanted_name = "multiple strings search"
    wanted_hotkey = ""

    def init(self):
        action_desc = ida_kernwin.action_desc_t(
            ACTION_NAME,
            "multi search",
            SearchActionHandler(),
            "Q",
            "find funcs that contain lots of strings"
        )
        
        ida_kernwin.register_action(action_desc)
        
        ida_kernwin.attach_action_to_menu(
            "Search/text...",
            ACTION_NAME,
            ida_kernwin.SETMENU_APP
        )
        return ida_idaapi.PLUGIN_KEEP

    def run(self, arg):
        pass

    def term(self):
        ida_kernwin.unregister_action(ACTION_NAME)

def PLUGIN_ENTRY():
    return MultiStringSearchPlugin()
