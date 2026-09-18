# lua_pushfstring

search for string "%s%.*s" or "%s: bytecode version mismatch (expected [%d..%d], got %d)" or like any error, best one is "bytecode corrupted"

```asm
.rdata:0000000006E27B58 aSBytecodeCorru db '%s: bytecode corrupted',0
.rdata:0000000006E27B58                                         ; DATA XREF: sub_27582C0+232↑o
```

go to it and decompile:

```c
  result = sub_26F8DE0(a1: v3, a2: "%s: bytecode corrupted", v17);
```

double click sub_26F8DE0 and thats ur lua_pushfstring
