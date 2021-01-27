import random
class User:
    def __init__(self):

    mind = {}
    life = 10
    dominanta = []

    def save_post(self, result):
        self.mind.add(result)
    #def public_post(self):

    def choose_post(self, timeline):#Порівняння вподобань користувача з
        result = " "
        choose = random.random(0,global timeline.count())
        return choose




class Instance:#Інстанс
    def __init__(self, userlist):
        self.userlist = userlist#Список користувачів

    inp = " "
    def search_user(self, text):  # Пошук користувача, повідомляє чи успішно
        if text in self.userlist:
            # print("user present")
            return True
        else:
            # print("user not present")
            return False

    def add_user(self):
        self.inp = input("Enter username:")

        if not self.search_user(self.inp):
            self.userlist.append(self.inp)
            print(self.inp + " added")
        else:
            print(self.inp + " not added")

    def remove_user(self):
        self.inp = input("Enter username:")

        if self.search_user(self.inp):
            self.userlist.remove(self.inp)
            print(self.inp + " removed")
        else:
            print(self.inp + " not removed")

    def get_list(self):
        print(self.userlist)

    def call(self):
        while True:
            inp = input("enter command:")
            if inp == "show":
                self.get_list()
            if inp == "add":
                self.add_user()
            if inp == "remove":
                self.remove_user()
            if inp == "run":
                for i in self.userlist:
                    i.call()
            if inp == "end":
                break

timeline = ["con1", "con2", "con3"]
userlist = ["Vasa", "Vova", "Masha"]

instance1 = Instance(timeline, userlist)
instance1.call()
