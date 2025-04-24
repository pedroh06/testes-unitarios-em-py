import pytest

def func(alunoNotas):
    listaAceita = True
    for nota in alunoNotas:
        if not isinstance(nota, (int, float)):
            listaAceita = False
    
    if listaAceita:
        acumulador = 0
        for nota in alunoNotas:
            acumulador += nota
        mediaNotas = float(acumulador / len(alunoNotas))

        return mediaNotas
    else:
        return "Error: insira valores válidos"


def test_answer():
    casoDeTeste1_notasInvalidas = [-4, "g", "1", -23, -1]
    casoDeTeste2_notasValidas = [4, 1, 5, 10, 7]

    assert func(casoDeTeste1_notasInvalidas) == "Error: insira valores válidos"
    assert func(casoDeTeste2_notasValidas) == 5.4
