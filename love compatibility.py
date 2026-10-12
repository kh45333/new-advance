palabra = "true"
palabras = "love"

def calculate_love_score(oname, sname, lvalue=0, tvalue=0):
    for i in range(len(oname)):
        for j in range(len(palabra)):
            if palabra[j] == oname[i]:
                tvalue += 1
    for i in range(len(sname)):
        for j in range(len(palabra)):
            if palabra[j] == sname[i]:
                tvalue += 1
    for i in range(len(oname)):
        for j in range(len(palabras)):
            if palabras[j] == oname[i]:
                lvalue += 1
    for i in range(len(sname)):
        for j in range(len(palabras)):
            if palabras[j] == sname[i]:
                lvalue += 1
    print(f"{tvalue}{lvalue}% compatibility")

calculate_love_score("tatao", "tatrume")

