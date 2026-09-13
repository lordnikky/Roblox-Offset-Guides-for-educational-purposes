# luav gettable

search for string "'__index' chain too long; possible loop", first xref, thats the luav_gettable

```asm
.rdata:0000000006E26848 aIndexChainTooL db 27h,'__index',27h,' chain too long; possible loop',0
.rdata:0000000006E26848                                         ; DATA XREF: sub_27100E0:loc_2710EA2↑o
.rdata:0000000006E26870 aGetLengthOf    db 'get length of',0    ; DATA XREF: sub_27144C0:loc_27146DE↑o
.rdata:0000000006E26870                                         ; .text:0000000002736794↑o ...
```

so the offset is 0x27100E0