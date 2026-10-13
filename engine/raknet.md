this will cover quite some raknet offsets

**if you're searching for specific offset i recommend pressing ctrl + f and just search the name of it because this will have a lot of stuff**

raknet has been disabled by roblox in favour of rbxtransport, but, raknet still can be used via FFlag that you can found in my guides about rbxtransport

# raknetrecieve

search for string `"[DFLog::NetworkTrace] Incoming packet error: length <= 2 || buffe"`, or `"[DFLog::NetworkTrace] Incoming packet error: internalPacket->orde"`, first xref will be it:

```asm
.rdata:0000000006E41270 aDflogNetworktr_10 db '[DFLog::NetworkTrace] Incoming packet error: length <= 2 || buffe'
.rdata:0000000006E41270                                         ; DATA XREF: sub_29179F0+2AF2↑o
.rdata:0000000006E412B1                 db 'r == 0, length=%d, address=%s',0
.rdata:0000000006E412CF                 align 10h
```

so the offset is 0x29179F0

# RaknetReportNetworkError

search for string `"ConnectionFailure"` or `"[DFLog::NetworkTrace] reportPerServerMetric::: sc(%s:%d).state ="`, first xref

```asm
.rdata:0000000006FAEFE8 aConnectionfail db 'ConnectionFailure',0
.rdata:0000000006FAEFE8                                         ; DATA XREF: sub_47076E0+23C↑o
```

so the offset is 0x47076E0

# RaknetHandleConnectionState

search for string "updateServerConnectionState", first xref

```asm
.rdata:0000000006FAE550 aDflogNetworktr_14 db '[DFLog::NetworkTrace] updateServerConnectionState::: sc(%s).old_s'
.rdata:0000000006FAE550                                         ; DATA XREF: sub_4719560+182↑o
```

# RakNetReliabilityLayerSend

search for string `"[FLog::Network] out of memory in raknet at callsite %ld"`, second xref

```asm.rdata:0000000006E3E360 aFlogNetworkOut db '[FLog::Network] out of memory in raknet at callsite %ld',0
.rdata:0000000006E3E360                                         ; DATA XREF: sub_28F5620+100↑o
.rdata:0000000006E3E360                                         ; sub_290A2F0+1F↑o
```

sub_290A2F0 decompile the function

```c
unsigned __int64 __fastcall sub_290A2F0(__int64 a1, int a2)
{
  unsigned __int64 result; // rax
  __int128 v3; // [rsp+20h] [rbp-18h] BYREF

  result = qword_7C57C48;
  if ( (unsigned __int8)qword_7C57C48 >= 6u )
  {
    result = (unsigned __int64)qword_7C57C48 >> 8;
    if ( BYTE1(qword_7C57C48) >= 3u )
    {
      v3 = *(_OWORD *)&qword_7C57C48;
      return sub_4922BB0(a1: &v3, a2: "[FLog::Network] out of memory in raknet at callsite %ld", a2);
    }
  }
  return result;
}
```
	
press x on sub_290A2F0 and first xref will be it: Down	p	sub_291A640+CB	call    sub_290A2F0

so the offset is 0x291A640

(you can also scroll up a bit when you press on the sub_290A2F0 and see this .text:000000000290A2F0 sub_290A2F0     proc near               ; CODE XREF: sub_291A640+CB↓p the xref will be RakNetReliabilityLayerSend)

<details>

<summary><b>verify:</b></summary>


takes 13 args, at the very end you should see this

```c
      v36 = sub_27E5B40(a1, a2: *(unsigned int *)(v21 + 92));
      v37 = *(_DWORD *)(a1 + 352);
      v43[0] = v36;
      v43[1] = v21;
      sub_27E85A0(a1: a1 + 344, a2: v43);
      if ( v37 != 0 )
      {
        do
        {
          v38 = (v37 - 1) >> 1;
          a2 = 2LL * v38;
          v39 = *(_QWORD *)(a1 + 344);
          if ( *(_QWORD *)(v39 + 16LL * v38) <= v36 )
            break;
          v40 = *(_OWORD *)(v39 + 16LL * v37);
          *(_OWORD *)(v39 + 16LL * v37) = *(_OWORD *)(v39 + 16LL * ((v37 - 1) >> 1));
          *(_OWORD *)(*(_QWORD *)(a1 + 344) + 16LL * ((v37 - 1) >> 1)) = v40;
          v37 = (v37 - 1) >> 1;
        }
        while ( v38 != 0 );
      }
      if ( unk_83CDCA8 != 0 )
        *(_QWORD *)(a1 + 4056) += ((unsigned __int64)(unsigned int)(*(_DWORD *)(v21 + 24) + 7) >> 3) + 272;
      ++*(_DWORD *)(a1 + 4LL * *(int *)(v21 + 92) + 816);
      *(double *)(a1 + 8LL * *(int *)(v21 + 92) + 832) = (double)((unsigned int)(*(_DWORD *)(v21 + 24) + 7) >> 3)
                                                       + *(double *)(a1 + 8LL * *(int *)(v21 + 92) + 832);
      v22 = 1;
```
but uhh, 13 args check should be more than enough lol
	
</details>

# RakNetSend

