# ScriptContextResume

search string "can't resume script in this context", first xref will be it

```asm
.rdata:0000000006F78978 aCanTResumeScri db 'Can',27h,'t resume script in this context',0
.rdata:0000000006F78978                                         ; DATA XREF: sub_4260F50+31E↑o
.rdata:0000000006F7899C                 align 20h
```

48 8D 05 ? ? ? ? 48 89 44 24 ? 48 C7 44 24 ? ? ? ? ? ? ? ? ? 48 85 C0 74 ? 48 8B 48
