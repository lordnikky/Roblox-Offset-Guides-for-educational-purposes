# GetProperty

search string "Unable to query property {}. It is not scriptable" or "Could not find property descriptor", if first string go to first xref, decompile:

```c
  __debugbreak();
  __debugbreak();
  __debugbreak();
  sub_1CE4BE0(a1: v4 + 472, a2: (__int64)&v77, a3: v78.m128i_i64, a4: 0); <-- getproperty 
  if ( BYTE4(v77) != 0 )
    return 0;
  v7 = *(_QWORD *)(v4 + 488)
     + 16LL * (unsigned int)(*(_DWORD *)(v4 + 496) & *(_DWORD *)(*(_QWORD *)(v4 + 480) + 4LL * (unsigned int)v77));
  if ( v7 == 0 || *(_DWORD *)(v7 + 8) != 0 )
    return 0;
  v8 = *(_QWORD *)v7;
  if ( (*(_DWORD *)(v8 + 140) & 0x10) == 0 )
  {
    v78.m128i_i64[0] = sub_7D6BB0(a1: *(_QWORD *)(v8 + 8));
    sub_16F8930(a1: "Unable to query property {}. It is not scriptable", a2: &v78); // <-- you're here 
  }
  if ( *(_QWORD *)(v8 + 56) != 0 )
  {
```

so the offset is 0x1CE4BE0

if seconds string, first xref decompile

```c
  v124 = v9;
  if ( *(_DWORD *)(v5 + 472) == 0
    || (sub_1CE4BE0(a1: v5 + 472, a2: (__int64)&v123, a3: &v124, a4: 0), BYTE4(v123) != 0) // <-- GetProperty
    || (v10 = (const char **)(*(_QWORD *)(v5 + 488)
                            + 16LL
                            * (unsigned int)(*(_DWORD *)(v5 + 496)
                                           & *(_DWORD *)(*(_QWORD *)(v5 + 480) + 4LL * (unsigned int)v123)))) == nullptr
    || (v123 = *v10) == nullptr )
  {
LABEL_229:
    sub_4921FD0(a1: 0, a2: (__int64)"Could not find property descriptor"); // <-- you're here
  }
  v11 = *(_QWORD *)sub_F34620(a1: v2, a2: v122, a3: &v123);
```

so the offset is 0x1CE4BE0


# GetPropertyData

string "ButtonRight", second xref and decompile

```c
  sub_1CE7A60(a1: v148, a2: (unsigned int)"ButtonRight", a3: (unsigned int)&v151, a4: 1056, a5: (__int64)&qword_88907C0); // <-- you're here
  xmmword_8890800 = *(_OWORD *)sub_7BCD30(a1: v178, a2: &qword_8941FC8, a3: 283);
  sub_1CB8390(a1: &v175, a2: &unk_6DD98B0);
  xmmword_8890810 = v175;
  sub_1CB83B0(a1: &v176, a2: &unk_6DDA1A0);
  xmmword_8890820 = v176;
  sub_E6D4F0(a1: &v177, a2: &off_6DDAD78);
  xmmword_8890830 = v177;
  sub_2B0FAF0(a1: (__int64)&qword_6D04820); // <-- GetPropertyData
  sub_2B0FAF0(a1: (__int64)"Touch"); // <-- GetPropertyData
  return &qword_88907C0;
}
```

so the offset is 0x2B0FAF0