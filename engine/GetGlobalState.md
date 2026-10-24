# GetGlobalState

string `The schema may only be set once.`, first xref, decompile and scroll up until you see string `Invalid Facet Access`
```c
  *(_DWORD *)(a1 + 160) = 1;
  v12 = *(_DWORD *)(a3 + 5448);
  if ( v12 >= 3 )
  {
    __wind
    {
      sub_4AA5F60(a1: 0, a2: (__int64)"Invalid Facet Access"); // <-- scroll until this
    }
    __unwind
    {
      sub_4AA5ED0();
    }
  }
  __eh34_enter_wind_state(0, 6);
  try
  {
    __wind
    {
      __wind
      {
        v13 = a3 + 2440;
        v75 = 0;
        v74 = &RBX::Lua::WeakThreadRef::`vftable';
        v76 = 0;
        v78 = (__m128i *)v93;
        v84 = 0;
        v93[24] = 0;
        v14 = (__int64 *)(*(__int64 (__fastcall **)(__int64, _QWORD *))(*(_QWORD *)*a5 + 176LL))(a1: *a5, a2: v99);
        v15 = (__int64)v14;
        if ( (unsigned __int64)v14[3] >= 0x10 )
          v15 = *v14;
        __wind
        {
          v16 = sub_425E0F0(a1: v73);
        }
        __unwind
        {
          sub_7691D0(a1: v99);
        }
      }
      __unwind
      {
        sub_425C570(a1: v78);
      }
      __wind
      {
        v90 = v16;
        v91 = 0;
        v92 = 0;
        v17 = sub_430D730( // <-- this has to be double clicked
                a1: v13,
                a2: (__int64)&v80,
                a3: (__int64)&v90,
                a4,
                a5: v15,
                a6,
                a7: (__int64)&v84,
                a8: (__int64)v93);
        sub_4222FB0(a1: &v74, a2: v17);
        v80 = &RBX::Lua::WeakThreadRef::`vftable'; // <-- look down until SECOND weakthreadref
        v18 = v82;
        if ( v82 != 0 )
        {
          v19 = *(_DWORD *)(v82 + 8);
```

you saw the comments, double click that rva and in that function scroll down until you see invalid facet access, first one

```c
          v99 = -408;
        if ( *(int *)(v99 + 5448) >= 3 )
        {
          __wind
          {
            sub_4AA5F60(a1: 0, a2: (__int64)"Invalid Facet Access"); // <-- search for this
          }
          __unwind
          {
            sub_4AA5ED0();
          }
        }
        v15 = sub_425F7A0(a1: v99); // <-- getglobalstate
        v228 = 0;
        v100 = v212;
        if ( *(_BYTE *)(v212 + 24) != 0 )
```





<details>
<summary><b>click this if you're unsure that rva you got is correct </b></summary>

getglobalstate takes only 1 arg and returns global state:
```c
v15 = sub_425F7A0(a1: v99);

and

__int64 __fastcall sub_425F7A0(__int64 a1)
```

and to actually verify that function is correct decompile it and it should be like 21 lines with >=3 facet check:

```c
__int64 __fastcall sub_425F7A0(__int64 a1)
{
  __int64 v1; // rax
  __int64 v3; // [rsp+20h] [rbp-18h]

  if ( *(int *)(a1 + 5448) >= 3 )
  {
    __wind
    {
      ((void (__noreturn *)(void))sub_4AA5F60)();
    }
    __unwind
    {
      sub_4AA5ED0();
    }
  }
  v1 = sub_42DD7C0(a1: a1 + 424) + 24;
  LODWORD(v3) = *(_DWORD *)v1 ^ v1;
  HIDWORD(v3) = *(_DWORD *)(v1 + 4) ^ v1;
  return v3;
}
```

</details>
