# FakeDatamodelPointer

string `"[FLog::BrowserServiceDiagnose] BrowserServiceDiagnose RbxEmbeddedWebViewIE::Invoke signalJavaScriptCallback %s"`, first xref

```c
      v11 = *(_OWORD *)&qword_8165CE8;
      sub_4AA6E30(
        a1: &v11,
        a2: "[FLog::BrowserServiceDiagnose] BrowserServiceDiagnose RbxEmbeddedWebViewIE::Invoke signalJavaScriptCallback %s",
        a3: v6);
    }
    v7 = sub_4D543B0();
    sub_7693C0(a1: v12, a2: v13);
```

sub after the string, double click it

```c
void *sub_4D543B0()
{
  _DWORD *v0; // rdi

  v0 = (_DWORD *)(*(_QWORD *)NtCurrentTeb()->ThreadLocalStoragePointer + 32LL);
  if ( dword_8F59800 > *v0 )
  {
    sub_1270(a1: &dword_8F59800);
    if ( dword_8F59800 == -1 )
    {
      sub_4D53AF0(a1: &unk_8F59808); // <-- take this
      atexit(a1: sub_641DBE0);
      sub_1350(a1: &dword_8F59800);
    }
  }
  if ( dword_8F59A28 <= *v0 )
    return &unk_8F59808; // <-- or this
  sub_1270(a1: &dword_8F59A28);
  if ( dword_8F59A28 != -1 )
    return &unk_8F59808; // <-- or even this
  sub_4D53AF0(a1: &unk_8F59A30);
  atexit(a1: sub_641DBD0);
  sub_1350(a1: &dword_8F59A28);
  return &unk_8F59808; // <-- or also this...
}
```

easiest pattern is just to look for <= *v_

so, take that rva, yes 0x8F59808 and just add 8 to it

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
