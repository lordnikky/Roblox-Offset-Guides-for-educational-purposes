# luaC_init

search for string "InvalidInstance", second xref and decompile:

go to the very bottom

```c
  }
  else
  {
    v10 = (__int64 *)(v9 + 464 + 8LL * byte_7C50E50);
    v11 = *v10;
    if ( *v10 == 0 )
      v11 = sub_2728C80(a1, a2: v9 + 464, a3: v9 + 792); // <-- luaC_init
    v12 = *(int *)(v11 + 48);
    if ( (int)v12 < 0 )
    {
      v13 = *(_DWORD **)(v11 + 40);
      *(_QWORD *)(v11 + 40) = *((_QWORD *)v13 + 1);
    }
    else
    {
      v13 = (_DWORD *)(v12 + v11 + 64);
      LODWORD(v12) = v12 - *(_DWORD *)(v11 + 36);
      *(_DWORD *)(v11 + 48) = v12;
    }
    ++*(_DWORD *)(v11 + 52);
    if ( *(_QWORD *)(v11 + 40) == 0 && (int)v12 < 0 )
    {
      *v10 = *(_QWORD *)(v11 + 24);
      v14 = *(_QWORD *)(v11 + 24);
      if ( v14 != 0 )
        *(_QWORD *)(v14 + 16) = 0;
      *(_QWORD *)(v11 + 24) = 0;
    }
  }
  if ( v13 == nullptr )
    goto LABEL_133;
  *(_QWORD *)(v9 + 88) += 48LL;
  *(_QWORD *)(v9 + 8 * v8 + 11696) += 48LL;
  v16 = *(void (__fastcall **)(__int64, _DWORD *, _QWORD, __int64, int, int, _DWORD))(v9 + 1672);
  if ( v16 != nullptr )
  {
    LOBYTE(v75) = v8;
    v16(a1, a2: v13, a3: 0, a4: 48, a5: v75, a6: 7, a7: 0);
  }
  *(_BYTE *)v13 = *(_BYTE *)(*(_QWORD *)(a1 + 24) + 72LL) & 3;
  *((_BYTE *)v13 + 2) = 7;
  *((_BYTE *)v13 + 1) = *(_BYTE *)(a1 + 4);
  *((_QWORD *)v13 + 2) = 0;
  *(_WORD *)((char *)v13 + 3) = 255;
  *((_QWORD *)v13 + 3) = 0;
  *((_QWORD *)v13 + 1) = 0;
  *((_WORD *)v13 + 3) = 0;
  *((_BYTE *)v13 + 5) = 0;
  *((_QWORD *)v13 + 5) = &unk_63CAB08;
  *(_QWORD *)v7 = v13;
  *(_DWORD *)(v7 + 12) = 7;
  *(_QWORD *)(a1 + 40) += 16LL;
  return 1;
}
```
so the offset is 0x2728C80
