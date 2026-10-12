# dumpgco

search for string `"\"0\":{\"type\":\"userdata\",\"cat\":0,\"size\":0}\n"`, first xref decompile:

```c
  sub_2728B70(a1, a2, a3: sub_27261C0); // <-- double click the second rva, so in this case sub_27261C0
  sub_7BC160(a1: a2, a2: "\"0\":{\"type\":\"userdata\",\"cat\":0,\"size\":0}\n"); // <-- you're here
```

so the offset is sub_27261C0

sig: 48 89 5C 24 ? 57 48 83 EC 20 48 8D 15

<details>

<summary><b>verify</b></summary>


3 args

```c
char __fastcall sub_25C70E0(FILE *Stream, __int64 a2, const void *a3)
{
  sub_705140(a1: Stream, a2: "\"%p\"", a3);
  fputc(Character: 58, Stream);
  sub_25C6C20(Stream);
  fputc(Character: 44, Stream);
  fputc(Character: 10, Stream);
  return 0;
}
```

  
</details>
