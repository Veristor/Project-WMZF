print("""
                      ^^^^^^^^^^^^^^^^^^^^^^^^Program Ruch Zmienny^^^^^^^^^^^^^^^^^^^^^^^^
                                 Postępuj zgodnie z instrukcjami podanymi na ekranie
             #################################### MENU GLówne ####################################
                                          Wybierz opcje 1 , 2 lub 3 
""")
opcje_menu = ["1 - Ruch z tarciem", "2 - Ruch bez tarcia", "3 - Zamknij Program"]
menu1 = ["1 - Predkość początkowa (Vp)", "2 - Prędkość końcowa (Vk)","3 - Przyśpieszenie (a)","4 - Czas -(t)","5 - Droga (s)","6 - Powrót do głównego menu"]
menu2 = ["1 - Predkość początkowa (Vp)", "2 - Prędkość końcowa (Vk)","3 - Przyśpieszenie (a)","4 - Czas -(t)","5 - Droga (s)","6 - Powrót do głównego menu"]
#Funkcje do pierwszego wyboru

def tarcie_vp(vk, a, t):
    return vk - a*t

def tarcie_vk (vp,a,t):
    return vp + a*t

def tarcie_a (vp,vk,t) :
    return (vk - vp)/t

def tarcie_t (vp,vk,a) :
    return (vk - vp)/a

def tarcie_s (vp,a,t) :
    return vp + vp*t + 0,5*a*t**2

def get_inputs1(user_in1) :
    if user_in1 == '1':
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       t = int(input("Podaj czas (t): "))
       return tarcie_vp(vk,a,t)
    elif user_in1 == '2':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       t = int(input("Podaj czas (t): "))
       return tarcie_vk(vp,a,t)
    elif user_in1 == '3':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       t = int(input("Podaj czas (t): "))
       return tarcie_a(vp,vk,t)
    elif user_in1 == '4':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       return tarcie_t(vp,vk,a)
    elif user_in1 == '4':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       t = int(input("Podaj czas (t): "))
       return tarcie_s(vp,a,t)
#Funkcje do drugiego wyboru


def vp(vk, a, t):
    return vk - a*t
def vk (vp,a,t):
    return vp + a*t
def a (vp,vk,t) :
    return (vk - vp)/t
def t (vp,vk,a):
    return (vk - vp)/a
def s (vp,a,t):
    return vp + vp*t + 0,5*a*t**2

def get_inputs2(user_in2) :
    if user_in2 == '1':
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       t = int(input("Podaj czas (t): "))
       return vp(vk,a,t)
    elif user_in2 == '2':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       t = int(input("Podaj czas (t): "))
       return vk(vp,a,t)
    elif user_in2 == '3':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       t = int(input("Podaj czas (t): "))
       return a(vp,vk,t)
    elif user_in2 == '4':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       vk = int(input("Podaj prędkośc końcową (Vk): "))
       return t(vp,vk,a)
    elif user_in2 == '4':
       vp = int(input("Podaj prędkośc początkową (Vp): "))
       a = int(input("Podaj przyśpieszenie (a): "))
       t = int(input("Podaj czas (t): "))
       return s(vp,a,t)


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
            print("Przyśpieszenie :", a ,)
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
            vp = get_inputs2(user_in2)
            print("Prękośc początkowa :", vp)
        elif user_in2 == "2":
            vk = get_inputs2(user_in2)
            print("Prędkośc końcowa :", vk)
        elif user_in2 == "3":
            a = get_inputs2(user_in2)
            print("Przyśpieszenie :", a)
        elif user_in2 == "4":
            t = get_inputs2(user_in2)
            print("Czas :", t)
        elif user_in2 == "5":
            s = get_inputs2(user_in2)
            print("Droga :", s)
        elif user_in2 == "6":
            continue
        else:
            print("To nie jest dobra opcja\n"
                  "Wybierz ponownie lub powróc do menu głównego\n"
                  "")
        Ruchbeztarcia()
    elif user_in.upper() == "3":
        break
    else:
        print("To nie jest dobra opcja\n"
              "Wybierz ponownie lub zakończ program (3)\n"
              "")
