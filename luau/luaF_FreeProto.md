sigh, they changed it again.

# luaF_FreeProto

NO STRING, take luaC_step offset, without it you can't proceed (i have guide on it), decompile luaC_step

```c
  int v30; // ecx
  double v31; // xmm2_8
  double v32; // xmm1_8
  __int64 v33; // rcx
  double v34; // xmm0_8
  unsigned __int64 v35; // rax
  void (__fastcall *v36)(__int64, _QWORD); // rax

  v2 = *(_QWORD *)(a1 + 56);
  v5 = *(_QWORD *)(v2 + 80) - *(_QWORD *)(v2 + 72);
  v6 = *(void (__fastcall **)(__int64, _QWORD))(v2 + 1640);
  v7 = *(_DWORD *)(v2 + 68) * *(_DWORD *)(v2 + 64) / 100;
  if ( v6 != nullptr )
    v6(a1, a2: 0);
  if ( *(_BYTE *)(v2 + 57) == 0 )
  {
    v8 = sub_2646D70();
    v9 = *(_BYTE *)(v2 + 57) == 0;
    *(double *)(v2 + 21872) = v8;
    if ( v9 )
    {
      v10 = sub_2646D70();
      *(double *)(v2 + 22176) = v10;
      *(double *)(v2 + 22168) = v10 - *(double *)(v2 + 21960);
    }
  }
  v11 = sub_2646D70();
  if ( a2 != 0 && v5 * *(int *)(v2 + 68) / 0x64 > v7 )
    v7 = v5 * *(int *)(v2 + 68) / 0x64;
  v12 = *(unsigned __int8 *)(v2 + 57);
  v13 = sub_26158C0(a1, a2: v7); // <-- find this
  v14 = sub_2646D70() - v11;
  if ( v12 != 0 )
  {
    if ( v12 != 1 && v12 != 2 )
    {
      if ( v12 == 3 )
      {
        *(double *)(v2 + 22248) = v14 + *(double *)(v2 + 22248);
      }
      else if ( v12 == 4 )
      {
        *(_QWORD *)(v2 + 22328) += v13;
        *(double *)(v2 + 22296) = v14 + *(double *)(v2 + 22296);
        if ( a2 != 0 )
```

basically, look for scond rva that is above != 0 and above if block, then, double click that, in that function scroll till the very end

```c
            do
            {
              if ( v4 >= a2 )
                break;
              v15 = *(_QWORD *)(v2 + 104);
              v16 = *(_QWORD *)(v15 + 8);
              v4 += (int)(16 * sub_2616270(a1, a2: v15)); // <-- or this
              *(_QWORD *)(v2 + 104) = v16;
            }
            while ( v16 != 0 );
          }
          for ( i = *(_QWORD *)(v2 + 1192); i != 0; *(_QWORD *)(v2 + 1192) = i )
          {
            if ( v4 >= a2 )
              break;
            v18 = *(_QWORD *)(v2 + 1192);
            i = *(_QWORD *)(v18 + 8);
            v4 += (int)(16 * sub_2616270(a1, a2: v18)); // <-- double click this
          }
          if ( *(_QWORD *)(v2 + 104) == 0 && i == 0 )
          {
LABEL_33:
            **(_BYTE **)(v2 + 112) = **(_BYTE **)(v2 + 112) & 0xF8 | *(_BYTE *)(v2 + 56) & 3;
            sub_2614940(a1);
            *(_BYTE *)(v2 + 57) = 0;
            if ( byte_8043170 != 0 )
            {
              v19 = *(void (__fastcall **)(_QWORD))(v2 + 1824);
              if ( v19 != nullptr )
                v19(a1: *(_QWORD *)(v2 + 112));
            }
          }
        }
        break;
      default:
        break;
    }
  }
  else
  {
    sub_2615010(a1);
  }
  return v4;
```

function with 2 args above == 0 && i == 0 ) and under >= a2, double click, again, scroll till the end

```c
LABEL_10:
    v10 += v5;
    if ( v10 == v11 )
    {
      LODWORD(v9) = v16;
      LODWORD(v3) = v5;
      return (unsigned int)(((int)v11 - (int)v9) / (int)v3);
    }
  }
  if ( ((*v10 ^ 3) & v14) != 0 )
  {
    *v10 = v13 | *v10 & 0xF8;
    goto LABEL_10;
  }
  sub_26143E0(a1, a2: (__int64)v10, a3: a2);
  if ( --v8 != 0 )
    goto LABEL_10;
  return (unsigned int)(((int)v10 - v16) / (int)v5 + 1);
```

the last rva, double click that (literally last rva sub_26143E0), in that function, scroll till the end, look for case 0xF above case 0x10

