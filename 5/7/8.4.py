a = "Raining in the spring time. 미세먼지 안녕!"

print(a.replace("R", "r"), # Raining => raining
a.replace("ing",""), # Raining, spring => Rain, spr
a.replace("!",".")) #안녕! => 안녕.
b = a.replace("time","tiempo")
print(b) # b = "Raining in the spring tiempo. 미세먼지 안녕!"
print(a.replace("안녕!","Bye!")) # "Raining in the spring time. 미세먼지 Bye!"