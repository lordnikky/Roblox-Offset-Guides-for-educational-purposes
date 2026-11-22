# GetFFlag

search for string `= Error-not-set`, first xref, scroll up:

```c
  if ( (unsigned __int8)sub_498CD90(a1: qword_8A927F8, (_DWORD)a2, a3, a4: 127, a5: 0, a6: 0) != 0 )
  {
    __eh34_enter_wind_state(-1, 0);
    Src[0] = 0;
    v20 = 0;
    v21 = 15;
    v5 = qword_8A927F8;
    v6 = qword_8A927F8 + 64;
    v17 = qword_8A927F8 + 64;
    v18 = 1;
    sub_89F0(a1: qword_8A927F8 + 64, a2: 0);
    __wind
    {
      sub_498D9B0(a1: v5, a2: v3, a3: Src, a4: 0); // <-- getfflag
    }
    __unwind
    {
      sub_787CC0(a1: &v17);
    }
    __wind
    {
      sub_8B30(a1: v6);
      v7 = v3[2];
      if ( v3[3] >= 0x10u )
        v3 = (_QWORD *)*v3;
    }
    __unwind
    {
      sub_4974AF0();
    }
    v8 = sub_8548F0(a1: a1 + 632, a2: v3, a3: v7);
    v9 = sub_852F00(a1: v8, a2: "="); // <-- anchor
    v10 = Src;
    if ( v21 >= 0x10 )
      v10 = (_QWORD *)Src[0];
    v11 = sub_8548F0(a1: v9, a2: v10, a3: v20);
    sub_852F00(a1: v11, a2: "\\n");
```

so the offset is 0x4977B90


# SetFFlag

search for string `_UniverseFilter`, first xref will be the setfflag

```asm
.rdata:000000000749EA48 aUniversefilter db '_UniverseFilter',0  ; DATA XREF: sub_4989CC0+163↑o
.rdata:000000000749EA48                                         ; .rdata:0000000006A58470↑o
```

so the offset is 0x4989CC0

# FFlagPointer

exists in file called flogdatabank.md, sorry for inconvinience 

# BooleanType

shift f4 and ctrl for ```FLog::ValueGetSet<bool>::`vftable'```

```asm
.rdata:0000000007054590 const FLog::ValueGetSet<bool>::`vftable' dq offset sub_4A404B0
.rdata:0000000007054590                                         ; DATA XREF: sub_4A3F680+16D↑o
```

so the offset is 0x7054590
