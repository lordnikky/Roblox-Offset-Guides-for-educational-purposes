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

<details>

<summary><b>verify:</b></summary>

takes 4 args, should look like this

```c
__int64 __fastcall sub_1CA05A0(__int64 a1, __int64 a2, __int64 *a3, int a4)
{
  int v4; // r13d
  __int64 v5; // rbp
  unsigned __int64 v6; // rax
  __int64 v8; // r14
  unsigned int v10; // r15d
  int v11; // esi
  unsigned int v12; // ebx
  int v13; // r8d
  __int64 v14; // rax
  unsigned int v15; // r9d

  v4 = *(_DWORD *)(a1 + 28);
  v5 = *a3;
  v6 = (unsigned __int64)*a3 >> 3;
  v8 = *(_QWORD *)(a1 + 8);
  v10 = (unsigned int)(-1640531535 * v6) >> (32 - v4);
  v11 = (-1640531535 * (_DWORD)v6) << v4;
  v12 = v10 & 0xFFFFFFF0;
LABEL_2:
  v13 = 0;
  while ( 1 )
  {
    v14 = v12 + (((_BYTE)v10 + (unsigned __int8)(0x4D72EB980136AF5CuLL >> (4 * (unsigned __int8)v13))) & 0xF);
    v15 = *(_DWORD *)(v8 + 4 * v14);
    if ( v15 == -1 )
      break;
    if ( ((v11 ^ v15) & ~*(_DWORD *)(a1 + 24)) == 0
      && v5 == *(_QWORD *)(*(_QWORD *)(*(_QWORD *)(a1 + 16) + 16LL * (*(_DWORD *)(a1 + 24) & v15)) + 8LL) )
    {
      *(_BYTE *)(a2 + 4) = 0;
      goto LABEL_18;
    }
    if ( (unsigned int)++v13 >= 0x10 )
    {
      v12 = (v12 + 16) & ((1 << v4) - 1);
      goto LABEL_2;
    }
  }
  if ( a4 != 0 )
  {
    if ( unk_829C78C != 0 && unk_86A7FB8 != 0 && a4 == 1 && *(_DWORD *)a1 == *(_DWORD *)(a1 + 4) )
    {
      sub_1CA08C0(a1, a2, a3);
      return a2;
    }
    *(_DWORD *)(v8 + 4 * v14) = v11;
    if ( a4 == 1 )
      *(_DWORD *)(*(_QWORD *)(a1 + 8) + 4 * v14) |= (*(_DWORD *)a1)++;
  }
  *(_BYTE *)(a2 + 4) = 1;
LABEL_18:
  *(_DWORD *)a2 = v14;
  return a2;
}
```
  
</details>

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

<details>

<summary><b>verify:</b></summary>

takes 2 args when called checks if pointer that it returned is correct, if not errors with varitant cast failed

```c
    v15 = sub_1CA3D10(a1: v8, a2: v20);
    if ( v15 != 0 )
    {
      LODWORD(v21) = *(_DWORD *)(v15 + 48);
      sub_7A8930(a1: a1 + 1, a2: &v21);
      v16 = sub_7A7400();
      *a1 = v16;
      if ( v16 == sub_7A7400() )
      {
        if ( a1[1] == 0 )
          return nullptr;
        return v9;
      }
LABEL_27:
      sub_4976D00(a1: "Variant cast failed");
    }
```

function itself looks like this

```c
__int64 __fastcall sub_1CA3D10(_QWORD *a1, __m128i *a2)
{
  __m128i v2; // xmm1
  unsigned __int8 *v3; // rdx
  unsigned __int64 v4; // xmm0_8
  unsigned int v5; // r8d
  unsigned __int8 *i; // r9
  int v7; // eax
  __int64 v8; // r9
  unsigned __int64 v9; // rax

  v2 = *a2;
  v3 = (unsigned __int8 *)a2->m128i_i64[0];
  v4 = _mm_srli_si128(v2, 8).m128i_u64[0];
  v5 = 0x811C9DC5;
  for ( i = &v3[v4]; v3 != i; v5 = 16777619 * (v5 ^ v7) )
    v7 = *v3++;
  v8 = a1[10];
  v9 = (8LL * a1[11]) >> 3;
  while ( (__int64)v9 > 0 )
  {
    if ( *(_DWORD *)(v8 + 8 * (v9 >> 1)) >= v5 )
    {
      v9 >>= 1;
    }
    else
    {
      v8 += 8 * (v9 >> 1) + 8;
      v9 += -1LL - (v9 >> 1);
    }
  }
  if ( v8 == a1[10] + 8LL * a1[11] || *(_DWORD *)v8 != v5 )
    return 0;
  else
    return a1[8] + 56LL * *(unsigned __int16 *)(v8 + 4);
}
```
  
</details>
