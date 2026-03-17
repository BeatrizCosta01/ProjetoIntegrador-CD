def FiltroDeInconformidades(lista_completa):
    lista_limpa = []
    for nome, notas in lista_completa:
        notas_validadas = []
        for nota in notas:
            if isinstance(nota, (int, float)) and 0 <= nota <= 10:
                notas_validadas.append(nota)
            else:
                print(f"Aviso: Removendo dado inválido '{nota}' de {nome}")
        lista_limpa.append((nome, notas_validadas))
    
    return lista_limpa



