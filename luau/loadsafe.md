# loadsafe

search for string "%s: bytecode corrupted"
```asm
.rdata:0000000006E27B58 aSBytecodeCorru db '%s: bytecode corrupted',0
.rdata:0000000006E27B58                                         ; DATA XREF: sub_27582C0+232↑o
```

sub_27582C0 is the loadsafe

sig: 48 89 54 24 ? 48 89 4C 24 ? 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC 58 0B 00 00
