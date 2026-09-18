# luaF_FreeProto

search string "LuauSplitTableLookups":

```asm
.data:0000000007CC9F68                 dq offset aLuausplittable ; "LuauSplitTableLookups"
.data:0000000007CC9F70 qword_7CC9F70   dq 0                    ; DATA XREF: sub_600140+7↑w
.data:0000000007CC9F78                 align 20h
.data:0000000007CC9F80 dword_7CC9F80   dd 20h                  ; DATA XREF: sub_6001A0+E↑o
.data:0000000007CC9F80                                         ; sub_2774B10+53↑r
```
well, 3rd xref, the sub_2774B10, do NOT decompile it, from where you are scroll up until you see second SUBROUTINE section:

this will be the first (function that u got sent to)

```asm
text:0000000002774B10 ; =============== S U B R O U T I N E =======================================
.text:0000000002774B10
.text:0000000002774B10
.text:0000000002774B10 ; char __fastcall sub_2774B10(__int64, __int64, __int64, unsigned int)
.text:0000000002774B10 sub_2774B10     proc near               ; CODE XREF: sub_2788580+32EB↓p
.text:0000000002774B10                 sub     rsp, 38h
.text:0000000002774B14                 mov     rax, [rcx+48h]
.text:0000000002774B18                 cmp     qword ptr [rax+710h], 0
```

and you scroll up until you see next one

```asm
.text:00000000027748F0
.text:00000000027748F0 ; =============== S U B R O U T I N E =======================================
.text:00000000027748F0
.text:00000000027748F0
.text:00000000027748F0 ; __int64 __fastcall sub_27748F0(__int64, __int64, __int64)
.text:00000000027748F0 sub_27748F0     proc near               ; CODE XREF: sub_2762DA0+51↑j
.text:00000000027748F0
.text:00000000027748F0 var_18          = qword ptr -18h
.text:00000000027748F0 arg_0           = qword ptr  8
.text:00000000027748F0 arg_8           = qword ptr  10h
.text:00000000027748F0
.text:00000000027748F0                 mov     [rsp+arg_0], rbx

```

so that subroutine should be the luaF_FreeProto, and the offset is 0x27748F0, ik its ass i didnt find any good anchors 
