this will cover quite some raknet offsets

**if you're searching for specific offset i recommend pressing ctrl + f and just search the name of it because this will have a lot of stuff**

# raknetrecieve

search for string "[DFLog::NetworkTrace] Incoming packet error: length <= 2 || buffe", or "[DFLog::NetworkTrace] Incoming packet error: internalPacket->orde", first xref will be it:

```asm
.rdata:0000000006E41270 aDflogNetworktr_10 db '[DFLog::NetworkTrace] Incoming packet error: length <= 2 || buffe'
.rdata:0000000006E41270                                         ; DATA XREF: sub_29179F0+2AF2↑o
.rdata:0000000006E412B1                 db 'r == 0, length=%d, address=%s',0
.rdata:0000000006E412CF                 align 10h
```

so the offset is 0x29179F0


# RaknetReportNetworkError

search for string "ConnectionFailure" or "[DFLog::NetworkTrace] reportPerServerMetric::: sc(%s:%d).state =", first xref

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

search for string "[FLog::Network] out of memory in raknet at callsite %ld", second xref

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


# RakNetSend

search for string "[FLog::Network] out of memory in raknet at callsite %ld" and first xref will be it:

```asm
.rdata:0000000006E3E360 aFlogNetworkOut db '[FLog::Network] out of memory in raknet at callsite %ld',0
.rdata:0000000006E3E360                                         ; DATA XREF: sub_28F5620+100↑o
.rdata:0000000006E3E360                                         ; sub_290A2F0+1F↑o
```

0x28F5620 is the offset


# RakNetProcessNetworkPacket

search for string "RakPeer::ProcessNetworkPacket" first xref will be it

```asm
.rdata:0000000006E3D780 aRakpeerProcess db 'RakPeer::ProcessNetworkPacket',0
.rdata:0000000006E3D780                                         ; DATA XREF: sub_2901BC0+B18↑o
.rdata:0000000006E3D79E                 align 20h
```

so the offset is 0x2901BC0


# UpdateNetworkLoop

search for string "[FLog::Network] Timed-out: Failed to gracefully end update loop w" or "[DFLog::RakNetPktTrace] [%s][%s][ext=%s][%s][drop=%d][%#x][%s]", first xref will be it

```asm
.rdata:0000000006E3E950 aFlogNetworkTim_1 db '[FLog::Network] Timed-out: Failed to gracefully end update loop w' or "
.rdata:0000000006E3E991                 db 'ithin %d (ms). Actual time taken: %d (ms).',0
.rdata:0000000006E3E9BC asc_6E3E9BC     db '%#x ',0             ; DATA XREF: sub_28E7090+F0↑o
```

so the offset is 0x28E7090


# SendPacketsToSelf

search for string "[FLog::Network] RakPeer::SendPacketsToSelfToUnblockSocketReceiveT" or just SendPacketsToSelfToUnblockSocketReceiveT in case that doesnt have an xref, first xref will be the offset

```asm
.rdata:0000000006E3E830 aFlogNetworkRak_1 db '[FLog::Network] RakPeer::SendPacketsToSelfToUnblockSocketReceiveT'
.rdata:0000000006E3E830                                         ; DATA XREF: sub_28EAF50+110↑o
```

so the offset is 0x28EAF50


# RakPeerReceive

search for string "[DFLog::RaknetJoinOrDisconnectRequest] RakNet Receiving %s packet" first xref will be the rakpeerrecieve

```asm
.rdata:0000000006E3ED90 aDflogRaknetjoi db '[DFLog::RaknetJoinOrDisconnectRequest] RakNet Receiving %s packet'
.rdata:0000000006E3ED90                                         ; DATA XREF: sub_28ECA20+E7↑o
.rdata:0000000006E3EDD1                 db 0
```

so the offset is 0x28ECA20


# RakPeerVirtualTable

search for string "Unable to find NetAssetManager but should be loaded", first xref, decompile, you will be put to the very end, scroll up until the string that you got put to hides behind the output window, after that scroll once again, you should see something like this:

```c
      v71 = sub_49062B0(a1: 4200);
      v72 = v71;
      if ( v71 == 0 )
      {
        sub_7AE130(a1: v204);
        CxxThrowException(pExceptionObject: v204, pThrowInfo: (_ThrowInfo *)&_TI2_AVbad_alloc_std__);
      }
      v168 = v71;
      *(_DWORD *)(v71 + 8) = 1;
      *(_DWORD *)(v71 + 12) = 1;
      *(_QWORD *)v71 = &std::_Ref_count_obj2<RakNet::RakPeer>::`vftable';
      sub_28E7670(a1: v71 + 16); // <-- double click the rva
      v76 = v8 | 0x80;
      *((_QWORD *)v70 + 3) = v72 + 16;
      v77 = *((_QWORD *)v70 + 4);
      *((_QWORD *)v70 + 4) = v72;
      if ( v77 != 0 )
        sub_7BC290(a1: v77, a2: v73, a3: v74, a4: v75);
      LOBYTE(v73) = 1;
      (*(void (__fastcall **)(_QWORD, __int64))(**((_QWORD **)v70 + 3) + 368LL))(a1: *((_QWORD *)v70 + 3), a2: v73);
      (*(void (__fastcall **)(_QWORD, _QWORD))(**((_QWORD **)v70 + 3) + 528LL))(
        a1: *((_QWORD *)v70 + 3),
        a2: *((_QWORD *)v70 + 2));
      v8 = v76 | 0x60;
      v78 = (char **)(a1 + 344);
      if ( (char *)(a1 + 344) == &v181 )
      {
        v80 = *(void (__fastcall ***)(char *, __int64))v70;
```

then you'll be put here

```c
_int64 __fastcall sub_28E7670(__int64 a1)
{
  __int64 v2; // rax
  __int64 v3; // rax
  __int64 v4; // rax
  __int64 i; // rcx
  __int64 *v6; // rax
  __int64 v7; // rcx
  unsigned int v8; // eax
  unsigned int v9; // eax
  _DWORD v11[2]; // [rsp+30h] [rbp-218h] BYREF
  _QWORD v12[2]; // [rsp+38h] [rbp-210h] BYREF
  _BYTE v13[8]; // [rsp+48h] [rbp-200h] BYREF
  _DWORD pExceptionObject[3]; // [rsp+50h] [rbp-1F8h] BYREF
  _BYTE v15[20]; // [rsp+5Ch] [rbp-1ECh] BYREF
  _BYTE v16[416]; // [rsp+70h] [rbp-1D8h] BYREF

  v12[1] = a1;
  *(_QWORD *)a1 = &RakNet::RakPeer::`vftable';
  *(_QWORD *)(a1 + 8) = 0;
  *(_QWORD *)(a1 + 16) = 0;
```

double click the &RakNet::RakPeer::`vftable and thats where the offset is:

```asm
.rdata:0000000006BB1740 ; const RakNet::RakPeer::`vftable'
.rdata:0000000006BB1740 ??_7RakPeer@RakNet@@6B@ dq offset sub_28E8350
.rdata:0000000006BB1740                                         ; DATA XREF: sub_28E7670+33↑o
.rdata:0000000006BB1740                                         ; sub_28E83F0+17↑o
```

so the offset is 0x6BB1740


# convertItemEnumToString

search for string "Stream Prefetch Request Items" first xref will be da needed thing

```asm
.rdata:0000000007023E20 aStreamPrefetch_0 db 'Stream Prefetch Request Items',0
.rdata:0000000007023E20                                         ; DATA XREF: sub_47C64C0:loc_47C65C7↑o
.rdata:0000000007023E3E                 align 20h
```

so the offset is 0x47C64C0
