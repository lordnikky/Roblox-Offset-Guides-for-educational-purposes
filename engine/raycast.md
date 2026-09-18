some of raycast stuff :D

# ShapeCast

string "Attempt to shapecast with distance %f. The maximum distance is %f", first xref will be it
(you can also use this signature 48 8B C4 55 53 56 57 41 54 41 55 41 56 41 57 48 81 EC 88 05 00 00)
```asm
.rdata:0000000006D32AA0 aAttemptToShape_0 db 'Attempt to shapecast with distance %f. The maximum distance is %f'
.rdata:0000000006D32AA0                                         ; DATA XREF: sub_EC7720+E42↑o
.rdata:0000000006D32AE1                 db '.',0
.rdata:0000000006D32AE3                 align 10h
```

so the offset is 0xEC7720

# SphereCast

search for string "Attempt to shapecast with distance %f. The maximum distance is %d", second xref 
(also can be found via this signature 48 8B C4 48 89 70 ? 57 48 81 EC 90 00 00 00 80 3D)
```asm
.rdata:0000000006D327F0 aAttemptToSpher db 'Attempt to spherecast with radius %f. The maximum radius is %f.',0
.rdata:0000000006D327F0                                         ; DATA XREF: sub_EC65E0+549↑o
.rdata:0000000006D327F0                                         ; sub_EC70A0+134↑o
```

so the offset is 0xEC70A0

# BlockCast

search for string "Attempt to blockcast with side length %f. The maximum side length is %f", second xref will be it
48 8B C4 48 89 68 ? 48 89 70 ? 57 48 81 EC 80 00 00 00
```asm
.rdata:0000000006D32AF0 aAttemptToBlock db 'Attempt to blockcast with side length %f. The maximum side length'
.rdata:0000000006D32AF0                                         ; DATA XREF: sub_EC6B60+3A3↑o
.rdata:0000000006D32AF0                                         ; sub_EC6F50+126↑o
``` 

so the offset is 0xEC6F50


# WorldRoot_Raycast (or just normal raycast)

string "Raycast" exactly like that, same uppercasing nothing else, first xref
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

OR you can use the signature because im nice and i dont want to waste your time 48 8B C4 48 89 58 ? 48 89 70 ? 55 57 41 54 41 56 41 57 48 8D A8 ? ? ? ? 48 81 EC 80 04 00 00

so the offset is 0xEC5D60