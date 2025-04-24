def buscar_voos(origem, destino):
    voos_disponiveis = {
        ("Belém", "São Paulo"): [{"voo": "BE123", "horario": "08:00", "preco": 500, "assentos": 2}],
        ("Belém", "Manaus"): [{"voo": "BE456", "horario": "14:00", "preco": 350, "assentos": 0}],
    }
    return voos_disponiveis.get((origem, destino), [])

def selecionar_voo(voos):
    print("\nVoos disponíveis:")
    for i, voo in enumerate(voos):
        print(f"{i+1}. Voo {voo['voo']} - {voo['horario']} - R${voo['preco']} - Assentos: {voo['assentos']}")
    escolha = int(input("Escolha o número do voo desejado: ")) - 1
    return voos[escolha]

def reservar_assento(voo):
    if voo["assentos"] > 0:
        nome = input("Digite o nome do passageiro: ")
        voo["assentos"] -= 1
        print(f"\nReserva confirmada para {nome} no voo {voo['voo']} às {voo['horario']}.")
        print("Um e-mail de confirmação foi enviado.\n")
        return True
    else:
        print("Não há assentos disponíveis nesse voo.")
        return False

def main():
    print("Sistema de Reserva de Voos\n")
    origem = input("Digite o local de partida: ")
    destino = input("Digite o destino desejado: ")

    if not origem or not destino:
        print("Erro: Local de partida ou destino inválido.")
        return

    voos = buscar_voos(origem, destino)
    if not voos:
        print("Não há voos disponíveis para essa rota.")
        return

    voo_selecionado = selecionar_voo(voos)
    sucesso = reservar_assento(voo_selecionado)

    if not sucesso:
        print("A reserva não pôde ser confirmada.")

if __name__ == "__main__":
    main()