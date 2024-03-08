def calculer(first, second):
    if first == "" or second == "":
        final_text = "text nu este corect"
        return final_text
    semn = input("introduceti +, -, /, * ")
    result = 0
    if semn == "+":
        result = first + second
    elif semn == "-":
        result = first - second
    elif semn == "/":
        result = int(first / second)
    elif semn == "*":
        result = first * second
    else:
        print("fuck of it is not a sign")



def operation():
    pizda_1 = ""
    pizda_2 = ""

    try:
        pizda_1 = int(input(":"))
        print("pizda_1 este un număr întreg:", pizda_1)

    except ValueError as e:
        print("Eroare:", e)
        operation()

    try:
        pizda_2 = int(input(":"))
        print("pizda_2 este un număr întreg:", pizda_2)
    except ValueError as e:
        print("Eroare:", e)
        operation()


    print(calculer(pizda_1, pizda_2))


operation()
