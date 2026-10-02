wont only conain taskdefer but will have bit more stuff

# TaskDefer

Search for string "task.defer is not available for AuroraScripts", first xref will be it

```asm

.rdata:0000000006F7DCA0 aTaskDeferIsNot db 'task.defer is not available for AuroraScripts',0

.rdata:0000000006F7DCA0                                         ; DATA XREF: sub_4319B60:loc_4319FC2↑o

```

so the offset is 0x4319B60

sig: 48 89 5C 24 ? 48 89 74 24 ? 48 89 7C 24 ? 55 41 54 41 55 41 56 41 57 48 8D 6C 24 ? 48 81 EC 30 01 00 00 48 8B 05 ? ? ? ? 48 33 C4 48 89 45 ? 48 8B F9 33 DB

# TaskSpawn

string "task.spawn is not available for AuroraScripts", first xref will be it

```asm

.rdata:0000000006F7DD28 aTaskSpawnIsNot db 'task.spawn is not available for AuroraScripts',0

.rdata:0000000006F7DD28                                         ; DATA XREF: sub_431A020:loc_431A1DE↑o

```

so the offset is 0x431A020

sig: 48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC 60 48 8B F1 33 FF 40 38 3D

# TaskDelay

string "task.delay is not available for AuroraScripts" first xref bla bla, didn't you notice the pattern already lol

```asm

.rdata:0000000006F7DFE8 aTaskDelayIsNot db 'task.delay is not available for AuroraScripts',0

.rdata:0000000006F7DFE8                                         ; DATA XREF: sub_431A3B0:loc_431A66A↑o

```
well also can be found via "task.delay(t, f)"

so the offset is 0x431A3B0

sig: 40 55 53 56 57 41 54 41 56 41 57 48 8D 6C 24 ? 48 81 EC 90 00 00 00 48 8B F9

# TaskWait

string "task.wait is not available for AuroraScripts" first xref, done

```asm
.rdata:0000000006F7DFA8 aTaskWaitIsNotA db 'task.wait is not available for AuroraScripts',0
.rdata:0000000006F7DFA8                                         ; DATA XREF: sub_431A6B0:loc_431A874↑o
``` 

also "task.wait(t)"

sig: 40 53 56 57 48 83 EC 60 48 8B D9

# TaskDesynchronize (TaskDesync)

seach string "task.desynchronize() may only be called from a script that is a d", first xref will be it

```asm
.rdata:0000000006F7DBA0 aTaskDesynchron db 'task.desynchronize() may only be called from a script that is a d'
.rdata:0000000006F7DBA0                                         ; DATA XREF: sub_4318F70:loc_431905C↑o
```

so the offset is 0x4318F70

sig: 48 89 5C 24 ? 57 48 83 EC 40 48 8B D9 33 D2 48 85 C9 74 ? 48 8B 41 ? EB ? 48 8B C2 48 8B 40 ? 48 8B 48 ? 38 91 ? ? ? ? 75 ? 48 8D 0D ? ? ? ? E8 ? ? ? ? 84 C0 0F 84 ? ? ? ? BA 20 00 00 00 65 48 8B 04 25 ? ? ? ? ? ? ? ? ? ? 39 05 ? ? ? ? 0F 8E ? ? ? ? E9 ? ? ? ? 48 85 DB 74 ? 48 8B 53 ? 48 8B 42 ? 48 8B 78 ? 48 8B 87 ? ? ? ? 48 85 C0 74 ? 80 B8 ? ? ? ? ? 74 ? 33 C0

# TaskCancel

string "cannot cancel thread", first xref is da offset

```asm
.rdata:0000000007081F58 aCannotCancelTh db 'cannot cancel thread',0
.rdata:0000000007081F58                                         ; DATA XREF: sub_435AE30+B5↑o
.rdata:0000000007081F6D                 align 10h
```

so the offset is 0x435AE30

sig: 48 83 EC 28 48 8B 41 ? 4C 8B C9 48 8D 0D

# TaskSynchronize (TaskSync)

string "task.synchronize() may only be called from a script that is a descendant of an Actor", first xref

```asm
.rdata:0000000006F7DC20 aTaskSynchroniz db 'task.synchronize() may only be called from a script that is a des'
.rdata:0000000006F7DC20                                         ; DATA XREF: sub_4318B60:loc_4318C49↑o
```

so the offset is 0x4318B60

sig: 48 89 5C 24 ? 57 48 83 EC 40 48 8B D9 33 D2 48 85 C9 74 ? 48 8B 41 ? EB ? 48 8B C2 48 8B 40 ? 48 8B 48 ? 38 91 ? ? ? ? 75 ? 48 8D 0D ? ? ? ? E8 ? ? ? ? 84 C0 0F 84 ? ? ? ? BA 20 00 00 00 65 48 8B 04 25 ? ? ? ? ? ? ? ? ? ? 39 05 ? ? ? ? 0F 8E ? ? ? ? E9 ? ? ? ? 48 85 DB 74 ? 48 8B 53 ? 48 8B 42 ? 48 8B 78 ? 48 8B 87 ? ? ? ? 48 85 C0 74 ? 80 B8 ? ? ? ? ? 74 ? 8B 87
