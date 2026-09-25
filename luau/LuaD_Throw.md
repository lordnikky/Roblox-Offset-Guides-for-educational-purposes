# LuaD_Throw

search for string "resulting string too large", first xref decompile:

```c
      }
    }
    sub_266EA40(a1, a2: 4u); // <-- LuaD_Throw
  }
  v42 = v12;
  if ( v9 > 0x40000000uLL / v12 )
  {
    v54 = off_71EDEB0;
    sub_26648D0(a1, a2: "resulting string too large"); // <-- you're here!!!!!!!!!!!!!
  }
  v51[2] = a1;
```

so the offset is 0x266EA40
