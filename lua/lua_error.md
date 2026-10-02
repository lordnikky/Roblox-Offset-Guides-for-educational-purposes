# lua_error

search for string "stack overflow", firxt xref and decompile:

```c
  sub_2722360(a1, a2: "stack overflow");
  sub_26FA450(a1);
```

second rva is the lua_error, so the offset is 0x26FA450

sig: 48 83 EC 28 BA 02 00 00 00 E8
