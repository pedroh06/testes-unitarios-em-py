def func(idade):

    if idade <= 0:
        print("Idade inválida")
    else:
        if idade < 18:
            print("Não precisa votar obrigatoriamente")
        elif idade >= 18 and idade < 70:
            print("Deve votar obrigatoriamente")
        else:
            print("Não precisa votar obrigatoriamente")


def test_answer():
    assert func(17) == print("Não precisa votar obrigatoriamente")
    assert func(18) == print("Deve votar obrigatoriamente")
    