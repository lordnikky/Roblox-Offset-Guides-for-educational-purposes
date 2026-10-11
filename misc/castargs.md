# CastArgs

string "Argument %d missing or nil", second xref, decompile and scroll to the very top

```c
__int64 __fastcall sub_7A7EC0(__int64 a1, int a2, __int64 a3, int a4, unsigned int *a5)
{
  int v6; // ebx
  char v7; // bl
  __int64 v8; // r8
  unsigned __int64 v9; // r9
  __int64 v10; // rdx
  unsigned int *v11; // rax
  unsigned int v12; // ebx
  __int64 result; // rax
  __m128i pExceptionObject; // [rsp+30h] [rbp-98h] BYREF
  __m128i v15; // [rsp+40h] [rbp-88h]
  __int64 v16; // [rsp+50h] [rbp-78h]
  _QWORD v17[10]; // [rsp+60h] [rbp-68h] BYREF

  if ( a4 >= 3 )
  {
    v6 = a2 + 3;
    __eh34_enter_wind_state(-1, 0);
    __eh34_enter_wind_state(0, 1);
    v17[0] = sub_7A3930();
    memset(&v17[1], 0, 72);
    pExceptionObject = 0;
    v15 = 0;
    v16 = 0;
    v7 = sub_40ED3F0(a1, a2: v6, a3: (__int64)v17, a4: 1, a5: (__int64)&pExceptionObject); // <-- CastArgs
    v10 = pExceptionObject.m128i_i64[0];
    if ( pExceptionObject.m128i_i64[0] != 0 )
    {
```

its literally first rva in the function 

so the offset is 0x40ED3F0
