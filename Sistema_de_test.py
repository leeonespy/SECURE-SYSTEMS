from modulo_de_seguranca import Usuarios, Sistema
from cores import Cores as C
import random as rd 
import time, json


def carregar_users():
    with open("Dados de usuarios/dados_user.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        return dados
    return []

def users():
    n = []
    for nome in carregar_users():
        n.append(nome["Nome"])
    return n 

def passsword():
    p = []
    for passw in carregar_users():
        p.append(passw["Password"])
    return p

def logins_automatizado():
    vezes = 6
    while vezes:
        vezes -= 1
        Usuarios(rd.choice(users()), rd.choice(passsword()))

        time.sleep(0.2)

def tentativas():
    Sistema().total_de_tentativas_users()

def sistema_automatizado():
    try:
        while True:
            print("")
            print(C.negrito + C.sublinhado + C.azul_claro + "               ========SISTEMA AUTOMATIZADO=========                     " + C.resetar)
            print(C.amarelo + "\n Opções de testes disponiveis" + C.resetar)
            print(C.amarelo + " 1-Testar o sistema\n 2-Visualizar tentativas\n 3-Sair" + C.resetar)

            opcao = int(input("Digite uma das opções acima para continuar: "))
            print("")

            if opcao == 1:
                logins_automatizado()
            elif opcao == 2:
                tentativas()
            elif opcao == 3:
                break
            else:
                print(C.vermelho + "Error: Opção invalida!" + C.resetar)
    except(ValueError, TypeError, KeyError) as e:
        print(f"SYSTEM ERROR {e}")

sistema_automatizado()
