# Line separator detection library

This reports what kind of line separator is used in a file or stream.

## Details

`read(1)` is used in a loop; this has the advantage (compared with
iterating over the file stream) that it guarantees to retrieve single
characters, i.e. `stream_lineEnding` works even if the iterator would
return larger strings like lines instead of single characters (which
is important when using `codecs.open` instead of standard `open`--the
latter supports a `newline=""` argument to split on characters, the
former doesn't).

## Performance

`strace` on Linux confirms that the input is buffered (using `read(1)`
thus seems fine):

    read(3, "Hi\nThere\n", 4096)            = 9

The file is being streamed, not read into memory, thus memory usage
stays low.
