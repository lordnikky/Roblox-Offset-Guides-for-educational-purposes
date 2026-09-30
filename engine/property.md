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
    }
    v13 = v12[2];
    if ( v12[3] >= 0x10u )
      v12 = (_QWORD *)*v12;
    v19[0] = v12;
    v19[1] = v13;
    v14 = sub_1D6C050(a1: v7, a2: v19); // <-- getpropertydata
    if ( v14 != 0 )
    {
      LODWORD(v20) = *(_DWORD *)(v14 + 48);
      sub_890110(a1: a1 + 1, a2: &v20);
      v15 = sub_88ED30();
      *a1 = v15;
      if ( v15 == sub_88ED30() )
      {
        if ( a1[1] == 0 )
          return nullptr;
        return v8;
      }
LABEL_27:
      sub_49A60B0(a1: "Variant cast failed");
    }
  }
  v16 = sub_88EBA0();
  sub_8080D0(a1: *(_QWORD *)(v16 + 8));
  v17 = (const char *)sub_8080D0(a1: *(_QWORD *)(*a1 + 8));
  sub_49A60B0(a1: "Unable to cast %s to %s", v17, v18); // <-- you're here
}
```

so the offset is 0x1D6C050
