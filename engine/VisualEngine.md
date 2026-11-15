**Made by goodknigh1 (1067852356953329795), thanks a lot for contributing to community!**

# VisualEnginePointer

string `"AutoCapture_{}_Frames-{}-{}.raw"`, and go to the first xref
Then f5 to decompile an it should look like this

```c
    if ( v46 != *(_QWORD *)(v45 + 8) )
    {
      sub_2F67210(a1: v45);
      *(_QWORD *)(v45 + 8) = v46;
    }
    v47 = (_QWORD *)(v45 + 16);
    ++*(_QWORD *)(v45 + 16);
    byte_8A117F0 = 1;                  // <--- right here
    v48 = __rdtsc() - qword_8E542B8;
    v49 = *((_DWORD *)off_82C1F18 + 411940);
    v50 = (_QWORD *)sub_2A5B320();
    v108.m128i_i64[0] = (__int64)"AutoCapture_{}_Frames-{}-{}.raw";
    v108.m128i_i64[1] = 31;
    v51 = v50;
    if ( v50[3] >= 0x10u )
      v51 = (_QWORD *)*v50;
```
You wanna look for the first byte above the string 

now take that byte's rva (8A117F0 in this example) and you add 18 (hexidecimal) 
and there is your VisualEnginePointer (0x8a11808 in this example)
