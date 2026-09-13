# tclone

search for string "table has a protected metatable" second xref

```asm
.rdata:0000000007078A40 aTableHasAProte db 'table has a protected metatable',0
.rdata:0000000007078A40                                         ; DATA XREF: sub_5607360:loc_560745E↑o
.rdata:0000000007078A40                                         ; sub_5607560:loc_560762A↑o
```

```c
__int64 __fastcall sub_5607560(_QWORD *a1)
{
  unsigned __int64 v1; // rax
  __int64 v3; // r8
  __int64 v4; // r9
  __int128 v6; // [rsp+20h] [rbp-18h]
  v1 = a1[4];
  if ( v1 >= a1[5] || (_UNKNOWN *)v1 == &unk_63CDF48 || *(_DWORD *)(v1 + 12) != 7 )
    sub_26FF360(a1, a2: 1, a3: 7);
  if ( (unsigned int)sub_2701A50(a1, a2: 1, a3: &qword_6E26E40) != 0 )
    sub_26FF1F0(a1, a2: 1, a3: "table has a protected metatable");
  *(_QWORD *)&v6 = sub_27215A0(a1, a2: *(_QWORD *)a1[4], a3: v3, a4: v4);
  HIDWORD(v6) = 7;
  if ( (unsigned __int64)(a1[5] + 16LL) > *(_QWORD *)(a1[2] + 16LL) && (unsigned int)sub_26F7B00(a1, a2: 1) == 0 )
  {
    sub_2722360((__int64)a1, a2: "stack overflow");
    sub_26FA450(a1);
  }
  *(_OWORD *)a1[5] = v6;
  a1[5] += 16LL;
  return 1;
}
```

so the offset is 0x5607560