# ClientVTable

shift f4, ctrf f ```RBX::NetworkBase::RbxTransportConnection::`vftable'``` 

```asm
.rdata:0000000006D716E0 ; const RBX::NetworkBase::RbxTransportConnection::`vftable'
.rdata:0000000006D716E0 ??_7RbxTransportConnection@NetworkBase@RBX@@6B@ dq offset sub_3A851C0
.rdata:0000000006D716E0                                         ; DATA XREF: sub_3A850C0+20↑o
```

offset is 0x6D716E0

AppVTable

```RBX::RbxTransport::Impl::RtcAppConnection::`vftable'```

```asm
.rdata:0000000006CF6C38 ; const RBX::RbxTransport::Impl::RtcAppConnection::`vftable'
.rdata:0000000006CF6C38 ??_7RtcAppConnection@Impl@RbxTransport@RBX@@6B@ dq offset sub_20C8140
.rdata:0000000006CF6C38                                         ; DATA XREF: sub_20C14F0+1D↑o
.rdata:0000000006CF6C38                                         ; sub_20C16E0+1D↑o ...
```


# ClientDestructor


```RBX::NetworkBase::RbxTransportConnection::`vftable'```

```asm
.rdata:0000000006D716E0 ; const RBX::NetworkBase::RbxTransportConnection::`vftable'
.rdata:0000000006D716E0 ??_7RbxTransportConnection@NetworkBase@RBX@@6B@ dq offset sub_3A851C0 ; <-- here
.rdata:0000000006D716E0                                         ; DATA XREF: sub_3A850C0+20↑o
```

offset 0x3A851C0


# ClientSend

"Trying to send on a not ready channel!" 

first xref:

```asm
.rdata:00000000070909A8 aTryingToSendOn db 'Trying to send on a not ready channel!',0
.rdata:00000000070909A8                                         ; DATA XREF: sub_3A852E0:loc_3A85523↑o
.rdata:00000000070909A8                                         ; sub_3A85530:loc_3A85777↑o
```

# ClientReceive

i dont think its possible without a sig, 
48 89 5C 24 ? 48 89 6C 24 ? 48 89 74 24 ? 48 89 54 24 ? 57 41 56 41 57 48 81 EC 90 00 00 00

but 

```asm
.rdata:0000000006D71780                 dq offset sub_3A858A0
.rdata:0000000006D71788                 dq offset sub_3A85A30
.rdata:0000000006D71790                 dq offset sub_3A865A0
.rdata:0000000006D71798                 dq offset sub_3A86810
.rdata:0000000006D717A0                 dq offset sub_3A865F0
.rdata:0000000006D717A8                 dq offset sub_3A867A0
.rdata:0000000006D717B0                 dq offset ??_R4ConnectionInternal@NetworkBase@RBX@@6B@ ; const RBX::NetworkBase::ConnectionInternal::`RTTI Complete Object Locator'
.rdata:0000000006D717B8 ; const RBX::NetworkBase::ConnectionInternal::`vftable'
.rdata:0000000006D717B8 ??_7ConnectionInternal@NetworkBase@RBX@@6B@ dq offset sub_3A84B90
.rdata:0000000006D717B8                                         ; DATA XREF: sub_3A84620+16↑o
.rdata:0000000006D717B8                                         ; sub_3A84A90+D↑o
```

basically can be found with ??_7ConnectionInternal@NetworkBase@RBX@@6B@ - 0x38 which will result in .rdata:0000000006D71780                 dq offset sub_3A858A
```asm
.rdata:0000000006D71780                 dq offset sub_3A858A0
```

this will probably shift easily, ill have to find it every update but i'll do it

the top one is the offset 0x3A858A0

ps:

<details>
<summary>when decompiled it must look like this and take 2 args</b></summary>
```c
_QWORD *__fastcall sub_3A858A0(__int64 a1, _QWORD *a2)
{
  unsigned __int64 v4; // rsi
  __int64 **v5; // rcx
  __int64 *v6; // rbp
  __int64 *i; // rbx
  __int64 v8; // rcx
  _QWORD *result; // rax
  __int64 *v10; // [rsp+38h] [rbp-70h] BYREF
  __int64 *v11; // [rsp+40h] [rbp-68h]
  _BYTE v12[48]; // [rsp+60h] [rbp-48h] BYREF

  v4 = 0;
  *a2 = 0;
  a2[1] = 0;
  a2[2] = 0;
  __wind
  {
    do
    {
      if ( *(_BYTE *)(a1 + 2184) != 0 )
      {
LABEL_6:
        (*(void (__fastcall **)(_QWORD, __int64 **, _QWORD, __int64))(**(_QWORD **)(a1 + 2192) + 96LL))(
          a1: *(_QWORD *)(a1 + 2192),
          a2: &v10,
          a3: (unsigned int)v4,
          a4: 0x7FFFFFFF);
        __wind
        {
          v6 = v11;
          for ( i = v10; i != v6; i += 14 )
          {
            v8 = a2[1];
            if ( v8 == a2[2] )
            {
              sub_2166450(a1: a2, a2: a2[1], a3: i);
            }
            else
            {
              sub_5238130(a1: v8, a2: i);
              a2[1] += 88LL;
            }
          }
        }
        __unwind
        {
          sub_20AEFA0(a1: &v10);
        }
        v5 = &v10;
      }
      else
      {
        switch ( (int)v4 )
        {
          case 0:
          case 3:
          case 5:
          case 6:
          case 7:
          case 11:
            if ( (((_DWORD)v4 - 3) & 0xFFFFFFF7) != 0 )
              goto LABEL_15;
            (*(void (__fastcall **)(_QWORD, _BYTE *, _QWORD, __int64))(**(_QWORD **)(a1 + 2192) + 96LL))(
              a1: *(_QWORD *)(a1 + 2192),
              a2: v12,
              a3: (unsigned int)v4,
              a4: 0x7FFFFFFF);
            v5 = (__int64 **)v12;
            break;
          case 1:
          case 2:
          case 4:
          case 8:
          case 9:
          case 10:
          case 12:
          case 13:
            goto LABEL_6;
        }
      }
      sub_20B0EE0(a1: v5);
LABEL_15:
      ++v4;
    }
    while ( v4 < 0xE );
    result = a2;
  }
  __unwind
  {
    sub_20AEF80(a1: a2);
  }
  return result;
}
```
</details>

# ClientChannelConfig 


string "Failed to open send channel {}!", first xref 

```c
    v3 = sub_3A84FC0(a1: (__int64)v10, a2: v1); // <-- ClientChannelConfig
    v4 = *(__int64 **)(a1 + 2192);
    v5 = *(_QWORD *)v3;
    DWORD2(v9) = *(_DWORD *)(v3 + 8);
    v6 = *v4;
    *(_QWORD *)&v9 = v5;
    LOBYTE(v8) = BYTE8(v9);
    result = (*(__int64 (__fastcall **)(__int64 *, _QWORD, _QWORD, unsigned __int64, int))(v6 + 112))(
               a1: v4,
               a2: (unsigned int)v1,
               a3: (unsigned int)v5,
               a4: HIDWORD(v5),
               a5: v8);
    if ( (_BYTE)result == 0 )
    {
      v11 = (char *)sub_3A91A30(a1: (unsigned int)v1);
      sub_16714A0(a1: "Failed to open send channel {}!", a2: &v11); // <-- here
    }
