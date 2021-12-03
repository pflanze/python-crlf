import os

def file_is_using_crlf(file_name):
    with open(file_name, "rb") as inp:
        while True:
            b = inp.read(1)
            print(f"looking at '{b}'")
            if b == b'':
                return False
            elif b == b'\r':
                b2 = inp.read(1)
                print(f"found CR, now looking at '{b2}'")
                if b2 == b'\n':
                    return True
                else:
                    return False
            elif b == b'\n':
                return False

for file in [ "qc-lf.txt", "qc-crlf.txt", "qc-cr.txt", "other" ]:
    path = os.path.join("examples", file)
    print(f"== File '{path}': ==")
    print(file_is_using_crlf(path))
