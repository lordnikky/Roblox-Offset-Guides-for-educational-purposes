stuff used in bytecode signing or something, dont really know lol

# native::destroystring

string "doNotFallbackToBaselineRepresentation" first xref decompile and scroll to the very end

```c
  LOBYTE(v86[0]) = 0;
  if ( v30 >= 0x10 )
    sub_73B1D0(a1: v28, a2: v28[0], a3: v30 + 1);
  v29 = 0;
  v30 = 15;
  LOBYTE(v28[0]) = 0;
  sub_73AD10(a1: v103);
  sub_73AD10(a1: v92);
  sub_73AD10(a1: v106);
  sub_73AD10(a1: v101);
  sub_73AD10(a1: v97);
  sub_73AD10(a1: v58);
  sub_73AD10(a1: v99);
  sub_73AD10(a1: (__int64 *)Src);
  sub_73AD10(a1: v89);
  sub_73AD10(a1: (__int64 *)&v55);
  sub_73AD10(a1: v91);
  sub_73AD10(a1: (__int64 *)&v93);
  return atexit(a1: sub_62AF9E0);
}
```

yeah these 12 of same rva's are the native:destroystring

# native::verify

string `"%s: bytecode type version mismatch (expected [%d..%d], got %d)"` first xref

```c
        ++v15;
      while ( v7[v15] != 0 );
      v16 = (const char *)sub_2657740(Destination: v1554);
      result = sub_261AD70(
                 a1: v3,
                 a2: "%s: bytecode type version mismatch (expected [%d..%d], got %d)",
                 v16,
                 1,
                 3,
                 v1558);
      goto LABEL_2377;
    }
  }
  if ( (unsigned int)sub_4254A10(a1: v3, a2: (_DWORD)v7, a3: (_DWORD)v6, a4: v5, a5: v4) != 1 )
  {
    if ( v4 != 0 )
      v19 = (__int64 *)sub_2619850(a1: v3, a2: v4);
    else
      v19 = (__int64 *)(v3 + 128);
    v1395 = *v19;
    v1398 = -1;
    v20 = -1;
```

first sub after string (one with != 1) double click that, here you'll see:

```c
  _QWORD v28[3]; // [rsp+38h] [rbp-90h] BYREF
  int v29; // [rsp+50h] [rbp-78h]
  unsigned int v30[2]; // [rsp+58h] [rbp-70h] BYREF
  __int64 v31; // [rsp+60h] [rbp-68h]
  __m128i v32; // [rsp+70h] [rbp-58h]

  __wind
  {
    v28[0] = a2;
    v28[1] = a3;
    v28[2] = a4;
    v29 = a5;
    v30[0] = 0xFFFFFFFF;
    v6 = 0;
    v30[1] = 0;
    v31 = 0;
    v32 = *(__m128i *)&xmmword_740DD00;
    sub_4254D80();
    v8 = (int)sub_4255600(a1: v7, a2: (__int64)v28, a3: v30); // <-- this is the offset 
    sub_4254D80();
    v9 = dword_72A3948[byte_72A3938[byte_72A3928[v8]] % 0xAuLL] / 7u - 157;
    sub_4254D80();
    if ( v9 / 0xA9 != 13 * (v9 / 0xA9 / 0xD) )
      *(_DWORD *)(*(_QWORD *)(a1 + 80) + 1584LL) &= ~0x40000000u;
    if ( (unsigned int)v8 > 1 || v9 / 0xD != 13 * (v9 / 0xD / 0xD) )
    {
      sub_4254D80();
      v10 = 0;
      v11 = 0;
```

so the offset will be 3rd in the function


# native::key

so inside of native::verify theres a single unk_ in the whole function

```c
            *v20 = a0123456789abcd[(unsigned __int64)v22 >> 4];
            v20[1] = a0123456789abcd[v22 & 0xF];
            v20 += 2;
          }
          sub_7390E0(a1: a3 + 2, a2: Src, a3: "0123456789abcdef"); // <-- this can be the anchor 
        }
        __unwind
        {
          if ( (v40 & 2) != 0 )
          {
            v40 &= ~2u;
            sub_7390D0(a1: Src);
          }
        }
        __eh34_enter_wind_state(-1, 1);
        if ( v44 >= 0x10 )
        {
          v23 = Src[0];
          if ( v44 + 1 >= 0x1000 )
          {
            v23 = *(_QWORD *)(Src[0] - 8LL);
            if ( (unsigned __int64)(Src[0] - v23 - 8) > 0x1F )
              goto LABEL_63;
          }
          sub_49C4410(a1: v23);
        }
        if ( (int)*a3 > 0 )
        {
          v24 = 0;
          v25 = &unk_65D2A5C;    // <-- here!!!
          do
          {
            if ( a3[1] == *v25 )
              goto LABEL_79;
            ++v24;
            ++v25;
          }
          while ( v24 == 0 );
          LOBYTE(v5) = 1;
          result = (unsigned int)(v5 + 8);
```
