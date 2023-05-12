a = 'python 4 ever&EVER 최고!'

print(a.find("E"), # 14
a.find("eve"), # 9
a.find("rev"), # -1
a.rfind("VER"), # 15
a.find(" "), # 6
a.rfind(" "), # 18 => 뒤에서부터 나오는 첫번쨰 위치는 앞에서 3번쨰 띄어쓰기 부분
a.find("최"), # 19
a.find("고!"), # 20
a.find("고최") )# -1