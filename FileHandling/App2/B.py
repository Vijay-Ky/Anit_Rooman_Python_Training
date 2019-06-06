f = open("demofile.txt", "w")
f.write("Now the file is Overritten")
f.write("Now the file is Overritten one more time!")
f.close()

f = open("demofile.txt", "w")
f.write("Now the file is newly Overritten!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
