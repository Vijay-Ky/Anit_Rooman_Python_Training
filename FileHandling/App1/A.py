#open()
#"r" - Read -
#"a" - Append -
#"w" - Write -
#"x" - Create -

#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

# f = open("demofile.txt") or f = open("demofile.txt", "rt")

f = open("demofile.txt", "r")
print(f.read())
