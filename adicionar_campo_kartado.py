import json

def adicionar_campo(formulario_add, campo_novo):
    if formulario_dict["formulario"]:
        maior_id = max(campo["id"] for campo in formulario_add["formulario"])
    else:
        maior_id = 0

    novo_id = maior_id + 1

    campo_novo_com_id = {"id": novo_id, **campo_novo}

    formulario_add["formulario"].insert(0, campo_novo_com_id)

    return formulario_add

import json

# formulario_add = { "formulario": [] }
with open("formulario_kartado.json", "r", encoding="utf-8") as f:
    formulario_add = json.load(f)

campo_novo = {
    "displayName": "Material",
    "apiName": "material",
    "dataType": "string"
}

formulario_atualizado = adicionar_campo(formulario_dict, campo_novo)

# Agora salva o formulário atualizado com o novo campo
with open("formulario_atualizado.json", "w", encoding="utf-8") as f:
    json.dump(formulario_atualizado, f, indent=2, ensure_ascii=False)

print(json.dumps(formulario_atualizado, indent=2, ensure_ascii=False))
