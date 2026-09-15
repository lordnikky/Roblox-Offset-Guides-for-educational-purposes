# lua_newstate

search string "Failed to create Lua state", first xref, decompile:

```c
v11 = sub_26FDC10(a1: sub_4247E10); // <-- lua_newstate
v12 = v11;
v734 = v11;
if ( v11 == 0 )
sub_4924110(a1: "Failed to create Lua state"); // <-- you're here
```

so the offset is 0x26FDC10

