wont only conain taskdefer but will have bit more stuff

# TaskDefer

Search for string "task.defer is not available for AuroraScripts", first xref will be it

```asm

.rdata:0000000006F7DCA0 aTaskDeferIsNot db 'task.defer is not available for AuroraScripts',0

.rdata:0000000006F7DCA0                                         ; DATA XREF: sub\_4319B60:loc\_4319FC2↑o

```

so the offset is 0x4319B60

# TaskSpawn

string "task.spawn is not available for AuroraScripts", first xref will be it

```asm

.rdata:0000000006F7DD28 aTaskSpawnIsNot db 'task.spawn is not available for AuroraScripts',0

.rdata:0000000006F7DD28                                         ; DATA XREF: sub\_431A020:loc\_431A1DE↑o

```

so the offset is 0x431A020


# TaskDelay

string "task.delay is not available for AuroraScripts" first xref bla bla, didn't you notice the pattern already lol

```asm

.rdata:0000000006F7DFE8 aTaskDelayIsNot db 'task.delay is not available for AuroraScripts',0

.rdata:0000000006F7DFE8                                         ; DATA XREF: sub\_431A3B0:loc\_431A66A↑o

```
well also can be found via "task.delay(t, f)"

so the offset is 0x431A3B0


# TaskWait

string "task.wait is not available for AuroraScripts" first xref, done

```asm
.rdata:0000000006F7DFA8 aTaskWaitIsNotA db 'task.wait is not available for AuroraScripts',0
.rdata:0000000006F7DFA8                                         ; DATA XREF: sub_431A6B0:loc_431A874↑o
``` 

also "task.wait(t)"


# TaskDesynchronize (TaskDesync(

seach string "task.desynchronize() may only be called from a script that is a d", first xref will be it

```asm
.rdata:0000000006F7DBA0 aTaskDesynchron db 'task.desynchronize() may only be called from a script that is a d'
.rdata:0000000006F7DBA0                                         ; DATA XREF: sub_4318F70:loc_431905C↑o
```

so the offset is 0x4318F70


# TaskCancel

string "Cannot call task.%s on a thread that is already '%s' in the task library", first xref is da offset

```asm
.rdata:0000000006F7DB00 aCannotCallTask db 'Cannot call task.%s on a thread that is already ',27h,'%s',27h,' '
.rdata:0000000006F7DB00                                         ; DATA XREF: sub_4318580+7A↑o
.rdata:0000000006F7DB00                                         ; sub_431A6B0+235↑o
```

so the offset is 0x4318580

# TaskSynchronize (TaskSync)

string "task.synchronize() may only be called from a script that is a descendant of an Actor", first xref

```asm
.rdata:0000000006F7DC20 aTaskSynchroniz db 'task.synchronize() may only be called from a script that is a des'
.rdata:0000000006F7DC20                                         ; DATA XREF: sub_4318B60:loc_4318C49↑o
```

so the offset is 0x4318B60
