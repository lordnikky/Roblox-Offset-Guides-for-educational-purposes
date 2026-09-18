# LuaVMLoad

loads the fucking bytecode its in the name

search for string "bytecode corrupted", decompile it and go to the very top

```c
__int64 __fastcall sub_27AC890(__int64 a1, __int64 a2)
```

click on sub_27582C0 once, press x and second, there will be a number of same xrefs in a row, thats the luavmload

```asm
Down	o	sub_4210750+90	lea     rdx, sub_27AC890
Down	o	sub_4211130+197	lea     rdx, sub_27AC890
Down	o	sub_4211130+90F	lea     rdx, sub_27AC890
Down	o	sub_4211130+1166	lea     rdx, sub_27AC890
Down	o	sub_4211130+18F3	lea     rdx, sub_27AC890
Down	o	.rdata:000000000617D34E	dd rva sub_27AC890
```

so the offset is 0x4211130