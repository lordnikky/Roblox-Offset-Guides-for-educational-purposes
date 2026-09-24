# luaL_getmetafield

search for string "invalid argument #%d to '%s' (%s)" first xref is the luaL_getmetafield:

```asm
.rdata:0000000006F1B7D8                 db 'invalid argument #%d to ',27h,'%s',27h,' (%s)',0
.rdata:0000000006F1B7D8                                         ; DATA XREF: sub_2663C40+40↑o
.rdata:0000000006F1B7D8                                         ; sub_390F5B0+291↑o
```

```c
void __fastcall __noreturn sub_2663C40(__int64 a1, int a2, const char *a3)
{
  const char *v6; // rax

  v6 = (const char *)sub_2663BC0();
  if ( v6 != nullptr )
    sub_26648D0(a1, a2: "invalid argument #%d to '%s' (%s)", a2, v6, a3);
  sub_26648D0(a1, a2: "invalid argument #%d (%s)", a2, a3);
}
```

so the offset is 0x2663C40
