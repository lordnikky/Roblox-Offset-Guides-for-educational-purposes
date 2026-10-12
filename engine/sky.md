**TODO**

note to self: I didn't forget to make this

# CubeTextures

string "AnalyticsPoints" first xref

```asm
.rdata:000000000700CA58 aAnalyticspoint_1 db 'AnalyticsPoints',0
.rdata:000000000700CA58                                         ; DATA XREF: sub_2DF6870+177↑o
```

offset is 0x2DF6870

# DrawSkyEnv

string "AdvSkyRGBELinearEnvFS"

```asm
.rdata:0000000007076808 aAdvskyrgbeline db 'AdvSkyRGBELinearEnvFS',0
.rdata:0000000007076808                                         ; DATA XREF: sub_3747BC0+6ED↑o
```
yes first xref 0x3747BC0
this shit covers DrawCubeCall, DrawSkyPixel, DrawStars, DrawSun its all handled by same shit so they have same rva lmao

# SkyGroup

string "RenderAdvSkyGroup" first xref

```c
]__int64 sub_3743420()
{
  return sub_4991AD0(a1: qword_8A927F8, a2: "RenderAdvSkyGroup", a3: &qword_7E1C7B8, a4: 1);
}
```

it should be the second qword
0x7E1C7B8

# SkyThread

"AdvSkyKickWake" first xref

```asm
.rdata:0000000007076590 aAdvskykickwake db 'AdvSkyKickWake',0   ; DATA XREF: sub_3744320+1F2↑o
```

0x3744320
