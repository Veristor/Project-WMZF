from typing import List

import numpy as np
import matplotlib.pyplot as plt
vk=0
vp=0
F=0
t=0
m=0
n=0
g=0
a=0

print("""
                      ^^^^^^^^^^^^^^^^^^^^^^^^Program Ruch Zmienny^^^^^^^^^^^^^^^^^^^^^^^^
                                 Postępuj zgodnie z instrukcjami podanymi na ekranie
             #################################### MENU GLówne ####################################
                                          Wybierz opcje 1 , 2 lub 3 
""")
opcje_menu = ["1 - Ruch z tarciem", "2 - Ruch bez tarcia", "3 - Zamknij Program"]
menu1 = ["1 - Predkość początkowa (Vp) z wykresem V(t)", "2 - Prędkość końcowa (Vk) z wykresem V(t)","3 - Przyśpieszenie (a)","4 - Czas (t)","5 - Droga (s) z wykresem S(t)","6 - Powrót do głównego menu"]
menu2 = ["1 - Predkość początkowa (Vp) z wykresem V(t)", "2 - Prędkość końcowa (Vk) z wykresem V(t)","3 - Przyśpieszenie (a)","4 - Czas (t)","5 - Droga (s) z wykresem S(t)","6 - Powrót do głównego menu"]



#Funkcje do pierwszego wyboru

def tarcie_vp (vk, F, t, m, n, g):
        Tsim = []
        Vt = []
        Vp = vk - ((F - n * m * g) / m)
        for x in range(0, int(t * 10) + 1, 1):
            Vt.append(Vp + ((F - n * m * g) / m) * (x / 10))
            Tsim.append(float(x / 10))
        print("Prędkość początkowa:", Vp, "m/s")
        plt.plot(Tsim, Vt)
        plt.xlabel("Czas[s]")
        plt.ylabel("Predkosc[m/s]")
        plt.title("Wykres Funkcji")
        plt.show()
        return Vp

def tarcie_vk (vp,F,t,m,n,g):
    Tsim = []
    Vt = []
    Vk = vp+((F-n*m*g)/m)*t
    for x in range(0, int(t * 10) + 1, 1):
        Vt.append(Vk - ((F - n * m * g) / m) * (x / 10))
        Tsim.append(float(x / 10))
    print ("Prędkość końcowa:",Vk,"m/s")
    plt.plot(Tsim, Vt)
    plt.xlabel("Czas[s]")
    plt.ylabel("Predkosc[m/s]")
    plt.title("Wykres Funkcji")
    plt.show()
    return Vk

def tarcie_a (m,F,g,n) :
    return (F-n*m*g)/m

def tarcie_t (vp,vk,F,m,n,g):
    return ((vk-vp)*m)/(F-n*m*g)

def tarcie_s (vp,F,g,n,t,m) :
    Tsim = []
    St = []
    S= vp*t+0.5*((F-n*m*g)/m)*t**2
    for x in range(0, int(t * 10) + 1, 1):
        St.append((vp*x+0.5*((F-n*m*g)/m)*(x**2/10))/10)
        Tsim.append(float(x/ 10))
    print("Droga:", S, "m")
    plt.plot(Tsim, St)
    plt.xlabel("Czas[s]")
    plt.ylabel("Droga [m]")
    plt.title("Wykres Funkcji")
    plt.show()
    return S


