print("""
                      ^^^^^^^^^^^^^^^^^^^^^^^^Program Ruch Zmienny^^^^^^^^^^^^^^^^^^^^^^^^
                                 Postępuj zgodnie z instrukcjami podanymi na ekranie
             #################################### MENU GLówne ####################################
                                          Wybierz opcje 1 , 2 lub 3 
""")
opcje_menu = ["1 - Ruch z tarciem", "2 - Ruch bez tarcia", "3 - Zamknij Program"]
menu1 = ["1 - Predkość początkowa (Vp)", "2 - Prędkość końcowa (Vk)","3 - Przyśpieszenie (a)","4 - Czas (t)","5 - Droga (s)","6 - Powrót do głównego menu"]
menu2 = ["1 - Predkość początkowa (Vp)", "2 - Prędkość końcowa (Vk)","3 - Przyśpieszenie (a)","4 - Czas (t)","5 - Droga (s)","6 - Powrót do głównego menu"]
#Funkcje do pierwszego wyboru

def tarcie_vp(vk,F,t,m,n,g):
    return vk -((F-n*m*g)/m)*t

def tarcie_vk (vp,F,t,m,n,g):
    return vp+((F-n*m*g)/m)*t

def tarcie_a (m,F,g,n) :
    return (F-n*m*g)/m

def tarcie_t (vp,vk,F,m,n,g) :
    return ((vk-vp)*m)/(F-n*m*g)

def tarcie_s (vp,F,g,n,t,m) :
    return vp*t+0,5*((F-n*m*g)/m)*t**2

def get_inputs1(user_in1) :
    if user_in1 == '1':
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       F = int(input("Podaj siłe ciągu "))
       t = int(input("Podaj czas (t): "))
       m = int(input("Podaj masę (m): "))
       n = int(input("Podaj współczynnik tarcia (n): "))
       g = int (input("Podaj przyśpieszenie ziemskie (g): "))
       return tarcie_vp(vk,F,t,m,n,g)
    elif user_in1 == '2':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       F = int(input("Podaj siłe ciągu (F): "))
       t = int(input("Podaj czas (t): "))
       m = int(input("Podaj masę (m): "))
       n = int(input("Podaj współczynnik tarcia (n): "))
       g = int(input("Podaj przyśpieszenie ziemskie (g): "))
       return tarcie_vk(vp,F,t,m,n,g)
    elif user_in1 == '3':
       F = int(input("Podaj siłe ciągu (F): "))
       m = int(input("Podaj masę (m): "))
       n = int(input("Podaj współczynnik tarcia (n): "))
       g = int(input("Podaj przyśpieszenie ziemskie (g): "))
       return tarcie_a(F,g,m,n)
    elif user_in1 == '4':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       F = int(input("Podaj siłe ciągu (F): "))
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       m = int(input("Podaj masę (m): "))
       n = int(input("Podaj współczynnik tarcia (n): "))
       g = int(input("Podaj przyśpieszenie ziemskie (g): "))
       return tarcie_t(vp,vk,F,m,n,g)
    elif user_in1 == '5':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       F = int(input("Podaj siłe ciągu (F): "))
       t = int(input("Podaj czas (t): "))
       m = int(input("Podaj masę (m): "))
       n = int(input("Podaj współczynnik tarcia (n): "))
       g = int(input("Podaj przyśpieszenie ziemskie (g): "))
       return tarcie_s(vp,F,t,m,n,g)
#Funkcje do drugiego wyboru


def vp2(vk, a, t):
    return vk - a*t
def vk2 (vp,a,t):
    return vp + a*t
def a2 (vp,vk,t) :
    return (vk - vp)/t
def t2 (vp,vk,a):
    return (vk - vp)/a
def s2 (vp,a,t):
    return vp + vp*t + 0,5*a*t**2

def get_inputs2(user_in2) :
    if user_in2 == '1':
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       t = int(input("Podaj czas (t): "))
       return vp2(vk,a,t)
    elif user_in2 == '2':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       t = int(input("Podaj czas (t): "))
       return vk2(vp,a,t)
    elif user_in2 == '3':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       t = int(input("Podaj czas (t): "))
       return a2(vp,vk,t)
    elif user_in2 == '4':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       return t2(vp,vk,a)
    elif user_in2 == '4':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       t = int(input("Podaj czas (t): "))
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
            print("Aby wyliczyć prędkość początkową potrzebne są: predkość końcowa, przyśpieszenie oraz czas\n ")
            vp = get_inputs1(user_in1)
            print("Prękośc początkowa :", vp)
        elif user_in1 == "2":
            vk = get_inputs1(user_in1)
            print("Prędkośc końcowa :", vk)
        elif user_in1 == "3":
            a = get_inputs1(user_in1)
            print("Przyśpieszenie :", a,)
        elif user_in1 == "4":
            t = get_inputs1(user_in1)
            print("Czas :", t)
        elif user_in1 == "5":
            s = get_inputs1(user_in1)
            print("Droga :", s)
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
            print("Aby wyliczyć prędkość początkową potrzebne są: predkość końcowa, przyśpieszenie oraz czas\n ")
            vp2 = get_inputs2(user_in2)
            print("Prękośc początkowa :", vp2)
        elif user_in2 == "2":
            vk2 = get_inputs2(user_in2)
            print("Prędkośc końcowa :", vk2)
        elif user_in2 == "3":
            a2 = get_inputs2(user_in2)
            print("Przyśpieszenie :", a2)
        elif user_in2 == "4":
            t2 = get_inputs2(user_in2)
            print("Czas :", t2)
        elif user_in2 == "5":
            s2 = get_inputs2(user_in2)
            print("Droga :", s2)
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
