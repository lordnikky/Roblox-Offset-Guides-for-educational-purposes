# CubeTextures

string `AnalyticsPoints` first xref

```asm
.rdata:000000000700CA58 aAnalyticspoint_1 db 'AnalyticsPoints',0
.rdata:000000000700CA58                                         ; DATA XREF: sub_2DF6870+177↑o
```

offset is 0x2DF6870

# DrawSkyEnv

string `AdvSkyRGBELinearEnvFS`

```asm
.rdata:0000000007076808 aAdvskyrgbeline db 'AdvSkyRGBELinearEnvFS',0
.rdata:0000000007076808                                         ; DATA XREF: sub_3747BC0+6ED↑o
```
yes first xref 0x3747BC0
this shit covers DrawCubeCall, DrawSkyPixel, DrawStars, DrawSun its all handled by same shit so they have same rva lmao

# SkyGroup

string `RenderAdvSkyGroup` first xref

```c
__int64 sub_374AFC0()
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
  v3[0] = "RenderAdvSkyGroup";
  v3[1] = 17;
  sub_49FD170(a1: v0, a2: v3, a3: &qword_8002008, a4: 1);
  return sub_8B30(a1: v1);
}
```

qword (or byte or unk) after a3:

0x8002008

# SkyThread

`AdvSkyKickWake` first xref

```asm
.rdata:0000000007076590 aAdvskykickwake db 'AdvSkyKickWake',0   ; DATA XREF: sub_3744320+1F2↑o
```

0x3744320
