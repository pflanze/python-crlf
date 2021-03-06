import os
import codecs

from enum import Enum

class LineEnding(Enum):
    LF = 1
    CRLF = 2
    CR = 3
    Mixed = 4

warnings=False

def note(v):
    if warnings:
        print(v)
    

def stream_lineEndings(inp):
    while True:
        b = inp.read(1)
        note(f"looking at '{b}'")
        if b == '':
            return None
        elif b == '\r':
            b2 = inp.read(1)
            note(f"found CR, now looking at '{b2}'")
            if b2 == '\n':
                yield LineEnding.CRLF
            else:
                yield LineEnding.CR
        elif b == '\n':
            yield LineEnding.LF

def file_lineEndings(file_name):
    with open(file_name, "r", newline="") as inp:
        return stream_lineEndings(inp)

def stream_lineEnding(inp):
    endings = stream_lineEndings(inp)
    try:
        first = endings.__next__()
        for e in endings:
            if e != first:
                return LineEnding.Mixed
        return first
    except StopIteration:
        return None

def file_lineEnding(file_name):
    with open(file_name, "r", newline="") as inp:
        return stream_lineEnding(inp)


def test():
    global warnings
    # warnings=True
    errors=0
    for (file, expected) in [
            ("lf.txt", LineEnding.LF),
            ("crlf.txt", LineEnding.CRLF),
            ("cr.txt", LineEnding.CR),
            ("mixed.txt", LineEnding.Mixed),
            ("other", None)
    ]:
        path = os.path.join("examples", file)

        print(f"== File '{path}': ==")
        res = file_lineEnding(path)
        if res == expected:
            print("Ok.")
        else:
            print(f"FAILURE: expected {expected}, got {res}.")
            errors += 1

        print(f"  and with codecs.open:")
        with codecs.open(path,
                         encoding='utf-8', 
                         # errors='strict'
                         ) as stream:
            res = stream_lineEnding(stream)
        if res == expected:
            print("Ok.")
        else:
            print(f"FAILURE: expected {expected}, got {res}.")
            errors += 1
        
    warnings=False
    print(f"=> {errors} failure(s).")
    if errors:
        exit(1)

if __name__ == "__main__":
    test()
