def inversao(s):
    invertida = ""
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

string = input("Digite uma string para inverter: ")
print(f"String invertida: {inversao(string)}")
