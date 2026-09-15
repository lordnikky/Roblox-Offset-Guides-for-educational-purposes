# GetLuaStateForInstance

search string "script start", first xref, decompile it:

```c
    v220 = "Invalid Facet Access";
    sub_4921FD0(a1: 0, a2: "Invalid Facet Access");
  }
  if ( *((_QWORD *)&v216 + 1) != 0 )
    _InterlockedIncrement((volatile signed __int32 *)(*((_QWORD *)&v216 + 1) + 8LL));
  v252 = v216;
  if ( *(int *)(v22 + 5328) >= 3 )
  {
    v220 = "Invalid Facet Access";
    sub_4921FD0(a1: 0, a2: "Invalid Facet Access");
  }
  v23 = (_DWORD *)(sub_4248600(a1: v22 + 520, a2: &v225, a3: &v252) + 568); // <<-- the GetLuaStateForInstance
  LODWORD(v272) = (_DWORD)v23 - *v23;
  HIDWORD(v272) = (_DWORD)v23 - v23[1];
  v24 = v272;
  v231 = v272;
  if ( *((_QWORD *)&v252 + 1) != 0 )
    sub_7BC290(a1: *((_QWORD *)&v252 + 1));
  if ( v24 != 0 )
  {
    v25 = *(_QWORD *)(v24 + 96);
    v26 = *(_QWORD *)(*(_QWORD *)(v25 + 24) + 32LL);
  }
  else
  {
    v25 = 0;
    v26 = *(_QWORD *)(*(_QWORD *)&word_18 + 32LL);
  }
  v234 = *(_QWORD *)(*(_QWORD *)(v25 + 24) + 40LL);
  v235 = *(_QWORD *)(v234 + 448);
  *(_QWORD *)(v234 + 448) = "Script Start";		// <-- you're here
  if ( *(int *)(v26 + 5328) >= 3 )
  {
    v220 = "Invalid Facet Access";
    sub_4921FD0(a1: 0, a2: "Invalid Facet Access");

```

so the offset is 0x4248600
