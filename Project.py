print("""
                      ^^^^^^^^^^^^^^^^^^^^^^^^Program Ruch Zmienny^^^^^^^^^^^^^^^^^^^^^^^^
                                 Postępuj zgodnie z instrukcjami podanymi na ekranie
             #################################### MENU GLówne ####################################
                                          Wybierz opcje 1 , 2 lub 3 
""")
opcje_menu = ["1 - Ruch z tarciem", "2 - Ruch bez tarcia", "3 - Zamknij Program"]
menu1 = ["1 - Predkość końcowa (Vk)", "2 - Czas(t)", "3 - Powrót do głównego menu"]
menu2 = ["1 - Predkość końcowa (Vk)", "2 - Czas(t)", "3 - Powrót do głównego menu"]
#Funkcje do pierwszego wyboru

# def tarcie_vk()
# def tarcie_t()

#Funkcje do drugiego wyboru

# def tarcie_vk()
# def tarcie_t()


while True:
    for i in opcje_menu:
        print(i)
    print()
    user_in = input("Wybierz twoja opcje"
                    "")
    if user_in.upper() == "1":
        for i in menu1:
            print(i)
        print()
        user_in1 = input("RUCH Z TARCIEM\n"
                         "&&& Wybierz co chcesz policzyć &&&\n"
                         "")
        if user_in1.upper() == "1":
            tarcie_vk()
        elif user_in1.upper() == "2":
            tarcie_t()
        elif user_in1.upper() == "3":
            continue
        else:
            print("To nie jest dobra opcja\n"
                  "Wybierz ponownie lub powróc do menu głównego\n"
                  "")
    elif user_in.upper() == "2":
        for i in menu2:
            print(i)
        print()
        user_in2 = input("RUCH BEZ TARCIA\n"
                         "&&& Wybierz co chcesz policzyć &&&\n"
                         "")
        if user_in2.upper() == "1":
            vk()
        elif user_in2.upper() == "2":
            t()
        elif user_in2.upper() == "3":
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
