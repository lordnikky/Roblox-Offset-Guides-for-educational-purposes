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

search for string `[FLog::FastLogValueChanged] Setting variable {}" or "[FLog::FastLogValueChanged] ...(previously unknown)...`, first xref will be the setfflag

```asm
.rdata:0000000006FD61A8 aFlogFastlogval db '[FLog::FastLogValueChanged] Setting variable {}',0
.rdata:0000000006FD61A8                                         ; DATA XREF: sub_493A3A0+261↑o
.rdata:0000000006FD61D8 aFlogFastlogval_0 db '[FLog::FastLogValueChanged] ...(previously unknown)...',0
.rdata:0000000006FD61D8                                         ; DATA XREF: sub_493A3A0+328↑o
```

so the offset is 0x493A3A0

# FFlagPointer
searching for like any fflag name will also work, im just using this random one
search for string `DebugWinDisableUpdates`, second xref, decompile:

```c
__int64 sub_729960()
{
  __int64 v0; // rbx
  __int64 v1; // rdi
  _QWORD v3[3]; // [rsp+30h] [rbp-28h] BYREF
  char v4; // [rsp+48h] [rbp-10h]

  v0 = qword_8C86398;
  v1 = qword_8C86398 + 64;
  v3[2] = qword_8C86398 + 64;
  v4 = 1;
  sub_89F0(a1: qword_8C86398 + 64, a2: 0);
  v3[0] = "DebugWinDisableUpdates";
  v3[1] = 22;
  sub_49FE870(a1: v0, a2: v3, a3: &byte_848ECA0, a4: 1);
  return sub_8B30(a1: v1);
}
```

v0 = and that will be the FFlagPointer

# BooleanType

shift f4 and ctrl for ```FLog::ValueGetSet<bool>::`vftable'```

```asm
.rdata:0000000007054590 const FLog::ValueGetSet<bool>::`vftable' dq offset sub_4A404B0
.rdata:0000000007054590                                         ; DATA XREF: sub_4A3F680+16D↑o
```

so the offset is 0x7054590
