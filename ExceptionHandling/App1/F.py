try:
  f = open("demofile.txt", "w")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
   f.close()
