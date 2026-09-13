# require bypass

string "Cannot require a non-RobloxScript module from a RobloxScript" or "cannot require a non" if you're lazy, first xref:

```
.rdata:0000000006F79098 aCannotRequireA db 'Cannot require a non-RobloxScript module from a RobloxScript',0
.rdata:0000000006F79098                                         ; DATA XREF: sub_426F150:loc_4270243↑o
.rdata:0000000006F79098                                         ; .rdata:00000000065C99C0↑o
```

sub_426F150 decompile that

```c
  if ( *(_BYTE *)(v25 + 2996) == 0 ) // <-- require bypass
  {
    qmemcpy(v149, (const void *)(*(_QWORD *)(a1 + 96) + 48LL), sizeof(v149));
    if ( (sub_1CE6760(a1: v149) & 8) != 0 )
    {
      if ( (*(_BYTE *)(v122 + 360) & 1) == 0 ) // <-- iscorescript
        sub_4924110(a1: "Cannot require a non-RobloxScript module from a RobloxScript"); // <-- you're here
```

click h on that 2996 for ida to turn it into 0xBB4, and iscorescript into 0x168
