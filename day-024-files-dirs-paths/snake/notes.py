class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print('Inhale')
        print('Exhale')

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print('Doing this underwater')

    def swim(self):
        print('Moving in water.')

nemo = Fish()
nemo.breathe()
print('-----------------')
nemo.swim()
print('-----------------')
print(nemo.eyes)