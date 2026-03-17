import processamento

dados_alunos = [
    ("Ana Silva", [8.5, 9.0, 7.5, None]),
    ("Bruno Oliveira", [6.0, 5.5,"#", 7.0]),
    ("Carla Souza", [10.0, 9.5, 10.0]),
    ("Diego Santos", [4.5, 6.0, 5.0]),
    ("Elena Costa", [8.0, 8.0, 8.5])
]

dadosLimpos = processamento.FiltroDeInconformidades(dados_alunos) 
print(processamento.CalculoMedia(dadosLimpos)) 


