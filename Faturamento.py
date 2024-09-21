import json


fmensal = {
    "faturamento": [1350, 255, 120, 3000, 0, 0, 1500, 2700, 0, 2100, 0, 2200, 4600, 0]
}

Validacao = [dia for dia in fmensal['faturamento'] if dia > 0]


Menor= min(Validacao)
Maior= max(Validacao)
Media = sum(Validacao) / len(Validacao)

DiasMedia = len([dia for dia in Validacao if dia > Media])

print(f"Menor faturamento: R${Menor}")
print(f"Maior faturamento: R${Maior}")
print(f"Dias acima da média: {DiasMedia}")
