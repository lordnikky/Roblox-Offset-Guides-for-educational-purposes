# FireServer

string "FireServer can only be called from the client", first xref

```asm
.rdata:0000000007051850 aFireserverCanO db 'FireServer can only be called from the client',0
.rdata:0000000007051850                                         ; DATA XREF: sub_34496E0:loc_344984C↑o
.rdata:0000000007051850                                         ; sub_3449CE0:loc_3449E4C↑o
```

offset is 0x34496E0

# FireClient

string "FireClient can only be called from the server"

```asm
.rdata:00000000070517E8 aFireclientCanO db 'FireClient can only be called from the server',0
.rdata:00000000070517E8                                         ; DATA XREF: sub_3449880:loc_3449A89↑o
.rdata:00000000070517E8                                         ; sub_3449E80:loc_344A089↑o
```

0x3449880

# FireAllClients

string "FireAllClients can only be called from the server" first xref

```asm
.rdata:0000000007051818 aFireallclients_0 db 'FireAllClients can only be called from the server',0
.rdata:0000000007051818                                         ; DATA XREF: sub_3449AD0:loc_3449CBB↑o
.rdata:0000000007051818                                         ; sub_344A0D0:loc_344A2BB↑o
```

0x3449AD0

# InvokeServer

"InvokeServer can only be called from the client"

```asm
.rdata:000000000705D5F0 aInvokeserverCa db 'InvokeServer can only be called from the client',0
.rdata:000000000705D5F0                                         ; DATA XREF: sub_351D380:loc_351D697↑o
```
0x351D380

# InvokeClient

```asm
.rdata:000000000705D5B0 aInvokeclientCa db 'InvokeClient can only be called from the server',0
.rdata:000000000705D5B0                                         ; DATA XREF: sub_351D6D0:loc_351DA67↑o
```

what am i doing with my life
