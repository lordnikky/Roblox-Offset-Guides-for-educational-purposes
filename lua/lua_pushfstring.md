# lua_pushfstring

search for string "AuroraStruct<%s>" or these: "cannot resume %s coroutine", "%s: 0x%016llx", "%s:%d:", "bytecode corrupted"

```asm
.rdata:0000000007073B18 aAurorastructS  db 'AuroraStruct<%s>',0 ; DATA XREF: sub_419E1D0+52↑o
```

go to it and decompile:

```c
  sub_265D7D0(a1, a2: "AuroraStruct<%s>", v2);
```

so the offset is 0x265D7D0

sig: 48 89 54 24 ? 4C 89 44 24 ? 4C 89 4C 24 ? 53 48 83 EC 20 48 8B 51


<details>

<summary><b>verify</b></summary>

checks capacity and if full calls rva to allocate, takes 2 xrefs

```c
  if ( *(_QWORD *)(v2 + 16) >= *(_QWORD *)(v2 + 8) )
  {
    LOBYTE(v2) = 1;
    sub_25B0430(a1, a2: v2);
  }
```

full thing is

```c
__int64 sub_2588C50(__int64 a1, const char *a2, ...)
{
  __int64 v2; // rdx
  char v4; // al
  __int64 v5; // rcx
  va_list va; // [rsp+40h] [rbp+18h] BYREF

  va_start(va, a2);
  v2 = *(_QWORD *)(a1 + 24);
  if ( *(_QWORD *)(v2 + 16) >= *(_QWORD *)(v2 + 8) )
  {
    LOBYTE(v2) = 1;
    sub_25B0430(a1, a2: v2);
  }
  v4 = *(_BYTE *)(a1 + 1);
  if ( (v4 & 4) != 0 )
  {
    v5 = *(_QWORD *)(a1 + 24);
    *(_BYTE *)(a1 + 1) = v4 & 0xFB;
    *(_QWORD *)(a1 + 80) = *(_QWORD *)(v5 + 88);
    *(_QWORD *)(v5 + 88) = a1;
  }
  return sub_25C2C00(a1, a2, a3: (__int64 *)va);
}
```

  
</details>
