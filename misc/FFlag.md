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

sig: 48 89 5C 24 ? 55 56 57 48 83 EC 50 48 8B 05 ? ? ? ? 48 33 C4 48 89 44 24 ? 41 0F B6 F1

# SetFFlag

search for string `[FLog::FastLogValueChanged] Setting variable {}" or "[FLog::FastLogValueChanged] ...(previously unknown)...`, first xref will be the setfflag

```asm
.rdata:0000000006FD61A8 aFlogFastlogval db '[FLog::FastLogValueChanged] Setting variable {}',0
.rdata:0000000006FD61A8                                         ; DATA XREF: sub_493A3A0+261↑o
.rdata:0000000006FD61D8 aFlogFastlogval_0 db '[FLog::FastLogValueChanged] ...(previously unknown)...',0
.rdata:0000000006FD61D8                                         ; DATA XREF: sub_493A3A0+328↑o
```

so the offset is 0x493A3A0

sig: 48 89 5C 24 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC D0 01 00 00 48 8B 05 ? ? ? ? 48 33 C4 48 89 85 ? ? ? ? 44 89 4C 24

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

byte (or qword or unk) that is after a3: will be the offset, 0x848ECA0


# BooleanType

search for string `AnimGraphServerAuthorityNodeIndices`, first xref, decompile:

```c
__int64 sub_1A71B10()
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
  v3[0] = "AnimGraphServerAuthorityNodeIndices";
  v3[1] = 35;
  sub_49FE3E0(a1: v0, a2: v3, a3: &byte_8431A2D, a4: 4);
  return sub_8B30(a1: v1);
}
```

double click the sub_ which contains offset of the fflag itself ( one with a3: byte unk or qword)

```c
      *(_QWORD *)(v21 + 48) = 0;
      *(_QWORD *)(v21 + 56) = 0;
      *(_QWORD *)(v21 + 64) = 0;
      *(_QWORD *)(v21 + 72) = 0;
      *(_QWORD *)(v21 + 80) = 0;
      *(_QWORD *)(v21 + 88) = 0;
      *(_QWORD *)(v21 + 96) = 0;
      *(_QWORD *)(v21 + 104) = 0;
      *(_QWORD *)(v21 + 112) = 0;
      *(_QWORD *)(v21 + 128) = 0;
      *(_QWORD *)(v21 + 136) = 15;
      *(_QWORD *)(v21 + 144) = 0;
      *(_QWORD *)(v21 + 160) = 0;
      *(_QWORD *)(v21 + 168) = 15;
      *(_DWORD *)(v21 + 176) = a4;
      *(_DWORD *)(v21 + 180) = 4;
      *(_BYTE *)(v21 + 184) = 0;
      *(_QWORD *)v21 = &FLog::ValueGetSet<bool>::`vftable'; // <-- double click this
      v23 = v47;
      *((_QWORD *)v22 + 24) = v47;
      v22[200] = *v23;
      v47 = v22;
      if ( v16 != v48[1] )
      {
        if ( (*(unsigned __int8 (__fastcall **)(_QWORD))(**(_QWORD **)(v16 + 48) + 88LL))(a1: *(_QWORD *)(v16 + 48)) != 0 )
        {
          v24 = *(void (__fastcall **)(_BYTE *, __int64, __int64, __int128 *))(*(_QWORD *)v22 + 32LL);
          v25 = (*(__int64 (__fastcall **)(_QWORD, _QWORD *))(**(_QWORD **)(v16 + 48) + 264LL))(
                  a1: *(_QWORD *)(v16 + 48),
                  a2: pExceptionObject);
```

double click the flog you'll be put here:

```asm
.rdata:0000000006DA3DF8 ; const FLog::ValueGetSet<bool>::`vftable'
.rdata:0000000006DA3DF8 ??_7?$ValueGetSet@_N@FLog@@6B@ dq offset sub_497EDA0
.rdata:0000000006DA3DF8                                         ; DATA XREF: sub_497C690+1D8↑o                                      ; DATA XREF: sub_49A9780+1D8↑o
```

so the offset is 0x6DA3DF8
