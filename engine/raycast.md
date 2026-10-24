some of raycast stuff :D

# ShapeCast

string Attempt to shapecast with distance %f. The maximum distance is %f`, first xref will be it

```asm
.rdata:0000000006D32AA0 aAttemptToShape_0 db 'Attempt to shapecast with distance %f. The maximum distance is %f'
.rdata:0000000006D32AA0                                         ; DATA XREF: sub_EC7720+E42↑o
.rdata:0000000006D32AE1                 db '.',0
.rdata:0000000006D32AE3                 align 10h
```

so the offset is 0xEC7720

# SphereCast

search for string `Attempt to shapecast with distance %f. The maximum distance is %d`, second xref 
```asm
.rdata:0000000006D327F0 aAttemptToSpher db 'Attempt to spherecast with radius %f. The maximum radius is %f.',0
.rdata:0000000006D327F0                                         ; DATA XREF: sub_EC65E0+549↑o
.rdata:0000000006D327F0                                         ; sub_EC70A0+134↑o
```

so the offset is 0xEC70A0

# BlockCast

search for string `Attempt to blockcast with side length %f. The maximum side length is %f`, second xref will be it
```asm
.rdata:0000000006D32AF0 aAttemptToBlock db 'Attempt to blockcast with side length %f. The maximum side length'
.rdata:0000000006D32AF0                                         ; DATA XREF: sub_EC6B60+3A3↑o
.rdata:0000000006D32AF0                                         ; sub_EC6F50+126↑o
``` 

so the offset is 0xEC6F50


# WorldRoot_Raycast (or just normal raycast)

string `Raycast` exactly like that, same uppercasing nothing else, first xref
```asm
.rdata:0000000006D3BC40 aRaycast        db 'Raycast',0          ; DATA XREF: sub_FA55F0:loc_FA5649↑o
.rdata:0000000006D3BC40                                         ; .rdata:0000000006A13AA8↑o
```

decompile, scroll to the very up and press x on the rva

```c
__int64 *__fastcall sub_FA55F0(
```

first xref, go to it

```c
  v29 = 0;
  v30 = nullptr;
  sub_40FE120(a1: v41, a2: &v28);
  v40 = v0;
  v31[0] = sub_EC5D60; // <-- WorldRoot_Raycast
  v31[1] = 0;
  sub_FA55F0(a1: v1, a2: (unsigned int)v31, a3: v2, a4: v3); // <-- you're here
  if ( (_QWORD)v29 != 0 )
    (*(void (__fastcall **)(_QWORD, __int64))(*(_QWORD *)v29 + 24LL))(a1: v29, a2: 1);
  *(_QWORD *)&v29 = 0;
  v7 = (unsigned __int64)v30;
```

so the offset is 0xEC5D60

<details>
  
<summary><b>verify</b></summary>

takes 5 args

```c
  _BYTE v57[8]; // [rsp+428h] [rbp+320h] BYREF
  _BYTE v58[56]; // [rsp+430h] [rbp+328h] BYREF

  v35 = (signed __int64)a2;
  v29 = sub_4959690(a1: unk_867C100, (__int64)a2);
  sub_DB62E0(a1: v53, a2: *(_QWORD *)(a1 + 1024), a3: a5);
  sub_14CA2B0(a1: *(_QWORD *)(*(_QWORD *)(*(_QWORD *)(a1 + 1024) + 2240LL) + 2200LL));
  v30 = 0;
  v31 = 0;
  v32.m128_u64[0] = 0;
  v32.m128_i32[2] = 2139095040;
  v32.m128_i8[12] = 0;
  LODWORD(v33) = 1792;
  v9 = *(_QWORD *)(*(_QWORD *)(a1 + 1024) + 2240LL);
  v42 = *a3;
  v43 = *((_DWORD *)a3 + 2);
  v44 = *a4;
  v45 = *((_DWORD *)a4 + 2);
  v11 = sub_4959690(a1: unk_867C100, a2: v10);
  v36 = v11;
  v38 = v44;
  v39 = v45;
  v40 = v42;
  v41 = v43;
  LOBYTE(a1) = sub_1574C80(
                 a1: v9,
                 a2: (unsigned int)&v40,
                 a3: (unsigned int)&v38,
                 a4: (unsigned int)v53,
                 a5: (__int64)&v30);
  sub_4959690(a1: v11, a2: v12);
  if ( (_BYTE)a1 != 0 )
  {
    v50 = 0;
    v15 = v31;
    v46 = v31;
    v16 = v32;
    v47 = v32;
    v17 = _mm_shuffle_ps(v31, v31, 170).m128_f32[0];
    v18 = _mm_shuffle_ps(v31, v31, 85).m128_f32[0];
    v19 = v31.m128_f32[0];
    v20 = (float)((float)((float)(*(float *)a3 - v31.m128_f32[0]) * (float)(*(float *)a3 - v31.m128_f32[0]))
                + (float)((float)(*((float *)a3 + 1) - v18) * (float)(*((float *)a3 + 1) - v18)))
        + (float)((float)(*((float *)a3 + 2) - v17) * (float)(*((float *)a3 + 2) - v17));
    if ( v20 < 0.0 )
      v21 = sqrtf(X: v20);
    else
```

</details>

# FastClusterEntity VTableRva

press shift f4, ctrl f and search for ```RBX::Graphics::FastClusterEntity::`vftable'```, you'll see something like

```asm
const RBX::Graphics::FastClusterEntity::`vftable'	0000000006D70CE8
```

you can double click and just directly copy the rva:

```asm
.rdata:0000000006D70CE8 ; const RBX::Graphics::FastClusterEntity::`vftable'
.rdata:0000000006D70CE8 ??_7FastClusterEntity@Graphics@RBX@@6B@ dq offset sub_39AB450
.rdata:0000000006D70CE8                                         ; DATA XREF: sub_39AB180+E4↑o
.rdata:0000000006D70CE8                                         ; sub_39AB480+D↑o
```

so the offset is 0x6D70CE8
