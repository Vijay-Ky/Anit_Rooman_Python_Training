f = open("demofile.txt", "a")
f.write("Now the file is having more content!")
f.write("Now the file is having even more content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
