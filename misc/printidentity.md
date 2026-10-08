# PrintIdentity

search string "Current identity is %d", first xref will be it:

```asm

.rdata:0000000006F78F38 aCurrentIdentit db 'Current identity is %d',0
.rdata:0000000006F78F38                                         ; DATA XREF: sub_4267C80+B7↑o

```

so the offset is 0x4267C80

sig: 40 53 48 83 EC 40 48 8B D9 48 8B 0D ? ? ? ? E8 ? ? ? ? 48 8D 0D
