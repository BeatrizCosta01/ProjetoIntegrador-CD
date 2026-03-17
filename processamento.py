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

def CalculoMedia(lista_limpa):
    lista_com_media = []
    
    for nome, notas in lista_limpa:
        media = sum(notas) / len(notas) if len(notas) > 0 else 0
        lista_com_media.append((nome, notas, media))
        
    return lista_com_media

