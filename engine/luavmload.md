# LuaVMLoad

search for string `bytecode corrupted`, decompile it and go to the very top

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

sig: 40 53 56 57 41 54 41 55 41 56 41 57 48 81 EC 40 01 00 00 48 8B 05 ? ? ? ? 48 33 C4 48 89 84 24 ? ? ? ? 45 8B E1

<details>

<summary><b>verify:</b></summary>

whole function should be about ~1.8k-2k lines takes 2 args should have stack overflow and right after not enough memory:

```c
        }
        if ( (unsigned __int64)(*(_QWORD *)(a1 + 32) + 16LL) > *(_QWORD *)(*(_QWORD *)(a1 + 8) + 8LL)
          && (unsigned int)sub_2587960(a1, a2: 1) == 0 )
        {
          sub_25C3410(a1, a2: "stack overflow");
          sub_258B520(a1);
        }
        v205 = *(_QWORD **)(a1 + 32);
        v18 = v13;
        v19 = "not enough memory";
        v20 = 0;
```

about 7 stack overflows in function
  
</details>
