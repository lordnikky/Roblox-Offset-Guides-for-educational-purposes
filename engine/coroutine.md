So basically this wont be specific cuz they're all found with one string, search for string "cannot close %s coroutine", first xref, decompile and scroll very up, press x on that rva

```c
__int64 __fastcall sub_5694590(__int64 a1)
```

second xref
```asm
Down	o	.rdata:000000000666E4D8	dq offset sub_5694590
```

will put you here:

```asm
.rdata:000000000666E470                                         ; "create"
.rdata:000000000666E478                 dq offset sub_5693C10
.rdata:000000000666E480                 dq offset aRunning_0    ; "running"
.rdata:000000000666E488                 dq offset sub_56944A0
.rdata:000000000666E490                 dq offset aStatus_0     ; "status"
.rdata:000000000666E498                 dq offset sub_56921A0
.rdata:000000000666E4A0                 dq offset aWrap_0       ; "wrap"
.rdata:000000000666E4A8                 dq offset sub_56941D0
.rdata:000000000666E4B0                 dq offset aYield        ; "yield"
.rdata:000000000666E4B8                 dq offset sub_5694440
.rdata:000000000666E4C0                 dq offset aIsyieldable  ; "isyieldable"
.rdata:000000000666E4C8                 dq offset sub_5694510
.rdata:000000000666E4D0                 dq offset aClose_0      ; "close"
.rdata:000000000666E4D8                 dq offset sub_5694590
```

and as you guessed thats coroutine!!!!

CoroutineCreate: 0x5693C10
CoroutineRunning: 0x56944A0
CoroutineStatus: 0x56921A0
CoroutineWrap: 0x56941D0
CorotuineYield: 0x5694440
CoroutineIsYieldable: 0x5694510
CoroutineClose: 0x5694590
