# Line ending detection library

This is mostly meant as a template for teaching, possibly for
exploration, unlikely for actual future productive use.

## Analysis

To prevent Python from decoding and canonicalizing line endings and
thus preventing detection, binary mode is used for opening, which
means that byte strings are read instead of normal strings.

Currently `read(1)` is used and a loop. This doesn't hide the
underlying workings and is hence useful to explain the workings of,
but nicer code could probably be written using iterator based
operations (`drop_while`?).

### Efficiency

`strace` confirms that input is buffered:

    read(3, "Hi\nThere\n", 4096)            = 9

Thus `read(1)` seems fine.

### Correctness: TODO

 *  There's a problem in that some encodings could contain the byte
    values 10 and 13 as part of multi-byte character encodings, which
    would lead to bogus detection. What we need is having Python
    handle the charset decoding, yet leave alone the newline
    characters.

 *  Currently, it stops on the first detection. That can be sensible
    since if a mix of line endings is detected, what should it report
    as the correct one? But possibly what is wanted in this case is to
    literally report `LineEnding.MIXED`.

