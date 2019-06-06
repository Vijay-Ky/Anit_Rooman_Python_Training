import os
if os.path.exists("otherfile.txt"):
    os.remove("otherfile.txt")
else:
    print("The file does not exists")
