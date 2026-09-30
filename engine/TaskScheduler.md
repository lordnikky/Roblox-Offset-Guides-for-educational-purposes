# TaskSchedulerPTR

search for string "AppInitializer", first xref, decompile:

```c
  sub_2AD8F60(a1: qword_8B5CEE8, a2: "AppInitializer", a3: v7, a4: 0, a5: v5);
```

that qword is taskschedulerptr


# TaskSchedulerTargetFPS

search for string "TS::Step", first xref decompile:

```c
        }
      }
      qword_8AFF1E0 = sub_2AA6830(a1: (unsigned int)"Jobs", a2: (unsigned int)"TS::Step", a3: -1, a4: v5, a5: 255); // <-- you're here
      sub_1350(a1: &dword_8AFF1D8);
    }
  }
  memset(v148, 0, 32);
  *(__m128i *)&v148[4] = _mm_load_si128((const __m128i *)&xmmword_722DA10);
  *(_OWORD *)&v148[6] = 0;
  v149 = 0;
  v150 = 0;
  v151 = 0;
  v152 = 0;
  v153 = 0;
  v154 = 0;
  v155 = 0;
  sub_2A2AC30(a1: (unsigned int)v148, a2: qword_8AFF1E0, a3: -1, a4: 0, a5: 0);
  v6 = dword_8319D48;   // <-- the offset
  sub_8E60(a1: v157, a2: a1 + 144, a3: 0, a4: 0);
  v7 = *(_DWORD *)(a1 + 260);
  v122 = v7;
  v8 = sub_7690();
  v9 = v8;
  v10 = *(_QWORD *)(a1 + 168);
```

so the offset is 0x8319D48
