# GetGlobalState

search string "assignVal", 7th xref, decompile, scroll up until you see 1 string "invalid facet access", and look under em:

```c
      sub_259B470(a1: v15, a2: 4, a3: v22);
    }
    if ( !v14 )
    {
      v105 = a1 - 2336;
      if ( v9 == 0 )
        v105 = -416;
      if ( *(int *)(v105 + 5080) >= 3 )
      {
        __wind
        {
          *(_QWORD *)&v243 = &aVarCanvasdetai[31002];
          sub_4974B80(a1: 0, a2: "Invalid Facet Access"); // <-- look for this
        }
        __unwind
        {
          sub_4974AF0();
        }
      }
      v15 = sub_41921C0(a1: v105, a2: a3, a3: a6); // <-- GetGlobalState
      v240[24] = 0;
      v54 = v212;
      sub_42484F0(a1: v9, a2: (_DWORD)v212, a3: v15, a4: v7, a5: a6, a6: (__int64)v240);
LABEL_74:
      v55 = (__int64 *)sub_C8FE50(a1: v54, a2: v242);
      v56 = *v55;
      v218 = *v55;
      v219 = v55[1];
```

so the offset is 0x41921C0

sig: 48 83 EC 38 8B 81 ? ? ? ? 90

