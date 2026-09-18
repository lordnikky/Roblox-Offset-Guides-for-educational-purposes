# GetFFlag

search for string "not declared!", second xref, decompile, and scroll up a bit:

```c
LABEL_136:
        v87 = qword_887CA40;
        v88 = qword_887CA40 + 64;
        v135.m128_u64[0] = qword_887CA40 + 64;
        v89 = sub_5A2B400(a1: qword_887CA40 + 64);
        if ( v89 != 0 )
          sub_5A2B9D0(a1: v89);
        v90 = sub_493AF20(a1: v87, a2: v152, a3: (__int64)&v155, a4: 1); <-- getfflag
        sub_5A2B460(a1: v88);
        if ( v90 != 0 )
        {
          if ( v51 < 4 )
          {
            v94 = false;
          }
          else
          {
            v91 = 0;
            while ( 1 )
            {
              v92 = *(_BYTE *)(*(_QWORD *)v137 + v91++);
              if ( v92 != aUser_0[v91 - 1] )
                break;
              if ( v91 == 4 )
              {
                v93 = 0;
                goto LABEL_144;
              }
            }
            v93 = v92 < (unsigned __int8)aUser_0[v91 - 1] ? -1 : 1;
LABEL_144:
            v94 = v93 == 0;
          }
          v82 = "not declared!";	<-- you're here
          if ( v94 )
            v82 = "UserFlag";
        }
        else
```

so the offset is 0x493AF20


# SetFFlag

search for string "[FLog::FastLogValueChanged] Setting variable {}" or "[FLog::FastLogValueChanged] ...(previously unknown)...", first xref will be the setfflag

```asm
.rdata:0000000006FD61A8 aFlogFastlogval db '[FLog::FastLogValueChanged] Setting variable {}',0
.rdata:0000000006FD61A8                                         ; DATA XREF: sub_493A3A0+261↑o
.rdata:0000000006FD61D8 aFlogFastlogval_0 db '[FLog::FastLogValueChanged] ...(previously unknown)...',0
.rdata:0000000006FD61D8                                         ; DATA XREF: sub_493A3A0+328↑o
```

so the offset is 0x493A3A0


# FFlagPointer

search for string "DebugWinDisableUpdates", second xref, decompile:

```c
__int64 sub_7CD3F0()
{
  return sub_49A9CA0(a1: qword_88FC7C8, a2: "DebugWinDisableUpdates", a3: &byte_815FBA8, a4: 1);
}
```

that qword will be the FFlagPointer, so the offset is 0x88FC7C8


# BooleanType

search for string "AnimGraphServerAuthorityNodeIndices", first xref, decompile:

```c
__int64 sub_1A7F4F0()
{
  return sub_49A9780(
           a1: (_QWORD *)qword_88FC7C8,
           a2: (__int64)"AnimGraphServerAuthorityNodeIndices",
           a3: &byte_810290F,
           a4: 4);
}
```

double click the first return sub_, scroll down until you see this:

```c
  *(_QWORD *)(v21 + 40) = 0;
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
  *(_QWORD *)v21 = &FLog::ValueGetSet<bool>::`vftable'; // <-- double click the flog
  *(_QWORD *)(v21 + 192) = a3;
  *(_BYTE *)(v21 + 200) = *a3;
  if ( v16 != a1[1] )
  {
    if ( (*(unsigned __int8 (__fastcall **)(_QWORD))(**(_QWORD **)(v16 + 48) + 88LL))(a1: *(_QWORD *)(v16 + 48)) != 0 )
    {
      v23 = (*v22)[4];
      v24 = (*(__int64 (__fastcall **)(_QWORD, _QWORD *))(**(_QWORD **)(v16 + 48) + 264LL))(
              a1: *(_QWORD *)(v16 + 48),
              a2: pExceptionObject);
      ((void (__fastcall *)(void (__fastcall ***)(_QWORD, __int64), __int64, __int64, __int128 *))v23)(
        a1: v22,
```

double click the flog you'll be put here:

```asm
.rdata:0000000006D1DCC0 ; const FLog::ValueGetSet<bool>::`vftable'
.rdata:0000000006D1DCC0 ??_7?$ValueGetSet@_N@FLog@@6B@ dq offset sub_49ABE90
.rdata:0000000006D1DCC0                                         ; DATA XREF: sub_49A9780+1D8↑o
```

so the offset is 0x6D1DCC0


# BoolValueType

search for string "DebugWinDisableUpdates", second xref and decompile

```c
__int64 sub_7CD3F0()
{
  return sub_49A9CA0(a1: qword_88FC7C8, a2: "DebugWinDisableUpdates", a3: &byte_815FBA8, a4: 1);
}
```

double click the first sub, scroll down until you see this:

```c
 ( v21 == 0 )
  {
    sub_7B39A0(a1: pExceptionObject);
    CxxThrowException(pExceptionObject, pThrowInfo: (_ThrowInfo *)&_TI2_AVbad_alloc_std__);
  }
  *(_QWORD *)(v21 + 8) = 0;
  *(_QWORD *)(v21 + 24) = 0;
  *(_QWORD *)(v21 + 32) = 15;
  *(_QWORD *)(v21 + 40) = 0;
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
  *(_QWORD *)v21 = &FLog::ValueGetSet<FFlag::Value>::`vftable'; // <-- double click flog
  *(_QWORD *)(v21 + 192) = a3;
  *(_BYTE *)(v21 + 200) = *(_BYTE *)a3;
  *(_OWORD *)(v21 + 208) = *(_OWORD *)(a3 + 8);
  if ( v16 != a1[1] )
  {
    if ( (*(unsigned __int8 (__fastcall **)(_QWORD))(**(_QWORD **)(v16 + 48) + 88LL))(a1: *(_QWORD *)(v16 + 48)) != 0 )
    {
      v23 = (*v22)[4];
      v24 = (*(__int64 (__fastcall **)(_QWORD, _QWORD *))(**(_QWORD **)(v16 + 48) + 264LL))(
              a1: *(_QWORD *)(v16 + 48),
              a2: pExceptionObject);
      ((void (__fastcall *)(void (__fastcall ***)(_QWORD, __int64), __int64, __int64, __int128 *))v23)(
        a1: v22,
        a2: v24,
        a3: 127,
        a4: &v51);
      if ( v54 >= 0x10 )
```

Double click the flog:

```asm
rdata:0000000006D1DA90 ; const FLog::ValueGetSet<class FFlag::Value>::`vftable'
.rdata:0000000006D1DA90 ??_7?$ValueGetSet@VValue@FFlag@@@FLog@@6B@ dq offset sub_49ABE90
.rdata:0000000006D1DA90                                         ; DATA XREF: sub_49A9CA0+1D8↑o
```

so the offset is 0x6D1DA90
