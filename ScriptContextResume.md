# ScriptContextResume

search string "[FLog::ScriptContext] Resuming script: %p" or "resumeParallelWaitingScripts"

if first string:

```asm
.rdata:0000000006F789D0 aFlogScriptcont_3 db '[FLog::ScriptContext] Resuming script: %p',0
.rdata:0000000006F789D0                                         ; DATA XREF: sub_4262210+1D4↑o
```

0x4262210 is the scriptcontextresume

if second string:

```asm
.rdata:0000000006F7B828 aResumeparallel db 'resumeParallelWaitingScripts',0
.rdata:0000000006F7B828                                         ; DATA XREF: sub_42CC4B0+9C↑o
```

decompile it and just scroll to the up

```c
__int64 __fastcall sub_42CC4B0(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
```