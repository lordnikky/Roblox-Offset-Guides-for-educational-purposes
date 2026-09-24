# TaskSchedulerPTR

search for string "AppInitializer", first xref, decompile:

```c
  sub_2AD8F60(a1: qword_8B5CEE8, a2: "AppInitializer", a3: v7, a4: 0, a5: v5);
```

that qword is taskschedulerptr


# TaskSchedulerTargetFPS

search for string "TS::Step", first xref decompile:

```c
      qword_89DD820 = sub_2B801C0(
                        a1: (unsigned int)&aOcnewmtfixstag[-754112],
                        a2: (unsigned int)"TS::Step", // <-- you're here
                        a3: -1,
                        a4: v4,
                        a5: 255);
      sub_1330(a1: &dword_89DD818);
    }
  }
  memset(v143, 0, 32);
  *(__m128i *)&v143[4] = _mm_load_si128((const __m128i *)&xmmword_714D4A0);
  *(_OWORD *)&v143[6] = 0;
  v144 = 0;
  v145 = 0;
  v146 = 0;
  v147 = 0;
  v148 = 0;
  v149 = 0;
  v150 = 0;
  sub_2B057F0(a1: (unsigned int)v143, a2: qword_89DD820, a3: -1, a4: 0, a5: 0);
  v5 = dword_8227738; // <-- your desired offset
  sub_5E30(a1: v152, a2: a1 + 144, a3: 0, a4: 0);
```

so the offset is 0x8227738
