def func(alunoNotas):
    acumulador = 0
    for nota in alunoNotas:
        acumulador += nota
    mediaNotas = float(acumulador/len(alunoNotas))

    return mediaNotas


def test_answer():
    notas = [7, 8, 3, 4, 9]
    assert func(notas) == 6.2
