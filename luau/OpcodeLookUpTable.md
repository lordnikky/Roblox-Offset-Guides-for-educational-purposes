# OpcodeLookUpTable

string "bytecode corrupted" first xref

decompile it, copy over in notepad and ctrl f for "switch ( byte" or "switch ( qword" or "switch ( unk" wtv 

```c
        {
          v153 = *v152 & 0xFFFFFF00 | byte_71433E0[(unsigned __int8)*v152];
          *v152 = v153;
          switch ( byte_7144260[(unsigned __int8)v153] )
          {
            case 7:
            case 8:

```

that byte is the opcodelookuptable 0x7144260
