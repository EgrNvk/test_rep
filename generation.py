class Grandfathers:
    def method(self):
        print ("Дедушка Сергей и Бабушка Наташа, Дедушка Толя и Бабушка Катя")
class MomS(Grandfathers):   
    def method(self):
        super().method()
        print ("Мама Оксана")
class DadN(Grandfathers):
    def method(self):
        super().method()
        print ("Папа Толя")
class Son(DadN, MomS):
    def method(self):
        super().method()
        print ("Сын Егор")
Son().method()