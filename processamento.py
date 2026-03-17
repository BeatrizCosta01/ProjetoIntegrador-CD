dados_alunos = [
    ("Ana Silva", [8.5, 9.0, 7.5, None]),
    ("Bruno Oliveira", [6.0, 5.5,"#", 7.0]),
    ("Carla Souza", [10.0, 9.5, 10.0]),
    ("Diego Santos", [4.5, 6.0, 5.0]),
    ("Elena Costa", [8.0, 8.0, 8.5])
]

def FiltroDeInconformidades(lista_notas):
    if not isinstance(lista_notas, list) or not lista_notas:
        print("Erro: A lista de notas está vazia ou não é uma lista válida.")
        return False

    for nota in lista_notas:
        if not isinstance(nota, (int, float)):
            print(f"Erro: Dado corrompido encontrado (não numérico): {nota}")
            return False
        if not (0 <= nota <= 10):
            print(f"Erro: Nota fora do intervalo (0-10): {nota}")
            return False

    print("Lista de notas válida.")
    return True

FiltroDeInconformidades(dados_alunos)