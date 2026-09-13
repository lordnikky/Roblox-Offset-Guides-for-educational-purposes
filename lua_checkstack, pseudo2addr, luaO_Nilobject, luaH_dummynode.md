# LuaO_NilObject

# LuaH_DummyNode

# pseudo2addr

# lua_checkstack

these can be found via string "Attempt to migrate WeakObjectRef across VM boundary", first xref, decompile:

```armasm
__int64 __fastcall sub_41812B0(__int64 a1, __int64 a2)
{
  __int64 result; // rax
  int v5; // esi
  __int64 v6; // rdx
  __int64 v7; // rax
  __int64 v8; // rcx
  double *i; // r8
  char *v10; // r10
  double v11; // xmm1_8
  __int64 v12; // rcx

  if ( (unsigned __int8)sub_E22AD0(a1) != 0 )
  {
    if ( (unsigned __int64)(*(_QWORD *)(a2 + 40) + 16LL) <= *(_QWORD *)(*(_QWORD *)(a2 + 16) + 16LL)
      || (unsigned int)sub_26F7B00(a1: a2, a2: 1) != 0 ) ; <-- lua_checkstack
    {
      result = *(_QWORD *)(a2 + 40);
      *(_DWORD *)(result + 12) = 0;
      goto LABEL_20;
    }
LABEL_22:
    sub_2722360(a1: a2, a2: "stack overflow");
    sub_26FA450(a1: a2);
  }
  if ( *(_QWORD *)(*(_QWORD *)(sub_33FC1E0(a1) + 24) + 800LL) != *(_QWORD *)(*(_QWORD *)(a2 + 24) + 800LL) )
    sub_4924110(a1: "Attempt to migrate WeakObjectRef across VM boundary");
  v5 = sub_417FAE0(a1);
  if ( (*(_BYTE *)a2 & 4) != 0 )
  {
    v6 = *(_QWORD *)(a2 + 24);
    *(_BYTE *)a2 &= ~4u;
    *(_QWORD *)(a2 + 112) = *(_QWORD *)(v6 + 48);
    *(_QWORD *)(v6 + 48) = a2;
  }
  if ( (unsigned __int64)(*(_QWORD *)(a2 + 40) + 16LL) > *(_QWORD *)(*(_QWORD *)(a2 + 16) + 16LL)
    && (unsigned int)sub_26F7B00(a1: a2, a2: 1) == 0 ) - // <-- lua_checkstack
  {
    goto LABEL_22;
  }
  v7 = sub_26F7960(a1: a2, a2: 4294957296LL); // <-- pseudo2addr
  v8 = *(_QWORD *)v7;
  if ( (unsigned int)(v5 - 1) >= *(_DWORD *)(*(_QWORD *)v7 + 8LL) )
  {
    v10 = *(char **)(v8 + 40);
    if ( v10 == (char *)&unk_63CAB08 ) <-- luaH_Dummynode
    {
LABEL_18:
      i = (double *)&unk_63CDF48; // <-- LuaO_nilobject
    }
    else
    {
      v11 = (double)v5;
      for ( i = (double *)&v10[32
                             * ((int)(1540483477
                                    * ((1540483477
                                      * (HIDWORD(v11)
                                       & 0x7FFFFFFF
                                       ^ ((1540483477 * (LODWORD(v11) ^ ((HIDWORD(v11) & 0x7FFFFFFFu) >> 18))) >> 22)))
                                     ^ ((1540483477
                                       * ((1540483477 * (LODWORD(v11) ^ ((HIDWORD(v11) & 0x7FFFFFFFu) >> 18)))
                                        ^ ((1540483477
                                          * (HIDWORD(v11)
                                           & 0x7FFFFFFF
                                           ^ ((1540483477 * (LODWORD(v11) ^ ((HIDWORD(v11) & 0x7FFFFFFFu) >> 18))) >> 22))) >> 17))) >> 19)))
                              & (unsigned __int64)((1 << *(_BYTE *)(v8 + 7)) - 1))]; ; i += 4 * (v12 >> 4) )
      {
        v12 = *((int *)i + 7);
        if ( (*((_BYTE *)i + 28) & 0xF) == 3 && i[2] == v11 )
          break;
        if ( (v12 & 0xFFFFFFF0) == 0 )
          goto LABEL_18;
      }
    }
  }
  else
  {
    i = (double *)(*(_QWORD *)(v8 + 24) + 16LL * (v5 - 1));
  }
  result = *(_QWORD *)(a2 + 40);
  *(_OWORD *)result = *(_OWORD *)i;
LABEL_20:
  *(_QWORD *)(a2 + 40) += 16LL;
  return result;
}
```

so the offsets are

lua_checkstack 0x26F7B00
pseudo2addr 0x26f7960
LuaO_NilObject 0x63CDF48
LuaH_DummyNode 0x63CAB08
