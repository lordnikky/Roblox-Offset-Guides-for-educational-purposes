# luau_execute

search for string "iterate over"

```asm
.rdata:0000000006E275A8 aIterateOver    db 'iterate over',0     ; DATA XREF: .text:000000000273662D↑o
.rdata:0000000006E275A8                                         ; .text:00000000027368FA↑o ...
```

press shift x on the xref:

```asm
Direction	Type	Address	Text
Up	o	.text:000000000273662D	lea     rax, aIterateOver; "iterate over"
Up	o	.text:00000000027368FA	lea     rax, aIterateOver; "iterate over"
Up	o	.text:00000000027369A4	lea     rax, aIterateOver; "iterate over"
Up	o	.text:00000000027369D0	lea     rax, aIterateOver; "iterate over"
Up	o	.text:00000000027369FC	lea     rax, aIterateOver; "iterate over"
Up	o	sub_2736E10+B9E3	lea     rax, aIterateOver; "iterate over"
Up	o	sub_2736E10+BCFA	lea     rax, aIterateOver; "iterate over"
Up	o	sub_2736E10+BDA4	lea     rax, aIterateOver; "iterate over"
Up	o	sub_2736E10+BDD0	lea     rax, aIterateOver; "iterate over"
Up	o	sub_2736E10+BDFC	lea     rax, aIterateOver; "iterate over"
```

so, the sub_2736E10 technically is the luau_execute, thats what luau_execute calls to well execute stuff, but you dont wanna that, you want this

well okay, after half an hour of trying to find best approach i failed, here's mid:

luau_execute_body, thing that luau execute calls as can be seen here:

do as said earlier (iterate over) and sub_2736E10 is the luau_execute_body, to find the luau_execute you gotta decompile the luau_execute_body which is ~10k lines so, thats why i tried to find better way. so, best way i found is dumb as shit but it seems to work, lol

search for string "attempt to %s a %s value"

```asm
.rdata:0000000006E26AB8 aAttemptToSASVa db 'attempt to %s a %s value',0
.rdata:0000000006E26AB8                                         ; DATA XREF: sub_2722A00+15↑o
```

first xref, decompile it

```c
void __fastcall __noreturn sub_2722A00(__int64 a1, __int64 a2, const char *a3)
```

click sub_2722A00 and press x, 16th xref:

```asm
Down	p	sub_2736E10+BCE7	call    sub_2722A00
```

double click, you'll land here

```c
                                sub_2722A00(a1: v5, a2, a3: "call");
```

look up like 26 lines:

```c
                            sub_272A260(a1: v5);
```

THATS the fucking luau_execute, whole code batch:

```c
                            sub_272A260(a1: v5); // <-- your  tagret!!!!!
                            if ( byte_7C51308 != 0 )
                              sub_270BE30(a1: v5, a2: v905);
                            if ( v904 == 0 )
                              *(_BYTE *)(v5 + 5) = 0;
                          }
                          v913 = *(_BYTE *)(v5 + 3);
                          v914 = v913 == 1 || v913 == 6 || v913 == 127;
                          if ( v1356 != 0 )
                          {
                            --*(_WORD *)(v5 + 90);
                            if ( v914 )
                            {
                              *(_QWORD *)(*(_QWORD *)(v5 + 72) + v1310 + 16) = (char *)v1309 + *(_QWORD *)(v5 + 48) + 48;
LABEL_1949:
                              --*(_WORD *)(v5 + 88);
                              if ( *(_QWORD *)(*(_QWORD *)(v5 + 24) + 88LL) >= *(_QWORD *)(*(_QWORD *)(v5 + 24) + 80LL) )
                                sub_2719020(a1: v5, a2: 1);
                              v9 = *(_QWORD *)(v5 + 32);
                              nn = *ii;
                              a2 = v845 + v9;
                              v1198 = v9;
                              *(_QWORD *)(v5 + 40) = *(_QWORD *)(*ii + 16);
                              if ( *(_DWORD *)(v845 + v9 + 12) == 0 )
                              {
                                *(_QWORD *)(nn + 32) = v1224;
                                sub_2722A00(a1: v5, a2, a3: "call"); // <-- land here
```

fuck this shit
