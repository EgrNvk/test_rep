class Vodoem:
   vodoem_list = []
   def __init__(self , name , solt_or_fresh):
      self.name = name
      self.solt_or_fresh = solt_or_fresh
      Vodoem.vodoem_list.append(self)
   def __str__(self):
        return f'{self.name}, {self.solt_or_fresh}'
class Fish:
   fish_list = []
   def __init__(self , name , solt_or_fresh):
      self.name = name
      self.solt_or_fresh = solt_or_fresh
      Fish.fish_list.append(self)
   def __str__(self):
        return f'{self.name}, {self.solt_or_fresh}'
black_sea = Vodoem ("Черное море", "solt")
azov_sea = Vodoem ("Азовское море", "solt")
rDnipro = Vodoem ("река Днепр","fresh")
rSamara = Vodoem ("река Самара","fresh")
oBlue = Vodoem ("Голубое озеро","fresh")
oSoltLiman = Vodoem ("озеро Соленый лиман","solt")
karas = Fish ("Карась", "fresh")
schuka = Fish ("Щука", "fresh")
kambala = Fish ("Камбала", "solt")
katran = Fish("Катран","solt")
print("Водоемы Украины")
print("________________________")
x = 0
while x<=5:
   print(Vodoem.vodoem_list[x])
   x += 1
print("************************")
print("Рыбы Украины")
print("________________________")
y = 0
while y <= 3:
   print(Fish.fish_list[y])
   y += 1
### основная часть
x=0 
while x <= 5:
   v = Vodoem.vodoem_list[x].solt_or_fresh
   y = 0
   while y <= 3:
      f = Fish.fish_list[y].solt_or_fresh
      if v == f:
         print("В ", Vodoem.vodoem_list[x].name, "может жить ", Fish.fish_list[y].name)
      y += 1
   x += 1