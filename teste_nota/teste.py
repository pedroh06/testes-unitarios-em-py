def func(alunoNotas):

    listaAceita = True
    for nota in alunoNotas:
        if isinstance(alunoNotas, (int, float)):
            listaAceita = False
    
    if listaAceita:
        acumulador = 0
        for nota in alunoNotas:
            acumulador += nota
        mediaNotas = float(acumulador/len(alunoNotas))

        return print(mediaNotas)
    else:
        return print("Error: insira valores válidos")

func([4, 1, 5, 10, 7])