class Student:
    def __init__(self, name, surname, age, group, боблішко, money1, marks):
        self.name = name
        self.surname = surname
        self.age = age
        self.group = group
        self.боблішко = боблішко
        self.money1 = money1
        self.marks = marks

    def info(self):
        print(f"Student {self.name} {self.surname}")

    def dx(self):
        self.боблішко = float(input("Крутити бінанс:"))
        if (self.боблішко) < 500:
                print("Ти ЛОХ")
        elif (self.боблішко) > 1000:
            print("Добре")
        else:
            print("Не будь як Лебовський заробляй гроші нормаоьно а не будь боржником")
        print(f'боблішко = {self.боблішко}')
    def year(self):
        self.money1 = float(input("Заробиш:"))
        print(f'боблішко = {self.боблішко + self.money1 * 12 - 7565}')
        if (self.боблішко + self.боблішко * 12) > 12000:
            print("ЛОХ з великої букви XDDDD")
        else:
            print("ПОВНИЙ ЛОШАРА")
    def learn(self):
        global боблішко
        if 7 >= sum(self.marks) / len(self.marks) :
            int(self.боблішко-75012)
            return sum(self.marks) + 6
        elif 4 >= sum(self.marks) / len(self.marks) :
            self.боблішко-75012
            return sum(self.marks) / len(self.marks) + 6
    def average(self):
        return sum(self.marks) / len(self.marks)
student1 = Student("Стас", "Чікотіла", 14, "4-Б", 0, 0, [10, 12, 9, 11, 13])
student2 = Student("Де мої гроші", "Лебовський", 12, "Боржник", 0, 0, [3, 6, 2, 1, 5])
student1.info()
student1.dx()
student1.learn()
student1.year()
print(student1.average())
student2.info()
student2.dx()
student2.learn()
student2.year()
student2.dx()
