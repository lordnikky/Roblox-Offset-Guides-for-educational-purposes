**special thanks to proohio (994616269624062052) for teaching me this, people like them keep this repository great!!!!!!!!**


# FakeDatamodelPointer

string `"[FLog::BrowserServiceDiagnose] BrowserServiceDiagnose RbxEmbeddedWebViewIE::Invoke signalJavaScriptCallback %s"`, first xref

```c
      if ( v17 >= 0x10 )
        v6 = (_QWORD *)v16[0];
      v14 = *(_OWORD *)&qword_8250CB8;
      sub_4B50A20(
        a1: &v14,
        a2: "[FLog::BrowserServiceDiagnose] BrowserServiceDiagnose RbxEmbeddedWebViewIE::Invoke signalJavaScriptCallback %s",
        a3: v6);
    }
    v7 = sub_4E50F50();
    v8 = sub_738FE0(a1: v15, a2: v16);
    sub_4E52DD0(a1: v7, a2: v8);
```

sub after the string, double click it

```c
void *sub_4E50F50()
{
  if ( dword_8F8E958 > *(_DWORD *)(*(_QWORD *)NtCurrentTeb()->ThreadLocalStoragePointer + 40LL) )
  {
    sub_12E0(a1: &dword_8F8E958);
    if ( dword_8F8E958 == -1 )
    {
      sub_4E50630(a1: &unk_8F8E960); // <-- or this
      sub_5FCBC50(a1: sub_6601650);
      sub_14F0(a1: &dword_8F8E958);
    }
  }
  if ( dword_8F8EBE8 > *(_DWORD *)(*(_QWORD *)NtCurrentTeb()->ThreadLocalStoragePointer + 40LL) )
  {
    sub_12E0(a1: &dword_8F8EBE8);
    if ( dword_8F8EBE8 == -1 )
    {
      sub_4E50630(a1: &unk_8F8EBF0);
      sub_5FCBC50(a1: sub_6601640);
      sub_14F0(a1: &dword_8F8EBE8);
    }
  }
  return &unk_8F8E960; // <-- use this
}
```

easiest pattern is just to look for <= *v_

so, take that rva, yes 0x8F8E960 and just add 8 to it

<img width="325" height="506" alt="image" src="https://github.com/user-attachments/assets/19cce983-3dea-4213-bb71-2d6bd2e03567" />

That will be your FakeDatamodelPointer

# RealDataModel 

string `"[FLog::LuaAppExperienceController] LuaAppExperienceController: EnableLuaAppScriptErrorListener is enabled, connecting to ScriptContext.Error."` first xref

```c
    if ( (unsigned __int8)qword_81AB508 >= 6u && BYTE1(qword_81AB508) >= 4u )
    {
      v22.m128i_i64[0] = (__int64)"[FLog::LuaAppExperienceController] LuaAppExperienceController: EnableLuaAppScriptError"
                                  "Listener is enabled, connecting to ScriptContext.Error.";
      v4 = -1;
      do
        ++v4;
      while ( aFlogLuaappexpe_18[v4] != 0 );
      v22.m128i_i64[1] = v4;
      v21.m128i_i64[0] = 0;
      v21.m128i_i64[1] = (__int64)&v28;
      v24 = v21;
      v25 = v22;
      v26 = *(_OWORD *)&qword_81AB508;
      LOBYTE(a2) = 4;
      sub_4AA7070(a1: (unsigned int)&v26, a2, a3: (unsigned int)&v25, a4: (unsigned int)&v24, a5: 1);
    }
    v5 = v2 + 496; // <-- look for something like this under function with 5 args
    if ( v2 == 0 )
```

that number is not full realdatamodel, you have to take that number and add 8 to it, so 496+8 which is 504 and then turn that into hex which is 0x1F8

<img width="320" height="264" alt="image" src="https://github.com/user-attachments/assets/8d28c40c-4354-4ba0-8924-3e97a49d6e05" />

:D
