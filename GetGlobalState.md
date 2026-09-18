# GetGlobalState

search string "assignVal", 7th xref, decompile, scroll up until you see 2 strings "invalid facet access", and look under em:

```c
    sub_2750300(a1: v15, a2: 4, a3: v74);
  }
  v104 = a1 - 2632;
  if ( v9 == 0 )
    v104 = -504;
  if ( *(int *)(v104 + 5400) >= 3 )
  {
    *(_QWORD *)&v215 = "Invalid Facet Access";
    sub_498BD80(a1: 0, a2: "Invalid Facet Access");
  }
  v15 = sub_421A7A0(a1: v104); // <-- GetGlobalState
  v238[24] = 0;
  v53 = a2;
  sub_42CD770(a1: v9, a2, a3: v15, a4: v7, a5: (__int64)a6, a6: (__int64)v238);
LABEL_74:
  v54 = (__int64 *)sub_E2AC20(a1: v53, a2: v240);
  v217 = *v54;
  v55 = v217;
  v218 = v54[1];
  *v54 = 0;
  v54[1] = 0;
  if ( v55 != 0 )
    v56 = *(_QWORD *)(v55 + 40);
```

so the offset is 0x421A7A0
