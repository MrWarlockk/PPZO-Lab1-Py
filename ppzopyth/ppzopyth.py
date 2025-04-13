
def calcFunc():
    while True:
        try:
            numb1 = float(input("Podaj pierwsza liczbe: "))
            break;
        except ValueError:
            print("Nieprawidlowa wartosc. Podaj liczbe: ")

    while True:
        try:
            numb2 = float(input("Podaj druga liczbe: "))
            break;
        except ValueError:
            print("Nieprawidlowa wartosc. Podaj liczbe: ")

    while True:
        print("Podaj dzialanie ktore chcesz wykonac: ")
        print("+: Dodawanie")
        print("-: Odejmowanie: ")
        print("*: Mnozenie")
        print("/: Dzielenie")

        operationChoice = input("Wybor: ")

        if(operationChoice == "+" or operationChoice == "-" or operationChoice == "*" or operationChoice == "/"):
            break;
        else:
            print("Nieprawidlowy input, podaj prawidlowy symbol.")

    if (operationChoice == "+"):
        return numb1+numb2;
    elif (operationChoice == "-"):
        return numb1-numb2;
    elif (operationChoice == "*"):
        return numb1*numb2;
    elif (operationChoice == "/"):
        if (numb2 == 0):
            return None;
        return numb1/numb2;


def temperFunc():

    while True:
        print("Podaj jednostke wejsciowa: ")
        print("C: Zamiana stopni Celciusza na Fahrenheit ")
        print("F: Zamiana stopni Fahrenheit na Celciusza ")

        conversionChoice = input("Wybor: ")
        if(conversionChoice == "c" or conversionChoice == "C" or conversionChoice == "f" or conversionChoice == "F"):
            while True:
                try:
                    degreeValue = float(input("Podaj ilosc stopni: "))
                    break;
                except ValueError:
                    print("Nieprawidlowa wartosc, podaj liczbe.")

            if(conversionChoice == "c" or conversionChoice == "C"):
                return ((degreeValue * 1.8) + 32);
                
            elif(conversionChoice == "f" or conversionChoice == "F"):
                return ((degreeValue - 32) / 1.8);

            else:
                print("Nieprawidlowy input")
                return None;
        else:
            print("Nieprawidlowa jednostka, podaj poprawna.")

while True:
    choiceMain = input("Input(1: Zadanie 1, 2: Zadanie 2, 3: Zadanie 3, pozostale symbole wyjscie z konsoli): ")
    if(choiceMain == "1"):

        resultCalc = calcFunc()

        if (resultCalc != None):
            print(f"Wynik to: {resultCalc}")
        else:
            print("Nie mozna dzielic przez 0")

    elif(choiceMain == "2"):

        temperFuncRet = temperFunc()

        if (temperFuncRet != None):
            print(f"Wynik to: {temperFuncRet}")
        else: print("Wystapil blad")
    else:
        break;


