# BytecodeVerificationTableA

search string "GuidRegistryMemScopeEnabled", first xref, do NOT decompile, in binary scroll up until you see next subroutine

```asm
.text:00000000005E1B80 ; =============== S U B R O U T I N E =======================================
.text:00000000005E1B80
.text:00000000005E1B80
.text:00000000005E1B80 ; __int64 sub_5E1B80()
.text:00000000005E1B80 sub_5E1B80      proc near               ; DATA XREF: .rdata:0000000006073030↓o
.text:00000000005E1B80                                         ; .rdata:00000000060BB80C↓o
.text:00000000005E1B80                 sub     rsp, 28h
.text:00000000005E1B84                 lea     rcx, unk_844ED90  	; <-- this unk is the bytecodevertable
.text:00000000005E1B8B                 call    sub_1CCA3E0
.text:00000000005E1B90                 lea     rcx, sub_6004F80
.text:00000000005E1B97                 add     rsp, 28h
.text:00000000005E1B9B                 jmp     sub_5A29610
.text:00000000005E1B9B sub_5E1B80      endp
.text:00000000005E1B9B
.text:00000000005E1BA0
.text:00000000005E1BA0 ; =============== S U B R O U T I N E =======================================
.text:00000000005E1BA0
.text:00000000005E1BA0
.text:00000000005E1BA0 sub_5E1BA0      proc near               ; DATA XREF: .rdata:0000000006073038↓o
.text:00000000005E1BA0                                         ; .rdata:00000000060BB811↓o
.text:00000000005E1BA0
.text:00000000005E1BA0 var_18          = xmmword ptr -18h
.text:00000000005E1BA0
.text:00000000005E1BA0                 sub     rsp, 18h
.text:00000000005E1BA4                 lea     rax, aGuidregistryme ; "GuidRegistryMemScopeEnabled"     <-- you're here
.text:00000000005E1BAB                 mov     qword ptr [rsp+18h+var_18+8], 1Bh
.text:00000000005E1BB4                 mov     qword ptr [rsp+18h+var_18], rax
.text:00000000005E1BB8                 movups  xmm0, [rsp+18h+var_18]
.text:00000000005E1BBC                 movups  cs:xmmword_8158260, xmm0
.text:00000000005E1BC3                 add     rsp, 18h
.text:00000000005E1BC7                 retn
.text:00000000005E1BC7 sub_5E1BA0      endp
```

so the offset is 0x844ED90