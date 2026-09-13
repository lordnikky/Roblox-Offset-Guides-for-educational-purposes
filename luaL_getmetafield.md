# luaL_getmetafield

search for string "invalid argument #%d to '%s' (%s)" first xref and decompile:

```c
void __fastcall __noreturn sub_26FF1F0(__int64 a1, int a2, const char *a3)
{
  const char *v6; // rax
  v6 = (const char *)sub_26FF170();
  if ( v6 != nullptr )
    sub_26FFE40(a1, a2: "invalid argument #%d to '%s' (%s)", a2, v6, a3);
  sub_26FFE40(a1, a2: "invalid argument #%d (%s)", a2, a3);
}
```

so the offset is 0x26FF1F0