search for string `"[FLog::Network] out of memory in raknet at callsite %ld"` and first xref will be it:

```asm
.rdata:0000000006E3E360 aFlogNetworkOut db '[FLog::Network] out of memory in raknet at callsite %ld',0
.rdata:0000000006E3E360                                         ; DATA XREF: sub_28F5620+100↑o
.rdata:0000000006E3E360                                         ; sub_290A2F0+1F↑o
```

0x28F5620 is the offset

# RakPeerProcessNetworkPacket

search for string "RakPeer::ProcessNetworkPacket" first xref will be it

```asm
.rdata:0000000006E3D780 aRakpeerProcess db 'RakPeer::ProcessNetworkPacket',0
.rdata:0000000006E3D780                                         ; DATA XREF: sub_2901BC0+B18↑o
.rdata:0000000006E3D79E                 align 20h
```

so the offset is 0x2901BC0

# UpdateNetworkLoop

search for string `"[FLog::Network] Timed-out: Failed to gracefully end update loop w"` or `"[DFLog::RakNetPktTrace] [%s][%s][ext=%s][%s][drop=%d][%#x][%s]"`, first xref will be it

```asm
.rdata:0000000006E3E950 aFlogNetworkTim_1 db '[FLog::Network] Timed-out: Failed to gracefully end update loop w' or "
.rdata:0000000006E3E991                 db 'ithin %d (ms). Actual time taken: %d (ms).',0
.rdata:0000000006E3E9BC asc_6E3E9BC     db '%#x ',0             ; DATA XREF: sub_28E7090+F0↑o
```

so the offset is 0x28E7090

# SendPacketsToSelf

search for string `"[FLog::Network] RakPeer::SendPacketsToSelfToUnblockSocketReceiveT"` or just SendPacketsToSelfToUnblockSocketReceiveT in case that doesnt have an xref, first xref will be the offset

```asm
.rdata:0000000006E3E830 aFlogNetworkRak_1 db '[FLog::Network] RakPeer::SendPacketsToSelfToUnblockSocketReceiveT'
.rdata:0000000006E3E830                                         ; DATA XREF: sub_28EAF50+110↑o
```

so the offset is 0x28EAF50

# RakPeerReceive

search for string `"[DFLog::RaknetJoinOrDisconnectRequest] RakNet Receiving %s packet"` first xref will be the rakpeerrecieve

```asm
.rdata:0000000006E3ED90 aDflogRaknetjoi db '[DFLog::RaknetJoinOrDisconnectRequest] RakNet Receiving %s packet'
.rdata:0000000006E3ED90                                         ; DATA XREF: sub_28ECA20+E7↑o
.rdata:0000000006E3EDD1                 db 0
```

so the offset is 0x28ECA20

# RakPeerVirtualTable

press shift f4 and ctrl f, search for ```RakNet::RakPeer::`vftable'```
```asm
const RakNet::RakPeer::`vftable'	0000000006D03FC8
```

that 0000000006D03FC8 is the rva, 0x6D03FC8

so the offset is 0x6D03FC8

# convertItemEnumToString

search for string "Stream Prefetch Request Items" first xref will be da needed thing

```asm
.rdata:0000000007023E20 aStreamPrefetch_0 db 'Stream Prefetch Request Items',0
.rdata:0000000007023E20                                         ; DATA XREF: sub_47C64C0:loc_47C65C7↑o
.rdata:0000000007023E3E                 align 20h
```

so the offset is 0x47C64C0

# RakNetEncrypt

search for string "encryptionResult", first xref do not decompile, scroll up a bit till you see ------:

```asm
.text:00000000028B1B26 ; ---------------------------------------------------------------------------
.text:00000000028B1B26
.text:00000000028B1B26 loc_28B1B26:                            ; CODE XREF: sub_28B17D0+32C↑j
.text:00000000028B1B26                 mov     r15d, 5
.text:00000000028B1B2C
.text:00000000028B1B2C loc_28B1B2C:                            ; CODE XREF: sub_28B17D0+280↑j <-- that loc_ is the encrypt offset
.text:00000000028B1B2C                                         ; sub_28B17D0+291↑j ...
.text:00000000028B1B2C                 inc     qword ptr [rsi+110h]
.text:00000000028B1B33                 inc     qword ptr [rsi+118h]
.text:00000000028B1B3A                 lea     rdx, off_7D6B658 ; "RakNetEncryptionResultCounter"
.text:00000000028B1B41                 lea     rcx, [rbp+3B0h+var_390]
.text:00000000028B1B45                 call    sub_28B8DB0
.text:00000000028B1B4A                 nop
.text:00000000028B1B4B                 lea     rcx, [rbp+3B0h+var_C0]
.text:00000000028B1B52                 call    sub_2ED80D0
.text:00000000028B1B57                 lea     rcx, [rbp+3B0h+var_C0]
.text:00000000028B1B5E                 call    sub_2ED8350
.text:00000000028B1B63                 lea     rax, aEncryptionresu ; "encryptionResult" <-- you're here
.text:00000000028B1B6A                 mov     qword ptr [rbp+3B0h+var_420], rax
.text:00000000028B1B6E                 mov     qword ptr [rbp+3B0h+var_420+8], 10h
```

so the offset is 0x28B1B2C
