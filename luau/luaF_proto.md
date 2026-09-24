heyy i finally found good string anchor, even tho its a bit of a pain cuz decompiling 8k lines of code thats the best one i could find :/

# luaF_FreeProto

search for string "Failed to create Lua state", first xref, decompile:

```c
  if ( a4 == 0 )
    v8 = dword_85C4D88;
  *v7 = v8;
  v9 = sub_2662670(a1: sub_427CD10);
  v983 = v9;
  if ( v9 == 0 )
    sub_4960E00(a1: "Failed to create Lua state"); // <-- you're here
  if ( byte_7D64880 == 0 ) // <-- double click this
    goto LABEL_22;
  v10 = (_QWORD *)sub_4943800(a1: 0x58u);
  if ( v10 == nullptr )
  {
    sub_7BADF0(a1: v1093);
    throw (std::bad_alloc *)v1093;
```

double click the thing under the string:

```asm
.data:0000000007D64880 byte_7D64880    db 0                    ; DATA XREF: sub_604660+E↑o
.data:0000000007D64880                                         ; sub_26822A0:loc_26825AA↑r ...
```

second xref, decompile, scroll to the end:

```c
        v8 = v30 + 8;
        return sub_269C8B0(a1, (_DWORD)a2, a3: v8, a4: a2[2], a5: a3);
      }
    case 0xCu:
      v31 = *((_QWORD *)a2 + 4);
      if ( v31 != 0 )
        sub_269C800(a1, a2: v31, a3: 16LL * (unsigned int)(*((_DWORD *)a2 + 19) - *((_DWORD *)a2 + 18)), a4: a2[2]);
      v32 = *((_QWORD *)a2 + 6);
      if ( v32 != 0 )
        sub_269C800(a1, a2: v32, a3: 8LL * *((unsigned int *)a2 + 19), a4: a2[2]);
      v8 = 88;
      return sub_269C8B0(a1, (_DWORD)a2, a3: v8, a4: a2[2], a5: a3);
    case 0xDu:
      sub_269C800(a1, a2: *((_QWORD *)a2 + 4), a3: 16LL * *((unsigned int *)a2 + 6), a4: a2[2]);
      goto LABEL_60;
    case 0xFu:
      return sub_2698550(a1, (__int64)a2, a3); // <-- luaF_FreeProto
    case 0x10u:
LABEL_60:
      v8 = 40;
      return sub_269C8B0(a1, (_DWORD)a2, a3: v8, a4: a2[2], a5: a3);
    default:
      return (unsigned int)*a2 - 5;
  }
  while ( (unsigned __int8 *)v14 != a2 )
  {
    v13 = (__int64 *)(v14 + 8);
    v14 = *(_QWORD *)(v14 + 8);
    if ( v14 == 0 )
      goto LABEL_24;
  }
  *v13 = *(_QWORD *)(v14 + 8);
  --*(_DWORD *)(*(_QWORD *)(a1 + 24) + 28LL);
LABEL_24:
  v15 = *((_WORD *)a2 + 2) - ((*((_WORD *)a2 + 2) >> 1) & 0x5555);
  v16 = (unsigned __int16)((v15 & 0x3333) + ((v15 >> 2) & 0x3333));
  if ( (unsigned __int16)((257 * (((unsigned __int16)v16 + (unsigned __int16)(v16 >> 4)) & 0xF0F)) >> 8) < 8u )
    *(_DWORD *)(*(_QWORD *)(a1 + 24) + 1584LL) &= ~0x20000000u;
  v8 = *((_DWORD *)a2 + 5) + 25;
  return sub_269C8B0(a1, (_DWORD)a2, a3: v8, a4: a2[2], a5: a3);
}
```

you dont need to scroll, when u decompile the code that string will be the last string ull see on your monitor (unless you have like big ass monitor idfk)
