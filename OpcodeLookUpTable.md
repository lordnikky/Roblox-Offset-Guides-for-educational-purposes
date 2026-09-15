# OpcodeLookUpTable

string "iterate over" (same as luau_execute), ignore .text segments and go to xref

```asm
Up    o    sub_2736E10+B9E3    lea     rax, aIterateOver; "iterate over"
Up    o    sub_2736E10+BCFA    lea     rax, aIterateOver; "iterate over"
Up    o    sub_2736E10+BDA4    lea     rax, aIterateOver; "iterate over"
Up    o    sub_2736E10+BDD0    lea     rax, aIterateOver; "iterate over"
Up    o    sub_2736E10+BDFC    lea     rax, aIterateOver; "iterate over"
```

decompile it, its 10 thousand lines so it will take a while, after its done, copy over the code to notepad and ctrl f search for  `a1: &unk_`

every possibility:

```c
          v52 = (unsigned __int8 *)((__int64 (__fastcall *)(void *, __int64, signed __int64, __int16 *))sub_2772CD0)(
                                     a1: &unk_6E964D0,
          v53 = (unsigned __int8 *)((__int64 (__fastcall *)(void *, __int64))sub_2772CD0)(a1: &unk_6E964D0, a2: v29);
          v5 = v1454;
          v63 = (_BYTE *)((__int64 (__fastcall *)(void *, __int64, signed __int64, __int16 *))sub_2772CD0)(
                           a1: &unk_6E964D0,
          result = ((__int64 (__fastcall *)(void *, __int64))sub_2772CD0)(a1: &unk_6E964D0, a2: 95);
          if ( *((unsigned __int8 *)v21 - 8) == *(unsigned __int8 *)result )
            if ( *(v1340 - 8) == *(unsigned __int8 *)((__int64 (__fastcall *)(void *, __int64))sub_2772CD0)(
                                                       a1: &unk_6E964D0,
        *((_DWORD *)v33 - 2) = *(unsigned __int8 *)((__int64 (__fastcall *)(void *, __int64, _OWORD *, unsigned __int64))sub_2772CD0)(
                                                     a1: &unk_6E964D0,
        v41 = (unsigned __int8 *)((__int64 (__fastcall *)(void *, __int64))sub_2772CD0)(a1: &unk_6E964D0, a2: 48);
            if ( *((unsigned __int8 *)v1339 - 8) == *(unsigned __int8 *)((__int64 (__fastcall *)(void *, __int64))sub_2772CD0)(
                                                                          a1: &unk_6E964D0,
                                                                          a2: 153) )

```

That &unk_ is the OpcodeLookUpTable
