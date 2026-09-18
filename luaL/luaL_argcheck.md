# luaL_argcheck

search for string "cannot change a protected metatable", first xref decompile:

```c
  if ( (unsigned int)sub_2701A50((__int64)a1, a2: 1, a3: (__int64)&qword_6E26E40, a4) != 0 ) // <-- sub_2701A50 is the offset
    sub_26FFE40(a1, a2: "cannot change a protected metatable"); // <-- you're here
```

so the offset is sub_2701A50
