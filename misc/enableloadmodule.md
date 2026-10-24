# EnableLoadModule

search for string `EnableLoadModule`, second xref:

```c
__int64 sub_425C270()
{
  __int64 v0; // rbx
  __int64 v1; // rdi
  _QWORD v3[3]; // [rsp+30h] [rbp-28h] BYREF
  char v4; // [rsp+48h] [rbp-10h]

  v0 = qword_8C86398;
  v1 = qword_8C86398 + 64;
  v3[2] = qword_8C86398 + 64;
  v4 = 1;
  sub_89F0(a1: qword_8C86398 + 64, a2: 0);
  v3[0] = "EnableLoadModule";
  v3[1] = 16;
  sub_49FE870(a1: v0, a2: v3, a3: &byte_888F650, a4: 1);
  return sub_8B30(a1: v1);
}
```

byte (or unk) as 3rd arg will be the offset, so 0x888F650 is the offset
