import json

############## CARREGAR CONTATOS ##############
lista_contatos = []
def carregar_contatos():
    with open("contatos.json", 'r') as f:
        return json.load(f)
############## CARREGAR CONTATOS ##############


############## SALVAR JSON ##############

def salvar_contatos(contatos):
    with open("contatos.json", 'w', encoding="utf-8") as j:
        json.dump(
            contatos,
            j,
            indent = 2,
            ensure_ascii= False
        )

############## SALVAR JSON ##############

############## ADICIONAR CONTATO NOVO ##############
def adicionar_contato(contatos,novo_contato):
    if not any (c["telefone"] == novo_contato["telefone"] for c in contatos):
        contatos.append(novo_contato)

############## ADICIONAR CONTATO NOVO ##############