```c
      v8 = 112;
      return sub_2645690(a1, a2, a3: v8, a4: *(unsigned __int8 *)(a2 + 2), a5: a3);
    case 0xD:
      v31 = *(_QWORD *)(a2 + 32);
      if ( v31 != 0 )
        sub_26455E0(a1, a2: v31, a3: 16LL * *(unsigned int *)(a2 + 24), a4: *(unsigned __int8 *)(a2 + 2));
      goto LABEL_53;
    case 0xE:
      return result;
    case 0xF:
      return sub_261D6B0(a1, a2, a3); // <-- LUAF FREE PROTO
    case 0x10:
LABEL_53:
      v8 = 40;
      return sub_2645690(a1, a2, a3: v8, a4: *(unsigned __int8 *)(a2 + 2), a5: a3);
    default:
      return (unsigned int)*(unsigned __int8 *)(a2 + 1) - 5;
  }
  while ( v14 != a2 )
  {
    v13 = (__int64 *)(v14 + 8);
    v14 = *(_QWORD *)(v14 + 8);
    if ( v14 == 0 )
      goto LABEL_23;
  }
  *v13 = *(_QWORD *)(v14 + 8);
  --*(_DWORD *)(*(_QWORD *)(a1 + 56) + 8LL);
LABEL_23:
  v15 = *(_WORD *)(a2 + 4) - ((*(_WORD *)(a2 + 4) >> 1) & 0x5555);
  v16 = (unsigned __int16)((v15 & 0x3333) + ((v15 >> 2) & 0x3333));
  if ( (unsigned __int16)((257 * (((unsigned __int16)v16 + (unsigned __int16)(v16 >> 4)) & 0xF0F)) >> 8) < 8u )
    *(_DWORD *)(*(_QWORD *)(a1 + 56) + 1576LL) &= ~0x20000000u;
  v8 = *(_DWORD *)(a2 + 20) + 25;
  return sub_2645690(a1, a2, a3: v8, a4: *(unsigned __int8 *)(a2 + 2), a5: a3);
```

so after all of this, you were able to find luaF_freeproto. Good job, and if you failed to, just dm me idfk

so the offset is 0x261D6B0

<details>
<summary><b>verify</b></summary>

3 args, ypu

```c
__int64 __fastcall sub_25C5110(__int64 a1, __int64 a2, __int64 a3)
{
  __int64 v6; // rcx
  __int64 v7; // rcx
  __int64 v8; // rcx
  __int64 v9; // rdx

  sub_25C93C0(a1, a2: *(_QWORD *)(a2 + 40), a3: 4LL * *(int *)(a2 + 168), a4: *(unsigned __int8 *)(a2 + 2));
  sub_25C93C0(a1, a2: *(_QWORD *)(a2 + 72), a3: 8LL * *(int *)(a2 + 160), a4: *(unsigned __int8 *)(a2 + 2));
  sub_25C93C0(a1, a2: *(_QWORD *)(a2 + 32), a3: 16LL * *(int *)(a2 + 172), a4: *(unsigned __int8 *)(a2 + 2));
  v6 = *(_QWORD *)(a2 + 16);
  if ( a2 + 16 != v6 )
    sub_25C93C0(a1, a2: a2 - v6 + 16, a3: *(int *)(a2 + 164), a4: *(unsigned __int8 *)(a2 + 2));
  sub_25C93C0(a1, a2: a2 + *(_QWORD *)(a2 + 8) + 8LL, a3: 24LL * *(int *)(a2 + 152), a4: *(unsigned __int8 *)(a2 + 2));
  sub_25C93C0(a1, a2: *(_QWORD *)(a2 + 88) ^ (a2 + 88), a3: 8LL * *(int *)(a2 + 144), a4: *(unsigned __int8 *)(a2 + 2));
  v7 = *(_QWORD *)(a2 + 128);
  if ( a2 + 128 != v7 )
    sub_25C93C0(a1, a2: a2 - v7 + 128, a3: *(int *)(a2 + 168), a4: *(unsigned __int8 *)(a2 + 2));
  if ( *(_QWORD *)(a2 + 104) != 0 )
    (*(void (__fastcall **)(__int64, __int64))(*(_QWORD *)(a1 + 24) + 1768LL))(a1, a2);
  v8 = *(_QWORD *)(a2 + 96);
  if ( v8 + a2 + 96 != 0 )
    sub_25C93C0(a1, a2: v8 + a2 + 96, a3: *(int *)(a2 + 140), a4: *(unsigned __int8 *)(a2 + 2));
  v9 = *(_QWORD *)(a2 + 176);
  if ( v9 != 0 )
    sub_25C93C0(a1, a2: v9, a3: 16LL * *(unsigned int *)(a2 + 184), a4: *(unsigned __int8 *)(a2 + 2));
  return sub_25C9470(a1, a2, a3: 216, a4: *(unsigned __int8 *)(a2 + 2), a5: a3);
}
```
g
  
</details>
