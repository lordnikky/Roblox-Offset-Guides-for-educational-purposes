# luaG_runerror

search for string "table overflow", any xref works, decompile first for example

```c
        sub_2723350(a1, a2: (__int64)"table overflow", v22);
```

sub_2723350 is the luaG_runerror

```c
void __noreturn sub_2723350(__int64 a1, __int64 a2, ...)
{
  _BYTE v3[520]; // [rsp+20h] [rbp-208h] BYREF
  va_list va; // [rsp+240h] [rbp+18h] BYREF
  va_start(va, a2);
  sub_B9A7D0(a1: v3, a2: 512, a3: a2, a4: (__int64 *)va);
  sub_26F7F50(a1, a2: 1);
  sub_2722D60(a1, a2: v3);
  sub_2709720(a1, a2: 2u);
}
```
