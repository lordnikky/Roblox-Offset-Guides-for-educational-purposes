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
