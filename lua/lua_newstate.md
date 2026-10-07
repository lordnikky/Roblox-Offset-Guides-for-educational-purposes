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
