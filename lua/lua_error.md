# lua_error

search for string "stack overflow", firxt xref and decompile:

```c
  sub_2722360(a1, a2: "stack overflow");
  sub_26FA450(a1);
```

second rva is the lua_error, so the offset is 0x26FA450

sig: 48 83 EC 28 BA 02 00 00 00 E8

<details>
  
<summary><b>verity</b></summary>

takes 1 arg, which is luastate, calls luaD_throw:

```asm
void __fastcall __noreturn sub_258B520(__int64 a1)
{
  sub_259B470(a1, a2: 2);
}
```

</details>
