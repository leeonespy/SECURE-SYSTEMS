from datetime import datetime as dt
from cores import Cores as C
import os, json, time


class Usuarios:
    def __init__(self, nome, password):
        try:
            self.nome = nome
            self.password = password
            dados = self.carregar_dados()

            for user in dados:
                existe = False
                if user["Nome"] == self.nome and user["Password"] == self.password:
                    existe = True
                    print(C.negrito + C.verde + "Acesso Permitido!" + C.resetar)
                    break
            
            if existe == False:
                print(C.negrito + C.vermelho + "Acesso Negado (Nome ou Senha incorrecta)!" + C.resetar) 

            Sistema().seguranca(existe, self.nome)
                
        except(TypeError, IndexError, ValueError):
            print(C.negrito + C.vermelho + "ERRO No Sistema(class Usuarios)!" + C.resetar)

    def carregar_dados(self):
        os.makedirs("Dados de ususrios", exist_ok=True)
        try:
            with open("Dados de usuarios/dados_user.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                return dados
            return []
        except(FileExistsError, FileNotFoundError, json.decoder.JSONDecodeError):
            print("Erro no Ficheiro(dados_user.json)")
    

class Sistema:
    def __init__(self):
        pass
    
    def seguranca(self, verificacao, nome):
        if verificacao == True:
            self.salvar_logs_txt(nome, status="SUCESSO")
            self.salvar_logs_json(nome, status="SUCESSO")
        else:
            self.salvar_logs_txt(nome, status="FALHA")
            self.salvar_logs_json(nome, status="FALHA")
          

    def salvar_logs_txt(self, nome, status):
        try:
            date = dt.now().strftime("%d/%m/%Y %H:%M:%S")
            os.makedirs("logs", exist_ok=True)
            
            with open("logs/logs.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{date} | Usuario={nome} | Status={status}\n")
        except(FileExistsError, FileNotFoundError, json.decoder.JSONDecodeError):
            print("Erro no Ficheiro(salvar_logs_txt)")

    def carregar_logs_txt(self):
        try:
            with open("logs/logs.txt", "r", encoding="utf-8") as arquivo:
                logs = arquivo.read()
                print(logs)
        except(FileExistsError, FileNotFoundError, json.decoder.JSONDecodeError):
            print("Erro no Ficheiro(salvar_logs_txt)!")

    def carregar_logs_json(self):
        try:
            with open("logs/logs.json", "r", encoding="utf-8") as arquivo:
                logs = json.load(arquivo)
                return logs
            return []
        except(FileExistsError, FileNotFoundError, json.decoder.JSONDecodeError):
            return []

    def salvar_logs_json(self, nome, status):
        try:
            date = dt.now().strftime("%d/%m/%Y %H:%M:%S")
            new_dados = self.carregar_logs_json()
            dados = {
                "Data": date,
                "Usuario": nome,
                "Status": status
            }

            new_dados.append(dados)
            with open("logs/logs.json", "w", encoding="utf-8") as f:
                json.dump(new_dados, f, indent=4)

        except(FileExistsError, FileNotFoundError, json.decoder.JSONDecodeError):
            print("Erro no Ficheiro(salsalvar_logs_json)!")

    def total_de_tentativas_users(self):
        dados = self.carregar_logs_json()
        
        users = []
        for lista in dados:
            users.append((lista["Usuario"], lista["Status"]))
        self.relatorio(users)

    def relatorio(self, logs):
        relatorio = {}

        for usuario, status in logs:
            if usuario not in relatorio:
                relatorio[usuario] = {
                    "tentativas": 0,
                    "SUCESSO": 0,
                    "FALHA": 0
                }
            relatorio[usuario]["tentativas"] += 1
            if status == "SUCESSO":
                relatorio[usuario]["SUCESSO"] += 1
            else:
                relatorio[usuario]["FALHA"] += 1

        for usuario, dados in relatorio.items():
            print(C.azul_claro + f"    {usuario} " + C.resetar + C.amarelo_claro + f"tentou {dados['tentativas']} vezes, " + C.resetar + C.verde_claro + f"logou {dados['SUCESSO']} vezes, " + C.resetar + C.vermelho_claro + f"falhou {dados['FALHA']} vezes" + C.resetar + C.vermelho + f"{self.alerta(dados['FALHA'], usuario)}" + C.resetar)
            time.sleep(0.2) 

    def alerta(self, falhas, user):
        
        if falhas > 5:
            return f": (Alerta! Usuario {user} falhou mais de 5 vezes)"
        else:
            return ""

def main():
    print("          ======================Sistema Iniciado================\n")
    #Usuarios("Patricia2009", "kalakal")
    Sistema().total_de_tentativas_users()

if __name__== "__main__":
        main()
        