```


# AppDestructor

```??_7RtcAppConnection@Impl@RbxTransport@RBX@@6B@```

```asm
.rdata:0000000006CF6C38 ; const RBX::RbxTransport::Impl::RtcAppConnection::`vftable'
.rdata:0000000006CF6C38 ??_7RtcAppConnection@Impl@RbxTransport@RBX@@6B@ dq offset sub_20C8140
.rdata:0000000006CF6C38                                         ; DATA XREF: sub_20C14F0+1D↑o
.rdata:0000000006CF6C38                                         ; sub_20C16E0+1D↑o ...
```

0x20C8140 is the offset


# AppSend

string "overflow_size"

first xref, go to very top, press x on the rva

```c
signed __int64 __fastcall sub_20C6F90(__int64 a1, unsigned int a2, __int64 *a3)
```

first xref, do that again in function you're put into, but dont double click:

```asm
Up	p	sub_20C3030+4C	call    sub_20C30B0
```
thats the AppSend

# AppReceive 

string "[DFLog::RbxTransportRnaExpConnection] {}. receivePop. Channel {} not found" or "e object field '{}' is not exported, returning nil." (cuz debug strings can be unreliable), first xref on both

```asm
.rdata:0000000006F629F0 aDflogRbxtransp_84 db '[DFLog::RbxTransportRnaExpConnection] {}. receivePop. Channel {} '
.rdata:0000000006F629F0                                         ; DATA XREF: sub_20C3420+BF↑o
.rdata:0000000006F62A31                 db 'not found',0
```

```asm
.rdata:00000000070E3A98 aTheStateObject db 'The state object field ',27h,'{}',27h,' is not exported, returnin'
.rdata:00000000070E3A98                                         ; DATA XREF: _RTC_AllocaFailure(void *,_RTC_ALLOCA_NODE *,int)+21D↑o
.rdata:00000000070E3A98                                         ; sub_20C3420+6AF↑o
.rdata:00000000070E3ACD                 db 'g nil.',0
```


# AppReceiveMaxBytes 

string "[DFLog::RbxTransportRnaExpConnection] {}. receivePopMaxBytes. channelId {}, maxBytes {}, bytesRead {}" or "[DFLog::RbxTransportRnaExpConnection] {}. receivePopMaxBytes. Channel {} not found" first xref on butt

