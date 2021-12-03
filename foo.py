import os

from enum import Enum

class LineEnding(Enum):
    LF = 1
    CRLF = 2
    CR = 3

def file_lineEnding(file_name):
    with open(file_name, "rb") as inp:
        while True:
            b = inp.read(1)
            print(f"looking at '{b}'")
            if b == b'':
                return None
            elif b == b'\r':
                b2 = inp.read(1)
                print(f"found CR, now looking at '{b2}'")
                if b2 == b'\n':
                    return LineEnding.CRLF
                else:
                    return LineEnding.CR
            elif b == b'\n':
                return LineEnding.LF

def test():
    for file in [ "qc-lf.txt", "qc-crlf.txt", "qc-cr.txt", "other" ]:
        path = os.path.join("examples", file)
        print(f"== File '{path}': ==")
        print(file_lineEnding(path))

if __name__ == "__main__":
    test()
