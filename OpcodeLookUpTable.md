# OpcodeLookUpTable

string "iterate over" (same as luau_execute), ignore .text segments and go to xref

```asm
Up    o    sub_2736E10+B9E3    lea     rax, aIterateOver; "iterate over"
Up    o    sub_2736E10+BCFA    lea     rax, aIterateOver; "iterate over"
Up    o    sub_2736E10+BDA4    lea     rax, aIterateOver; "iterate over"
Up    o    sub_2736E10+BDD0    lea     rax, aIterateOver; "iterate over"
Up    o    sub_2736E10+BDFC    lea     rax, aIterateOver; "iterate over"
```

decompile it, its 10 thousand lines so it will take a while, after its done, copy over the code to notepad and ctrl f search for  `"(unsigned __int8 *)sub"`

every possibility:

```c
        v50 = (unsigned __int8 *)sub_2722610(a1: &unk_6E26C70, a2: 188);
        v51 = (unsigned __int8 *)sub_2722610(a1: &unk_6E26C70, a2: v28);
            nn = *(unsigned __int8 *)sub_2722610(a1: &unk_6E26C70, a2: 124);
        v39 = (unsigned __int8 *)sub_2722610(a1: &unk_6E26C70, a2: 48);
            if ( *(v1212 - 8) == *(unsigned __int8 *)sub_2722610(a1: &unk_6E26C70, a2: 153) )
        v27 = (unsigned __int8 *)sub_2722610(a1: &unk_6E26C70, a2: 77);
```

That &unk_ is the OpcodeLookUpTable