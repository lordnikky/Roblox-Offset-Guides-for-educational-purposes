# DisconnectConnect

string `Function Connection.Disconnect is not safe to call in parallel` first xref, well uhh, thats all lmao

```asm
.rdata:000000000729ADC8 aFunctionConnec db 'Function Connection.Disconnect is not safe to call in parallel',0
.rdata:000000000729ADC8                                         ; DATA XREF: sub_4169EE0:loc_4169FC3↑o
```

yeah i dont think this needs the verify section 

# FireTouchInterest

string `new overlap in different world` first xref decompile it

```c
            if ( v52 == 0 || v51 == 0 || *(_QWORD *)(v52 + 512) != *(_QWORD *)(v51 + 512) )
              sub_49DDC40(a1: "new overlap in different world", a2: &lParam);
            if ( (unsigned __int8)sub_1589DB0(a1: v52, a2: v51, a3: 0) == 0 )
              sub_15205C0(a1: *(_QWORD **)(v52 + 512), a2: v52, a3: v51, a4: 0, a5: 0);
            goto LABEL_76;
```

seocond sub after it, the sub_15205C0 is firetouchinterest

offset is 15205C0

<details>

<summary><b>verify</b></summary>

takes 5 args is about 40 lines long 

```c
  __int64 v13; // rcx

  if ( byte_84EF648 != 0 )
    v7 = (void (__fastcall ***)(_QWORD, __int64, __int64, _QWORD, char))a1[24];
  else
    v7 = (void (__fastcall ***)(_QWORD, __int64, __int64, _QWORD, char))a1[23];
  if ( v7 != nullptr && (unsigned __int8)sub_15C7610(a1: a1[320]) != 0 )
  {
    v9 = *(_QWORD *)(a2 + 72);
    v10 = v9 == 0;
    v11 = v9 - 16;
    v12 = *(_QWORD *)(v8 + 72);
    if ( v10 )
      v11 = 0;
    v13 = v12 - 16;
    if ( v12 == 0 )
```

first 5 lines are good identificator

```c
  if ( byte_84EF648 != 0 )
    v7 = (void (__fastcall ***)(_QWORD, __int64, __int64, _QWORD, char))a1[24];
  else
    v7 = (void (__fastcall ***)(_QWORD, __int64, __int64, _QWORD, char))a1[23];
  if ( v7 != nullptr && (unsigned __int8)sub_15C7610(a1: a1[320]) != 0 )
```

  
</details>

I think for firetouchinterest u'll also need Primitive and BasePart

# BasePart

string `new overlap in different world` first xref

```c
            v51 = *(_QWORD *)(v42 + 16);
            v52 = *(_QWORD *)(v42 + 8);
            if ( v52 == 0 || v51 == 0 || *(_QWORD *)(v52 + 512) != *(_QWORD *)(v51 + 512) )
              sub_49DDC40(a1: "new overlap in different world", a2: &lParam);
            if ( (unsigned __int8)sub_1589DB0(a1: v52, a2: v51, a3: 0) == 0 )
              sub_15205C0(a1: *(_QWORD *)(v52 + 512), a2: v52, a3: v51, a4: 0, a5: 0);
            goto LABEL_76;
```

right above that string there's if statement, at the end of it there's number, press h on it and that's your BasePart (0x200)


# Primitive

same string, second xref 

```c
__int64 __fastcall sub_188B1A0(__int64 a1)
{
  __int64 v1; // r8
  __int64 v2; // rdx
  __int64 v3; // rcx

  v1 = *(_QWORD *)(*(_QWORD *)(a1 + 32) + 384LL);
  v2 = *(_QWORD *)(*(_QWORD *)(a1 + 16) + 384LL);
  if ( v2 == 0 || v1 == 0 || (v3 = *(_QWORD *)(v2 + 512)) != *(_QWORD *)(v1 + 512) )
    sub_49DDC40(a1: "new overlap in different world", a2: &lParam);
  return sub_15205C0(a1: v3, a2: v2, a3: v1, a4: 0, a5: 1);
}
```

see that 2 first lines with numbers at the end? that's your Primitive, so its 0x180



<details>>

<summary><b>click this</b></summary>

<img width="345" height="345" alt="image" src="https://github.com/user-attachments/assets/d7b4e502-76d2-4d62-a83f-5a837509c0fa" />

</details>
