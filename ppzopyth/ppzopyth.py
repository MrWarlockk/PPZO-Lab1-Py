
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

while True:
    choiceMain = input("Input(1: Zadanie 1, pozostale symbole wyjscie z konsoli): ")
    if(choiceMain == "1"):

        resultCalc = calcFunc()

        if (resultCalc != None):
            print(f"Wynik to: {resultCalc}")
        else:
            print("Nie mozna dzielic przez 0")
    else:
        break;


