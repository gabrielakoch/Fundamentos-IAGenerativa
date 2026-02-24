def classificar_mensagem(mensagem, temperature=0.2):
    prompt = f"""
    Classifique a mensagem abaixo em uma das seguintes categorias:
    suporte, vendas, financeiro ou outros.

    Avalie o seu nível de certeza nessa classificação e dê um score de confiança de 0 a 100.

    Retorne APENAS um JSON estrito neste formato:
    {{
        "categoria": "nome_da_categoria",
        "confianca": 95
    }}

    Mensagem: "{mensagem}"
    """
    
    # Aqui chama a função do llm_client para gerar a resposta
    from llm_client import gerar_resposta
    return gerar_resposta(prompt, temperature)