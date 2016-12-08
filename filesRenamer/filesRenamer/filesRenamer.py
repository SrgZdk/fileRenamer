import os
import hashlib
for filename in os.listdir("."):
    if not filename.endswith(".py"):
        hasher = hashlib.sha1()
        with open(filename, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
            print(hasher.hexdigest())
        os.rename(filename,hasher.hexdigest() + " string " + filename)
