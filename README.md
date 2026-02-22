# SECURE-SYSTEMS

### 📌 Descrição (até 350 caracteres)

Sistema de autenticação em Python que valida usuários a partir de um ficheiro JSON, registra tentativas de login em logs TXT e JSON, gera relatórios de acessos (sucesso e falha) e emite alertas quando há múltiplas tentativas inválidas. Simula um controle básico de segurança e monitoramento de acessos.

---

# 📘 README – Sistema de Autenticação e Logs

## 📖 Sobre o Projeto

Este projeto é um sistema simples de autenticação desenvolvido em Python. Ele verifica credenciais de usuários armazenadas em um ficheiro JSON e registra todas as tentativas de login, sejam bem-sucedidas ou não.

O sistema também gera relatórios automáticos com o total de tentativas, sucessos e falhas por usuário.

---

## ⚙️ Funcionalidades

* ✅ Validação de login com nome e senha
* ✅ Leitura de dados a partir de ficheiro JSON
* ✅ Registro de logs em:

  * `logs.txt`
  * `logs.json`
* ✅ Relatório automático de tentativas por usuário
* ✅ Alerta para mais de 5 falhas de login
* ✅ Organização automática de pastas

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* JSON
* Manipulação de arquivos
* Programação Orientada a Objetos (POO)

---

## 📂 Estrutura do Projeto

```
📁 Dados de usuarios/
   └── dados_user.json

📁 logs/
   ├── logs.txt
   └── logs.json

main.py
cores.py
```

---

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado.
2. Configure o ficheiro `dados_user.json` com os usuários.
3. Execute:

```bash
python main.py
```

---

## 📊 Exemplo de Relatório

O sistema exibirá no terminal algo como:

```
Usuario X tentou 7 vezes, logou 2 vezes, falhou 5 vezes
```

Caso o número de falhas seja superior a 5, será exibido um alerta de segurança.

---

