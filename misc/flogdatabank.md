# flogdatabank

string `[FLog::SingleSurfaceApp] leaveUGCGameInternal`, first xref decompile

```c
    sub_4972020(
      a1: (unsigned int)&v61,
      a2: (unsigned int)"[FLog::SingleSurfaceApp] leaveUGCGameInternal",
      a3: 0,
      a4: 0,
      a5: 0,
      a6: 0,
      a7: 0);
  }
  if ( a3 != 0 )
  {
    sub_13C28C0(a1, a2: 1);
    sub_4C76630();
  }
  sub_13C3510(a1, a2: 0);
  v7 = qword_84E2BF8;
  v54 = (volatile signed __int64 *)(qword_84E2BF8 + 64);
  v55 = 1;
  sub_2E12FD0(a1: qword_84E2BF8 + 64);
```

the qword_ + 64 is the thing, so it is 0x84E2BF8
