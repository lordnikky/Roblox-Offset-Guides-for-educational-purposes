# GetProperty

search string "Unable to query property {}. It is not scriptable" or "Could not find property descriptor", if first string go to first xref, decompile:

```c
  if ( *(_DWORD *)(v4 + 472) == 0 )
    return 0;
  sub_1D32FF0(a1: v4 + 472, a2: &v67, a3: &v68, a4: 0); // <-- GetProperty
  if ( BYTE4(v67) != 0 )
    return 0;
  v7 = *(_QWORD *)(v4 + 488)
     + 16LL * (unsigned int)(*(_DWORD *)(v4 + 496) & *(_DWORD *)(*(_QWORD *)(v4 + 480) + 4LL * (unsigned int)v67));
  if ( v7 == 0 || *(_DWORD *)(v7 + 8) != 0 )
    return 0;
  v8 = *(_QWORD *)v7;
  if ( (*(_DWORD *)(v8 + 140) & 0x10) == 0 )
  {
    v68.m128i_i64[0] = sub_7E39A0(a1: *(_QWORD *)(v8 + 8));
    sub_1719AD0(a1: "Unable to query property {}. It is not scriptable", a2: &v68); // <-- you're here
  }
  if ( *(_QWORD *)(v8 + 56) != 0 )
  {
```

so the offset is 0x1D32FF0

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

string "Unable to cast %s to %s", third xref and decompile

```c
    if ( v9[3] >= 0x10u )
      v9 = (_QWORD *)*v9;
    v11 = (_QWORD *)sub_2B0FB20(a1: v9); // <-- getpropertydata
    v12 = v11[2];
    if ( v11[3] >= 0x10u )
      v11 = (_QWORD *)*v11;
    v18[1] = v12;
    v18[0] = v11;
    v13 = sub_1CE80B0(a1: v10, a2: v18);
    if ( v13 != 0 )
    {
      v19 = *(_DWORD *)(v13 + 48);
      sub_8607F0(a1: a1 + 1, a2: &v19);
      v14 = sub_85F410();
      *a1 = v14;
      if ( v14 == sub_85F410() )
      {
        if ( a1[1] == 0 )
          return nullptr;
        return v8;
      }
LABEL_19:
      sub_4924110(a1: "Variant cast failed");
    }
  }
  v15 = sub_85F280();
  sub_7D6BB0(a1: *(_QWORD *)(v15 + 8));
  v16 = (const char *)sub_7D6BB0(a1: *(_QWORD *)(*a1 + 8));
  sub_4924110(a1: "Unable to cast %s to %s", v16, v17); //<-- you are here
```

so the offset is 0x2B0FB20
