# 作者：童鼎
qiang = int(input('枪的技巧:'))
qiang = qiang*0.3
fa = int(input('法师技巧'))
fa = (fa+qiang)*0.25
ji = int(input('祭祀的技巧'))
ji = (ji+qiang)*1.3+fa
print(ji*0.25)