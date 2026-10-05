# luaH_clone

search for string "table has a protected metatable", second xref and decompile:

```c
    sub_26FF1F0(a1, a2: 1, a3: "table has a protected metatable"); // <-- you're here
  *(_QWORD *)&v6 = sub_27215A0(a1, a2: *(_QWORD *)a1[4], a3: v3, a4: v4); // <-- sub_27215A0 is the offset
```

so the offset is 0x27215A0

sig: 48 89 5C 24 ? 48 89 6C 24 ? 56 57 41 55 41 56 41 57 48 83 EC 40 44 0F B6 79
