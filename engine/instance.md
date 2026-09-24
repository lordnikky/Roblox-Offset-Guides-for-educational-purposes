# instance.new

idk if this is any useful but its jsut what i found 

search for string `"Unable to create an Instance of type \"%s\""`

```asm
.rdata:0000000006FEA618 aUnableToCreate_2 db 'Unable to create an Instance of type "%s"',0
.rdata:0000000006FEA618                                         ; DATA XREF: sub_43297B0+C80↑o
```

first xref is the offset

so the offset is 0x43297B0


# InstanceFindFirstAncestorImpl

search for string "FindFirstAncestorWhichIsA", first xref will be it:

```asm
.rdata:0000000006E04D18 aFindfirstances_1 db 'FindFirstAncestorWhichIsA',0
.rdata:0000000006E04D18                                         ; DATA XREF: sub_5AF4E0:loc_5AF5B0↑o
.rdata:0000000006E04D18                                         ; sub_1F22EF0+4B706C8↑o
```

so the offset is 0x5AF4E0


# InstanceGetAttribute

search for string "[DFLog::HugeHugePersistentLog] Part {} is too large, treating as persistent", first xref will be it:

```asm
.rdata:00000000070271F0 aDflogHugehugep db '[DFLog::HugeHugePersistentLog] Part {} is too large, treating as '
.rdata:00000000070271F0                                         ; DATA XREF: sub_48001B0+AA4↑o
.rdata:0000000007027231                 db 'persistent.',0
.rdata:000000000702723D                 align 20h
```

so the offset is 0x48001B0


# InstanceFindFirstChild

search for string "FindFirstChild", first xref will be it:

```asm
.rdata:0000000006E04B88 aFindfirstchild_0 db 'FindFirstChild',0 ; DATA XREF: sub_5B2B20:loc_5B2BFF↑o
.rdata:0000000006E04B88                                         ; sub_1F22EF0+4B706D8↑o
```

so the offset is 0x5B2B20


# InstanceFindFirstChildOfClass

search for string "FindFirstChildOfClass", yeah yeah it'll be first xref bruh:

```asm 
.rdata:0000000006E04D38 aFindfirstchild db 'FindFirstChildOfClass',0
.rdata:0000000006E04D38                                         ; DATA XREF: sub_5AF750:loc_5AF820↑o
.rdata:0000000006E04D38                                         ; sub_1F22EF0+4B706E8↑o
```

so the offset is 0x5AF750


# InstanceGetChildren

search for string "GetChildren", yup first xref strikes again:

```asm
.rdata:0000000006E04C80 aGetchildren    db 'GetChildren',0      ; DATA XREF: sub_5B05D0:loc_5B06AF↑o
.rdata:0000000006E04C80                                         ; sub_1F22EF0+4B70758↑o
```

so the offset is 0x5B05D0


# InstanceIndex

string "InstanceHandle is not enabled yet!" and guess what, its first xref

```
asm.rdata:0000000006FDDCA0 aInstancehandle_1 db 'InstanceHandle is not enabled yet!',0
.rdata:0000000006FDDCA0                                         ; DATA XREF: sub_41A26F0:loc_41A28ED↑o
.rdata:0000000006FDDCA0                                         ; sub_41A2900:loc_41A2AD3↑o ...
```

so the offset is 0x41A26F0
