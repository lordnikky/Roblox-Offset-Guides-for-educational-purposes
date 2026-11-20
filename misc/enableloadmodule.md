# EnableLoadModule

search for string `EnableLoadModule`, second xref:

```asm
.data:0000000008128E80 byte_8128E80    db 0                    ; DATA XREF: sub_41E1740+26↑r
.data:0000000008128E80                                         ; sub_41FA7D0+6↑r ...
.data:0000000008128E81                 align 8
.data:0000000008128E88                 dq offset aEnableloadmodu ; "EnableLoadModule"
```

that byte_ or whatever it'll be for you is the rva of the fflag, so in this case it is 0x8128E80