def get_inputs1(user_in1,vk,F,t,m,n,g):
    if user_in1 == '1':
       while True:
          try:
                vk =float(input("Podaj prędkośc końcową (Vk): "))
                F = float(input("Podaj siłe ciągu "))
                if F<0:
                    print("Liczba F musi być dodatnia")
                    continue
                t = float(input("Podaj czas (t): "))
                if t<0:
                    print("Liczba t musi być dodatnia")
                    continue
                m = float(input("Podaj masę (m): "))
                if m<0:
                    print("Liczba m musi być dodatnia")
                    continue
                n = float(input("Podaj współczynnik tarcia (n): "))
                if n<0:
                    print("Liczba n musi być dodatnia")
                    continue
                g = float(input("Podaj przyśpieszenie ziemskie (g): "))
                if g<0:
                    print("Liczba g musi być dodatnia")
                    continue
          except ValueError:
              print("Musisz podać liczbę")
              continue
          else:
              return tarcie_vp(vk,F,t,m,n,g)

    elif user_in1 == '2':
        while True:
            try:
               vp = float(input("Podaj prędkośc początkową (Vp): "))
               if vp < 0:
                   print("Liczba vp musi być dodatnia")
                   continue
               F = float(input("Podaj siłe ciągu (F): "))
               t = float(input("Podaj czas (t): "))
               if t < 0:
                   print("Liczba t musi być dodatnia")
                   continue
               m = float(input("Podaj masę (m): "))
               if m < 0:
                   print("Liczba m musi być dodatnia")
                   continue
               n = float(input("Podaj współczynnik tarcia (n): "))
               if n < 0:
                   print("Liczba n musi być dodatnia")
                   continue
               g = float(input("Podaj przyśpieszenie ziemskie (g): "))
               if g < 0:
                   print("Liczba g musi być dodatnia")
                   continue
            except ValueError:
                print("Musisz podać liczbę")
                continue
            else:
               return tarcie_vk(vp,F,t,m,n,g)
    elif user_in1 == '3':
        while True:
            try:
               F = float(input("Podaj siłe ciągu (F): "))
               m = float(input("Podaj masę (m): "))
               if m < 0:
                   print("Liczba m musi być dodatnia")
                   continue
               n = float(input("Podaj współczynnik tarcia (n): "))
               if n < 0:
                   print("Liczba n musi być dodatnia")
                   continue
               g = float(input("Podaj przyśpieszenie ziemskie (g): "))
               if g < 0:
                   print("Liczba g musi być dodatnia")
                   continue
            except ValueError:
                print("Musisz podać liczbę")
                continue
            else:
                return tarcie_a(F,g,m,n)
    elif user_in1 == '4':
        while True:
            try:
                   vp = float(input("Podaj prędkośc początkową (Vp): "))
                   if vp < 0:
                       print("Liczba vp musi być dodatnia")
                       continue
                   F = float(input("Podaj siłe ciągu (F): "))
                   vk = float(input("Podaj prędkośc końcową (Vk): "))
                   m = float(input("Podaj masę (m): "))
                   if m < 0:
                       print("Liczba m musi być dodatnia")
                       continue
                   n = float(input("Podaj współczynnik tarcia (n): "))
                   if n < 0:
                       print("Liczba n musi być dodatnia")
                       continue
                   g = float(input("Podaj przyśpieszenie ziemskie (g): "))
                   if g < 0:
                       print("Liczba g musi być dodatnia")
                       continue
            except ValueError:
                print("Musisz podać liczbę")
                continue
            else:
             return tarcie_t,(vp,vk,F,m,n,g)
    elif user_in1 == '5':
      while True:
          try:
               vp = float(input("Podaj prędkośc początkową (Vp): "))
               if vp < 0:
                   print("Liczba vp musi być dodatnia")
                   continue
               F = float(input("Podaj siłe ciągu (F): "))
               t = float(input("Podaj czas (t): "))
               if t < 0:
                   print("Liczba musi t być dodatnia")
                   continue
               m = float(input("Podaj masę (m): "))
               if m < 0:
                   print("Liczba musi m być dodatnia")
                   continue
               n = float(input("Podaj współczynnik tarcia (n): "))
               if n < 0:
                   print("Liczba musi n być dodatnia")
                   continue
               g = float(input("Podaj przyśpieszenie ziemskie (g): "))
               if g < 0:
                   print("Liczba musi g być dodatnia")
                   continue
          except ValueError:
              print("Musisz podać liczbę")
              continue
          else:
            return tarcie_s(vp,F,t,m,n,g)
#Funkcje do drugiego wyboru


def vp2(vk, a, t):
    Tsim=[]
    Vt=[]
    Vp = vk - a*t
    for x in range(0,int(t*10)+1,1):
        Vt.append(Vp + a*(x/10))
        Tsim.append(float(x/10))
    print("Prędkość początkowa:", Vp, "m/s")
    plt.plot(Tsim,Vt)
    plt.xlabel("Czas[s]")
    plt.ylabel("Predkosc[m/s]")
    plt.title("Wykres Funkcji")
    plt.show()
    return Vp

def vk2 (vp,a,t):
    Tsim = []
    Vt = []
    Vk = vp + a*t
    for x in range(0, int(t * 10) + 1, 1):
        Vt.append(Vk - a * (x / 10))
        Tsim.append(float(x / 10))
    print("Prędkość końcowa:", Vk, "m/s")
    plt.plot(Tsim, Vt)
    plt.xlabel("Czas[s]")
    plt.ylabel("Predkosc[m/s]")
    plt.title("Wykres Funkcji")
    plt.show()
    return Vk
def a2 (vp,vk,t) :
    return (vk - vp)/t
def t2 (vp,vk,a):
    return (vk - vp)/a
def s2 (vp,a,t):
    Tsim = []
    St = []
    S = vp + vp*t + 0.5*a*t**2
    for x in range(0, int(t * 10) + 1, 1):
        St.append(vp + vp*x + 0.5*a*(x ** 2 / 10))
        Tsim.append(float(x / 10))
    print("Droga:", S, "m")
    plt.plot(Tsim, St)
    plt.xlabel("Czas[s]")
    plt.ylabel("Droga [m]")
    plt.title("Wykres Funkcji")
    plt.show()
    return S


