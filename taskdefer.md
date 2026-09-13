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