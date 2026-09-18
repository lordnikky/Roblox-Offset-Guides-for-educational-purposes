# luaL_checktype

search for string "invalid argument #%d to '%s' (%s expected, got %s)", first xref, decompile:

```c
void __fastcall __noreturn sub_26FF270(__int64 a1, unsigned int a2, const char *a3)
{
  const char *v6; // rdi
  __int64 v7; // rax
  const char *v8; // rax
  v6 = (const char *)sub_26FF170();
  v7 = sub_26F7A20(a1, a2);
  if ( v7 != 0 )
  {
    v8 = (const char *)sub_2725420(a1, a2: v7);
    if ( v6 != nullptr )
      sub_26FFE40(a1, a2: "invalid argument #%d to '%s' (%s expected, got %s)", a2, v6, a3, v8);
    sub_26FFE40(a1, a2: "invalid argument #%d (%s expected, got %s)", a2, a3, v8);
  }
  if ( v6 != nullptr )
    sub_26FFE40(a1, a2: "missing argument #%d to '%s' (%s expected)", a2, v6, a3);
  sub_26FFE40(a1, a2: "missing argument #%d (%s expected)", a2, a3);
}
```

very first line click the rva and press x, first xref will be the luaL_checktype:

```asm
Down	p	sub_26FF360+1B	call    sub_26FF270
```

yaayyyayaya new easy guide for me
