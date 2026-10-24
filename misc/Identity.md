# IdentityPTR

string `ParabolaAdornment may only be instantiated by CoreScripts at this time`, first xref

```c
    *(_QWORD *)a1 = &RBX::ParabolaAdornment::`vftable';
    *(_QWORD *)(a1 + 160) = &RBX::ParabolaAdornment::`vftable';
    *(_QWORD *)(a1 + 192) = &RBX::ParabolaAdornment::`vftable';
    v7 = (_QWORD *)sub_6BB0(a1: qword_854F778);
    v8 = (__int64 (__fastcall *)(_QWORD, _QWORD))v7[7];
    if ( v8 != nullptr )
    {
      v7[6] = v8(a1: v7[6], a2: v7[4]);
      v7[7] = 0;
    }
    if ( (v7[6] & 8) == 0 )
    {
      sub_71D690(a1: pExceptionObject, a2: "ParabolaAdornment may only be instantiated by CoreScripts at this time");
      throw (std::runtime_error *)pExceptionObject;
    }
```

under the rtti you'll see _qword with sub that has 1 arg, the first sub is GetTlsPointer, while second one is IdentityPtr, so in 1 line that's 2 rva's

GetTlsPointer: 0x6BB0

IdentityPtr: 0x854F778
