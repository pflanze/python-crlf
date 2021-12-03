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
    errors=0
    for (file, expected) in [
            ("qc-lf.txt", LineEnding.LF),
            ("qc-crlf.txt", LineEnding.CRLF),
            ("qc-cr.txt", LineEnding.CR),
            ("other", None)
    ]:
        path = os.path.join("examples", file)
        print(f"== File '{path}': ==")
        res = file_lineEnding(path)
        if res == expected:
            print("Ok.")
        else:
            print("FAILURE: expected {expected}, got {res}.")
            errors = errors + 1
    exit(errors)

if __name__ == "__main__":
    test()
