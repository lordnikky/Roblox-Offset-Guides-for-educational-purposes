# GetGlobalState

string `The schema may only be set once.`, first xref, decompile and scroll up until you see second string `Invalid Facet Access`
```c
    *(_QWORD *)&v78 = 21;
    *((_QWORD *)&v78 + 1) = 31;
    strcpy(v12, "ScriptContext is null");
    *(_QWORD *)&v77 = v12;
    *(_DWORD *)a2 = 1;
    *(_OWORD *)(a2 + 8) = v77;
    *(_OWORD *)(a2 + 24) = v78;
    *(__m128i *)(a2 + 40) = v79;
    return a2;
  }
  *(_DWORD *)(a1 + 160) = 1;
  if ( *(int *)(a3 + 5712) >= 3 )
    sub_4B4F960(a1: 0, a2: "Invalid Facet Access"); // <-- stop when u see this
  v61 = 0;
  v60 = &RBX::Lua::WeakThreadRef::`vftable';
  v62 = 0;
  v58 = (__m128i *)v74;
  v64 = 0;
  v74[24] = 0;
  v13 = (_QWORD *)(*(__int64 (__fastcall **)(_QWORD, _QWORD *))(*(_QWORD *)*a5 + 176LL))(a1: *a5, a2: v80);
  v14 = v13;
  if ( v13[3] >= 0x10u )
    v14 = (_QWORD *)*v13;
  v72 = sub_42D27D0(a1: a3); 
  v73 = 0;
  v15 = sub_4386EF0(a1: a3 + 2648, a2: v65, a3: &v72, a4, a5: v14, a6, a7: &v64, a8: v74, a9: 0); // <-- double click this
  sub_428D8B0(a1: &v60, a2: v15);
  v65[0] = &RBX::Lua::WeakThreadRef::`vftable'; // <-- look down for this
  v16 = sub_428D1C0(a1: v65);
  if ( v16 != 0 )
  {
```

you saw the comments, double click that rva and in that function scroll down until you see invalid facet access, first one

```c
  v97 = a1 - 2648;
  if ( v10 == 0 )
    v97 = -376;
  if ( *(int *)(v97 + 5712) >= 3 )
    sub_4B4F960(a1: 0, a2: (__int64)"Invalid Facet Access");
  v13 = sub_42D3B20(a1: v97, a2: a3, a3: a6); // <-- getglobalstate
  v286 = 0;
  v98 = v274;
  if ( *(_BYTE *)(v274 + 24) != 0 )
  {
    qmemcpy(v285, (const void *)v274, sizeof(v285));
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