```asm
.rdata:0000000006F62E90 aDflogRbxtransp_88 db '[DFLog::RbxTransportRnaExpConnection] {}. receivePopMaxBytes. cha'
.rdata:0000000006F62E90                                         ; DATA XREF: sub_20C3CD0+4F4↑o
.rdata:0000000006F62ED1                 db 'nnelId {}, maxBytes {}, bytesRead {}, bytes remaining {}',0
```

```asm
.rdata:0000000006F62A40 aDflogRbxtransp_87 db '[DFLog::RbxTransportRnaExpConnection] {}. receivePopMaxBytes. Cha'
.rdata:0000000006F62A40                                         ; DATA XREF: sub_20C3CD0+C3↑o
.rdata:0000000006F62A81                 db 'nnel {} not found',0
```


# StreamCreate and StreamAppend and StreamDestroy

string "RtcAppConnection::close", first xref

```asm
.rdata:0000000006F62940 aRtcappconnecti_2 db 'RtcAppConnection::close',0
.rdata:0000000006F62940                                         ; DATA XREF: sub_20C26F0+1BF↑o
```
decompile and scroll up until you see "\b"


```c
  _BYTE v52[40]; // [rsp+298h] [rbp+198h] BYREF

  v25 = a2;
  v34 = a3;
  v26 = 0;
  v5 = *(_BYTE *)(a1 + 3840);
  *(_BYTE *)(a1 + 3840) = 1;
  if ( v5 != 0 )
  {
    if ( *(_BYTE *)(a3 + 88) != 0 )
      sub_208F860(a1: (__int64 *)a3); // <-- StreamDestroy, its uhh first rva in the function you wont miss it
    return 0;
  }
  else
  {
    __wind
    {
      v7 = *(_BYTE *)(*(_QWORD *)(a1 + 104) + 71408LL);
      v8 = *(_BYTE *)(a3 + 88);
      v9 = 0;
      if ( v7 == 0 && v8 == 0 )
      {
        v50 = *a2;
        v51 = a2[1];
        sub_720E70(a1: v52, a2: a2 + 2);
        __wind
        {
          __wind
          {
            sub_5237C70(a1: (__int64)v39, a2: 10, a3: 8u); // <-- StreamCreate
            v26 = 3;
            v24[0] = 1;
            sub_20CA6B0(a1: v39, a2: v24, a3: 1);
            sub_20CA6B0(a1: v39, a2: "\b", a3: 1); // <-- anchor which is also StreamAppend
            v10 = v51;
            v27 = htonl(hostlong: (v51 | ((unsigned __int64)v50 << 32)) >> 32);
            sub_20CA6B0(a1: v39, a2: &v27, a3: 4);
            v28[0] = htonl(hostlong: v10);
```


# ClientRtti 

```RBX::NetworkBase::RbxTransportConnection::`RTTI Complete Object Locator'```

```asm
.rdata:00000000074FA7C8 ; const RBX::NetworkBase::RbxTransportConnection::`RTTI Complete Object Locator'
.rdata:00000000074FA7C8 ??_R4RbxTransportConnection@NetworkBase@RBX@@6B@ dd 1
.rdata:00000000074FA7C8                                         ; DATA XREF: .rdata:0000000006D716D8↑o
.rdata:00000000074FA7C8                                         ; .rdata:00000000074FA7DC↓o
.rdata:00000000074FA7C8                                         ; signature
```

offset is 0x74FA7C8

# AppRTTI

```RBX::RbxTransport::Impl::RtcAppConnection::`RTTI Complete Object Locator'```

```asm
.rdata:000000000745E7E0 ; const RBX::RbxTransport::Impl::RtcAppConnection::`RTTI Complete Object Locator'
.rdata:000000000745E7E0 ??_R4RtcAppConnection@Impl@RbxTransport@RBX@@6B@ dd 1
.rdata:000000000745E7E0                                         ; DATA XREF: .rdata:0000000006CF6C30↑o
.rdata:000000000745E7E0                                         ; .rdata:000000000745E7F4↓o
.rdata:000000000745E7E0                                         ; signature
```

0x745E7E0 is the offset


# UseRbxTransportClient 

string "UseRbxTransportClient" second xref

```c
__int64 sub_3A6BAA0()
{
  return sub_4993490(a1: qword_8A927D8[4], a2: "UseRbxTransportClient", a3: &unk_8694E30, a4: 1);
}
```

unk_ is the offset (0x8694E30) or qword whatever it'll be


# FailureFallbackToRbxTransport

string "failureFallbackToRbxTransport", first xref

```c
                            v128.m128i_i64[0] = (__int64)"failureFallbackToRbxTransport"; // <-- here
                            v128.m128i_i64[1] = 29;
                            v146 = v128;
                            sub_2E01900(a1: v199, a2: &v146, a3: byte_86A3408[0], a4: 1); // <-- failureFallbackToRbxTransport
                            if ( byte_86A3408[0] != 0 ) // <-- failureFallbackToRbxTransport
```
