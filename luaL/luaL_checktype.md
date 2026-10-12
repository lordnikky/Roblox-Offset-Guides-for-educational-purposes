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

sig: 48 83 EC 28 44 8B CA 4C 8B D1


<details>

<summary><b>verify</b></summary>

takes 3 args calls GetTypeName 

```c
void __fastcall __noreturn sub_2590710(__int64 a1, unsigned int a2, __int64 a3)
{
  const char *v3; // rax
  unsigned int v4; // r9d
  __int64 v5; // r10

  v3 = (const char *)sub_25884C0(a1, a2: (unsigned int)a3, a3, a4: a2);
  sub_2590620(a1: v5, a2: v4, a3: v3);
}
```

  
</details>
