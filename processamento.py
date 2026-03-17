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

def MelhorMedia(listas_medias):
    top_student = ""
    maior_media = 0
    for nome, notas, media in listas_medias:
        if media > maior_media:
            maior_media = media
            top_student = nome
    
    return top_student,maior_media

def MediaEBaixa(lista_media):
    lista_com_categoria = []
    for nome, notas, media in lista_media:
        if media < 7:
            categoria = 'REPROVADO'
        else:
            categoria = 'APROVADO'
        lista_com_categoria.append((nome, notas, media, categoria))
    return lista_com_categoria

