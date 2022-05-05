class Cat:
    def __init__ (self , name , age,  weight ):
      self.name = name
      self.age = age
      self.weight = weight
      print(f"[КОТ] : {name} \n[возраст] : {age} \n[ВЕС] : {weight} ")
    def live(self, new_age):
        new_age = self.age + 1 #повзрослел на 1 день
        self.age = new_age    
    def eat(self, new_weight):
        new_weight = self.weight + 1 #поправился
        self.weight = new_weight
    def walk(self, new_weight):
         new_weight = self.weight - 1 #похудел
         self.weight = new_weight


vasya = Cat("Vasya" , 20, 3)
x = 1
while x <= 5: #пять дней жизни кота
    x += 1
    user_choise = input ("Гулять (W) или Eсть (E) ?     ")
    if user_choise == "W" or user_choise == "w":
        vasya.live("new_age")
        vasya.walk("new_weight")
    if user_choise == "E" or user_choise == "e":
        vasya.live("new_age")
        vasya.eat("new_weight")

    print(f"[КОТ] : {vasya.name} \n[возраст] : {vasya.age} \n[ВЕС] : {vasya.weight} ")