def get_inputs2(user_in2) :
    if user_in2 == '1':
      while True:
          try:
                vk = float(input("Podaj prędkośc końcową (Vk): "))
                a = float(input("Podaj przyśpieszenie (a): "))
                t = float(input("Podaj czas (t): "))
                if t < 0:
                      print("Liczba musi t być dodatnia")
                      continue
          except ValueError:
              print("Musisz podać liczbę")
              continue
          else:
            return vp2(vk,a,t)
    elif user_in2 == '2':
        while True:
            try:
                   vp = float(input("Podaj prędkośc początkową (Vp): "))
                   if vp < 0:
                       print("Liczba vp musi być dodatnia")
                       continue
                   a = float(input("Podaj przyśpieszenie (a): "))
                   t = float(input("Podaj czas (t): "))
                   if t < 0:
                       print("Liczba musi t być dodatnia")
                       continue
            except ValueError:
                print("Musisz podać liczbę")
                continue
            else:
               return vk2(vp,a,t)
    elif user_in2 == '3':
        while True:
            try:

                   vp = float(input("Podaj prędkośc początkową (Vp): "))
                   if vp < 0:
                       print("Liczba vp musi być dodatnia")
                       continue
                   vk = float(input("Podaj prędkośc końcową (Vk): "))
                   t = float(input("Podaj czas (t): "))
                   if t < 0:
                       print("Liczba musi t być dodatnia")
                       continue
            except ValueError:
                print("Musisz podać liczbę")
                continue
            else:
                return a2(vp,vk,t)
    elif user_in2 == '4':
        while True:
            try:
               vp = float(input("Podaj prędkośc początkową (Vp): "))
               if vp < 0:
                   print("Liczba vp musi być dodatnia")
                   continue
               a = float(input("Podaj przyśpieszenie (a): "))
               vk = float(input("Podaj prędkośc końcową (Vk): "))
            except ValueError:
                continue
            else:
                return t2(vp,vk,a)
    elif user_in2 == '5':
        while True:
            try:
                   vp = float(input("Podaj prędkośc początkową (Vp): "))
                   if vp < 0:
                       print("Liczba vp musi  być dodatnia")
                       continue
                   a = float(input("Podaj przyśpieszenie (a): "))
                   t = float(input("Podaj czas (t): "))
                   if t < 0:
                       print("Liczba t musi być dodatnia")
                       continue
            except ValueError:
                    print ("Musisz podać liczbę")
            else:
                return s2(vp,a,t)



while True:
    for i in opcje_menu:
        print(i)
    print()
    user_in = input("Wybierz twoja opcje"
                    "\n")
    if user_in.upper() == "1":
        for i in menu1:
            print(i)
        print()
        user_in1 = input("RUCH Z TARCIEM\n"
                         "&&& Wybierz co chcesz policzyć &&&\n"
                         "")
####################
        if user_in1 == "1":
            vp = get_inputs1(user_in1,vk,F,t,m,n,g)
        elif user_in1 == "2":
            vk = get_inputs1(user_in1,vk,F,t,m,n,g)
        elif user_in1 == "3":
            a = get_inputs1(user_in1,vk,F,t,m,n,g)
            print("Przyśpieszenie:", a, "m/s**2")
        elif user_in1 == "4":
            t = get_inputs1(user_in1,vk,F,t,m,n,g)
            print("Czas:", tarcie_t, "s")
        elif user_in1 == "5":
            s = get_inputs1(user_in1,vk,F,t,m,n,g)
        elif user_in1 == "6":
            continue
        else:
            print("To nie jest dobra opcja\n"
                  "Wybierz ponownie lub powróc do menu głównego\n"
                  "")
###################
    elif user_in.upper() == "2":
        for i in menu2:
            print(i)
        print()
        user_in2 = input("RUCH BEZ TARCIA\n"
                         "&&& Wybierz co chcesz policzyć &&&\n"
                         "")
        ####################
        if user_in2 == "1":
            vp2 = get_inputs2(user_in2)
        elif user_in2 == "2":
            vk2 = get_inputs2(user_in2)
        elif user_in2 == "3":
            a2 = get_inputs2(user_in2)
            print("Przyśpieszenie:", a2, "m/s**2")
        elif user_in2 == "4":
            t2 = get_inputs2(user_in2)
            print("Czas:", t2, "s")
        elif user_in2 == "5":
            s2 = get_inputs2(user_in2)
        elif user_in2 == "6":
            continue
        else:
            print("To nie jest dobra opcja\n"
                  "Wybierz ponownie lub powróc do menu głównego\n"
                  "")
    elif user_in.upper() == "3":
        break
    else:
        print("To nie jest dobra opcja\n"
              "Wybierz ponownie lub zakończ program (3)\n"
              "")
