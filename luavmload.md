# LuaVMLoad

search for string "loadstring() is not available", first xref, decompile, scroll down until you see "stack overflow" and stop here, somewhere at line ~300 there will be this

```c
    *((_BYTE *)v66 + v35) = 0;
  }
  v43 = *(_QWORD *)(sub_4100CB0(a1: v64, a2: v66) + 8);
  if ( dword_8495C90 != 0 )
  {
    v45 = sub_490A0E0();
    *(_QWORD *)sub_4250(a1: qword_8495C50) = v45;
    v44 = sub_41B3B50(a1, a2: (_QWORD *)(v43 + 24), a3: v40, a4: 0); // <-- luavmload
    *(_QWORD *)sub_4250(a1: qword_8495C50) = 0;
  }
  else
  {
    v44 = sub_41B3B50(a1, a2: (_QWORD *)(v43 + 24), a3: v40, a4: 0); // <-- luavmload
  }
  sub_1050140(a1: v64);
  if ( v68 >= 0x10 )
  {
    v48 = v66[0];
    v49 = v66[0];
    if ( v68 + 1 >= 0x1000 )
    {
      v48 = *(_QWORD *)(v66[0] - 8LL);
      v49 = v66[0] - v48;
      if ( v66[0] - v48 - 8 > 0x1F )
        sub_5A59170();
    }
    sub_4905B60(a1: v48, a2: v49, a3: v46, a4: v47);
  }
  v67 = 0;
  v68 = 15;
  LOBYTE(v66[0]) = 0;
  if ( v44 != 0 )
  {
    if ( (unsigned __int64)(a1[5] + 16LL) > *(_QWORD *)(a1[2] + 16LL) && (unsigned int)sub_26F7B00(a1, a2: 1) == 0 )
    {
      sub_2722360(a1, a2: "stack overflow"); 
      sub_26FA450(a1);
    }
    *(_DWORD *)(a1[5] + 12LL) = 0;
    a1[5] += 16LL;
    if ( (*(_BYTE *)a1 & 4) != 0 )
    {
      v53 = a1[3];
```

so the offset is 0x41B3B50