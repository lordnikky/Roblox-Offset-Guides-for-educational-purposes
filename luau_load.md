# luau_load

loads the fucking bytecode its in the name

search for string "bytecode corrupted", decompile it and go to the very top

```c
__int64 __fastcall sub_27582C0(__int64 a1, __int64 a2)
```

click on sub_27582C0 once, press x and second, third, forth and idk there will be 4 xrefs that are the same, thats luau_load:

```asm
Down	o	sub_41B3B50+197	lea     rdx, sub_27582C0
Down	o	sub_41B3B50+8FF	lea     rdx, sub_27582C0
Down	o	sub_41B3B50+1156	lea     rdx, sub_27582C0
Down	o	sub_41B3B50+18E3	lea     rdx, sub_27582C0
```

also can be found by searching string "stack overflow" and searching for 8 rva's that are the same in a row, it should be either somewhere at ~200 or ~400, god knows, but 8 in a row so uhh yeah
