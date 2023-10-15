# 1

def tetranachi_cache(func):
    cache = {}
    def inner(*args, **kwargs):
        try:
            return cache[args[0]]
        except:
            cache[args[0]] = func(args[0])
            return cache[args[0]]
    return inner

@tetranachi_cache
def tetranacci(n):
    if n == 1 or n == 2 or n == 3:
        return 0
    if (n == 4):
        return 1
    return tetranacci(n - 1) + tetranacci(n - 2) + tetranacci(n - 3) + tetranacci(n - 4)

# 2

def repeat(obj, n = None):
    if n == None:
        while (True):
            yield obj
    counter = 0
    while counter < n:
        yield obj
        counter += 1

# 3 & 4

class Pojazd:
    def __init__(self, predkosc_max, przebieg, model, miejsca):
        self.przebieg = przebieg
        self.predkosc_max = predkosc_max
        self.model = model
        self.kolor = 'biały'
        self.miejsca = miejsca
        self.mnoznik = 100
    def liczba_miejsc(self):
        print(f'{self.model} pomieści {self.miejsca} osób')
    
    def oplata(self):
        return round(self.miejsca * self.mnoznik, 0)        

class Autobus(Pojazd):
    def liczba_miejsc(self):
        return super().liczba_miejsc()
    def oplata(self):
        if self.miejsca == 50:
            self.mnoznik *= 1.1
        return super().oplata()
    
# 5
import math

class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def wypisz(self):
        print(f'Funkcja {self.a} * x^2 + {self.b} * x + {self.c}')

    def oblicz_wartosc(self, x):
        return math.pow(x, 2) * self.a + self.b * x + self.c 

    def rozwiaz(self):
        if self.a == 0:
            if self.b == 0:
                print(f'Podano funkcję stałą x = {self.c}')
            elif self.c == 0:
                print('x wynosi zero!')
            else:
                print(f'Podano funkcję liniową {self.b} * x + {self.c} = 0')
                print(f'Rozwiązaniem jest x = {-self.c / self.b}')     
        else:
            delta = math.pow(self.b, 2) - 4 * self.a * self.c            
            if (delta > 0):
                pierwiastek_z_delty = math.sqrt(delta)
                print(f'x1 = {(-self.b - pierwiastek_z_delty) / 2 * self.a}')
                print(f'x2 = {(-self.b + pierwiastek_z_delty) / 2 * self.a}')
            elif delta == 0:
                print(f'x1 = x2 = {-self.b / 2 * self.a}')
            else:
                print('Funkcja kwadratowa nie ma postaci iloczynowej i nie ma miejsc zerowych w dziedzinie liczb rzeczywistych')


