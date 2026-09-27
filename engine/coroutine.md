So basically this wont be specific cuz they're all found with one string, search for string "isyieldable", rdata xref

```asm
.rdata:0000000007178EBA                 align 20h
.rdata:0000000007178EC0 aIsyieldable    db 'isyieldable',0      ; DATA XREF: .rdata:00000000066F3CC0↑o
.rdata:0000000007178EC0                                         ; .rdata:00000000066F3D40↑o
```

will put you here:

```asm
.rdata:00000000066F3CF0                                         ; "create"
.rdata:00000000066F3CF8                 dq offset sub_575BAD0
.rdata:00000000066F3D00                 dq offset aRunning_1    ; "running"
.rdata:00000000066F3D08                 dq offset sub_575C350
.rdata:00000000066F3D10                 dq offset aStatus_0     ; "status"
.rdata:00000000066F3D18                 dq offset sub_575A060
.rdata:00000000066F3D20                 dq offset aWrap_0       ; "wrap"
.rdata:00000000066F3D28                 dq offset sub_575C080
.rdata:00000000066F3D30                 dq offset aYield        ; "yield"
.rdata:00000000066F3D38                 dq offset sub_575C2F0
.rdata:00000000066F3D40                 dq offset aIsyieldable  ; "isyieldable"
.rdata:00000000066F3D48                 dq offset sub_575C3C0
.rdata:00000000066F3D50                 dq offset aClose_0      ; "close"
.rdata:00000000066F3D58                 dq offset sub_575C450
```

and as you guessed thats coroutine!!!!

CoroutineCreate: 0x575BAD0

CoroutineRunning: 0x575C350

CoroutineStatus: 0x575A060

CoroutineWrap: 0x575C080

CorotuineYield: 0x575C2F0

CoroutineIsYieldable: 0x575C3C0

CoroutineClose: 0x575C450
