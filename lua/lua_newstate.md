# lua_newstate

search string "Failed to create Lua state", second xref, decompile:

```c
v11 = sub_26FDC10(a1: sub_4247E10); // <-- lua_newstate
v12 = v11;
v734 = v11;
if ( v11 == 0 )
sub_4924110(a1: "Failed to create Lua state"); // <-- you're here
```

so the offset is 0x26FDC10

48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC 50 02 00 00 4C 8B F2
