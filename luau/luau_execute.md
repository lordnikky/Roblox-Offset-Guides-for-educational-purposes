# luau_execute

search for string "iterate over"

```asm
.rdata:0000000006E275A8 aIterateOver    db 'iterate over',0     ; DATA XREF: .text:000000000273662D↑o
.rdata:0000000006E275A8                                         ; .text:00000000027368FA↑o ...
```

first xref decompile, it is a BIG function and will take a while if you're on older hardware, decompile it and go to very top, press x on first line's sub

```c
__int64 __fastcall sub_265FAB0(__int64 a1, __int64 a2)
```

<img width="836" height="631" alt="image" src="https://github.com/user-attachments/assets/4b90fc17-0134-418b-a047-5f2e82ccab97" />

You will see this, there's one that stands out, that is the luau_execute


<details>

<summary><b>click to verify</b></summary>

```c
__int64 __fastcall sub_265F2B0(__int64 a1, __int64 a2, __int64 i29)
{
  if ( *(_BYTE *)(a1 + 4) != 0 )
    return sub_265FAB0(a1, a2);
  else
    return sub_266D720(a1, a2, i29);
}
```

whole funcction is small, takes 2 args

</details>
