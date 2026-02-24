import json
from classifier import classificar_mensagem

# Nossas mensagens de teste
mensagens = [
    "Meu computador não liga de jeito nenhum.",
    "Quero comprar a licença corporativa para 50 usuários.",
    "Fui cobrado duas vezes na minha fatura deste mês.",
    "Qual é o horário de funcionamento de vocês?"
]

# A gaveta onde vamos medir a distribuição
distribuicao = {"suporte": 0, "vendas": 0, "financeiro": 0, "outros": 0}

print("Iniciando a classificação e gerando log...\n")

# Isso cria e abre um arquivo de texto para o nosso Log
with open("auditoria_log.txt", "w", encoding="utf-8") as arquivo_log:
    arquivo_log.write("--- LOG DE AUDITORIA DO SISTEMA ---\n\n")

    for msg in mensagens:
        # 1. Pede para a IA classificar
        resposta_texto = classificar_mensagem(msg, temperature=0.2)
        
        # 2. Converte o texto da IA para um formato que o Python entende
        try:
            dados = json.loads(resposta_texto)
            categoria_escolhida = dados.get("categoria", "outros").lower()
            confianca = dados.get("confianca", 0)
        except:
            categoria_escolhida = "outros"
            confianca = 0
            
        # 3. Mede a distribuição (soma +1 na categoria certa)
        if categoria_escolhida in distribuicao:
            distribuicao[categoria_escolhida] += 1
        else:
            distribuicao["outros"] += 1

        # 4. Escreve o resultado no arquivo de Log e mostra na tela
        resultado = f"Mensagem: '{msg}'\nCategoria: {categoria_escolhida} | Confiança: {confianca}%\n\n"
        arquivo_log.write(resultado)
        print(resultado)

    # No final, escreve o balanço da distribuição no log
    resumo_distribuicao = f"--- RESULTADO DA DISTRIBUIÇÃO ---\n{json.dumps(distribuicao, indent=4)}"
    arquivo_log.write(resumo_distribuicao)
    print(resumo_distribuicao)