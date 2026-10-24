# flogdatabank

string "WindowsThemeInit", first xref decompile

```c
__int64 sub_759560()
{
  __int64 v0; // rdi
  __int64 v1; // rcx
  __int64 result; // rax
  __int64 v3; // [rsp+40h] [rbp-18h] BYREF
  char v4; // [rsp+48h] [rbp-10h]

  v0 = qword_8E1B0D0 + 64;
  v3 = qword_8E1B0D0 + 64;
  v4 = 1;
  sub_89F0(a1: qword_8E1B0D0 + 64, a2: 0);
  __wind
  {
    sub_4AC4F90();
    v1 = v0;
  }
  __unwind
  {
    sub_7C98D0(a1: &v3);
  }
  __wind
  {
    result = sub_8B30(a1: v1);
  }
  __unwind
  {
    sub_4AA5ED0();
  }
  return result;
}
```

  first arg of first sub is the flogdatabank, so in this case its 0x8E1B0D0
