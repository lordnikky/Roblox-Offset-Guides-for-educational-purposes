# OpcodeLookUpTable

string `bytecode corrupted` first xref

decompile it, copy over in notepad and ctrl f for `& 0xFFFFFF00`

```c
              do
              {
                v149 = *v148 & 0xFFFFFF00 | byte_71CFBA0[(unsigned __int8)*v148]; // <-- here
                *v148 = v149;
                v148 += (int)sub_265AB70(a1: byte_71D0CF0[(unsigned __int8)v149]);
              }
              while ( (unsigned __int64)v148 < *(_QWORD *)(v126 + 136) + 4LL * *(int *)(v126 + 184) );
              v148 = *(unsigned int **)(v126 + 136);
            }
```

that byte (or wtv it is) is the opcodelookuptable 0x71CFBA0
