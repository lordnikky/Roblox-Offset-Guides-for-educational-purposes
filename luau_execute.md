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

click xrefs until you land on "call" (sorry dont got better way yet)

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
                ((void (__fastcall *)(__int64))sub_277A970)(a1: v5); // <-- luau execute
                if ( byte_7CCA548 != 0 )
                  ((void (__fastcall *)(__int64, __int64))sub_2752A30)(a1: v5, a2: v1081);
                if ( v1080 == 0 )
                  *(_BYTE *)(v5 + 5) = 0;
              }
              v1089 = *(_BYTE *)(v5 + 3);
              v1090 = v1089 == 1 || v1089 == 6 || v1089 == 127;
              if ( v1467 != 0 )
              {
                --*(_WORD *)(v5 + 50);
                if ( v1090 )
                {
                  v1082 = v1409;
                  *(_QWORD *)(v1409 + *(_QWORD *)(v5 + 120)) = *(_QWORD *)(v5 + 80) + v1403 + 48;
LABEL_2291:
                  --*(_WORD *)(v5 + 48);
                  if ( *(_QWORD *)(*(_QWORD *)(v5 + 72) + 64LL) >= *(_QWORD *)(*(_QWORD *)(v5 + 72) + 56LL) )
                  {
                    LOBYTE(v1082) = 1;
                    ((void (__fastcall *)(__int64, unsigned __int64))sub_2764400)(a1: v5, a2: v1082);
                  }
                  v9 = *(_QWORD *)(v5 + 96);
                  v1091 = (_QWORD *)*ii;
                  a2 = v949 + v9;
                  v1327 = v9;
                  *(_QWORD *)(v5 + 88) = *(_QWORD *)*ii;
                  if ( *(_DWORD *)(v949 + v9 + 12) == 0 )
                  {
                    v1091[4] = v1348;
                    ((void (__fastcall __noreturn *)(__int64, __int64, const char *))sub_27730C0)(
                      a1: v5,
                      a2,
                      a3: "call"); // <-- you're here 
```

fuck this shit
