multiple offsets in 1 guide again, search for string "setmetatable", first rdata xref:

```asm
rdata:00000000064542E0                                         ; "assert"
.rdata:00000000064542E8                 dq offset sub_279BE30
.rdata:00000000064542F0                 dq offset dword_6D63D68
.rdata:00000000064542F8                 dq offset sub_2795C80
.rdata:0000000006454300                 dq offset aGcinfo       ; "gcinfo"
.rdata:0000000006454308                 dq offset sub_279A770
.rdata:0000000006454310                 dq offset aGetfenv      ; "getfenv"
.rdata:0000000006454318                 dq offset sub_2797260
.rdata:0000000006454320                 dq offset aGetmetatable ; "getmetatable"
.rdata:0000000006454328                 dq offset sub_2796690
.rdata:0000000006454330                 dq offset aNext_0       ; "next"
.rdata:0000000006454338                 dq offset sub_279B380
.rdata:0000000006454340                 dq offset aNewproxy     ; "newproxy"
.rdata:0000000006454348                 dq offset sub_279CD30
.rdata:0000000006454350                 dq offset aPrint_1      ; "print"
.rdata:0000000006454358                 dq offset sub_2795830
.rdata:0000000006454360                 dq offset aRawequal     ; "rawequal"
.rdata:0000000006454368                 dq offset sub_2797550
.rdata:0000000006454370                 dq offset aRawget       ; "rawget"
.rdata:0000000006454378                 dq offset loc_2797660
.rdata:0000000006454380                 dq offset aRawset       ; "rawset"
.rdata:0000000006454388                 dq offset loc_2798070
.rdata:0000000006454390                 dq offset aRawlen       ; "rawlen"
.rdata:0000000006454398                 dq offset sub_279A6D0
.rdata:00000000064543A0                 dq offset aSelect_1     ; "select"
.rdata:00000000064543A8                 dq offset sub_279BEE0
.rdata:00000000064543B0                 dq offset aSetfenv      ; "setfenv"
.rdata:00000000064543B8                 dq offset sub_2797320
.rdata:00000000064543C0                 dq offset aSetmetatable ; "setmetatable"
.rdata:00000000064543C8                 dq offset sub_2796810
.rdata:00000000064543D0                 dq offset aTonumber     ; "tonumber"
.rdata:00000000064543D8                 dq offset sub_2795900
.rdata:00000000064543E0                 dq offset qword_6E96FE0
.rdata:00000000064543E8                 dq offset sub_279CCD0
.rdata:00000000064543F0                 dq offset aType_0       ; "type"
.rdata:00000000064543F8                 dq offset sub_279A790
.rdata:0000000006454400                 dq offset aTypeof_0     ; "typeof"
.rdata:0000000006454408                 dq offset sub_279AD90
```

all of these are luaB offsets, enjoy