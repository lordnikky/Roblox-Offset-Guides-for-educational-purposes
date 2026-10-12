# lua_newstate

search string "Failed to create Lua state", first xref, decompile:

```c
  v10 = sub_258EFB0(a1: (__int64 (__fastcall *)(__int64, _QWORD, _QWORD, __int64))sub_420F830, a2); // lua_newstate
  v974 = v10;
  if ( v10 == nullptr )
    sub_4976D00(a1: "Failed to create Lua state"); // you're here
```

so the offset is 0x258EFB0

sig: 48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC 50 02 00 00 4C 8B F2

<details>

<summary><b>verify</b></summary>

2 args

```c
  v10 = sub_258EFB0(a1: sub_420F830);
  v984 = v10;
  if ( v10 == 0 )
    sub_4976D00(a1: "Failed to create Lua state");
  if ( byte_7DEB720 == 0 )
    goto LABEL_23;
```

if failed well throws failed to create luastate

allocates 19808 bytes and zeroes em out

```c

  if ( byte_7DEB700 != 0 )
  {
    v4 = (char *)a1(a1: a2, a2: 0, a3: 0, a4: 19808);
    v5 = v4;
    if ( v4 != nullptr )
    {
      memset(a1: v4, Val: 0, Size: 0x4D60u);
      *(_WORD *)v5 = 2314;
      *((_QWORD *)v5 + 3) = v5 + 144;
      *((_QWORD *)v5 + 233) = 1;
      *((_QWORD *)v5 + 1480) = 19808;
      *(_OWORD *)(v5 + 1736) = 0;
      *((_QWORD *)v5 + 114) = v5 + 896;
      *(_OWORD *)(v5 + 1752) = 0;
      *((_QWORD *)v5 + 115) = v5 + 896;
      v6 = *((_DWORD *)v5 + 432);
      *(_OWORD *)(v5 + 1768) = 0;
      *((_WORD *)v5 + 72) = 9;
      *(_OWORD *)(v5 + 1896) = 0;
      *((_QWORD *)v5 + 111) = v5;
      *(_OWORD *)(v5 + 1784) = 0;
      *((_DWORD *)v5 + 432) = v6 & 0xFFFFFFF | 0x70000000;
      *(_OWORD *)(v5 + 1912) = 0;
      v66 = 0;
      memset(&v65[14], 0, 32);
      v64 = 0;
      memset(v65, 0, 48);
      *((_QWORD *)v5 + 23) = a1;
      *(_OWORD *)&v65[6] = 0;
      *((_QWORD *)v5 + 24) = a2;
```

</details>
