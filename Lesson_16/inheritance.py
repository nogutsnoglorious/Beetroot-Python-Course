class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def run(self):
        print("Mammal runs")
    
    def sleep(self):
        print("Mammal sleeps")

class Bird(Animal):
    def fly(self):
        print("Bird flies")
    
class Bat(Mammal, Bird):
    def echolocate(self):
        print("Bat uses echolocation")