# GetGlobalState

search string "assignVal", 7th xref, decompile, scroll up until you see 2 strings "invalid facet access", and look under em:

```c
      if ( v9 == 0 )
        v100 = -488;
      if ( *(int *)(v100 + 5416) >= 3 )
      {
        __wind
        {
          v235 = "twareCodec::sendFrameInternal, pts: {}";
          sub_495EC80(a1: 0, a2: "Invalid Facet Access"); // <-- look for this
        }
        __unwind
        {
          sub_495EBF0();
        }
      }
      v15 = sub_41F2300(a1: v100, a2: a3, a3: a6); // <-- getglobalstate
      v232[24] = 0;
      v52 = v207;
      sub_42A6D10(a1: v9, a2: (_DWORD)v207, a3: v15, a4: v7, a5: a6, a6: (__int64)v232);
LABEL_74:
      v53 = (__int64 *)sub_D30300(a1: v52, a2: v234);
      v54 = *v53;
      v212 = *v53;
      v213 = v53[1];
      *v53 = 0;
```

so the offset is 0x41F2300

