import os
os. system("clear")

valor = 0
total = 0
lista_pratos = [] #variavel para guardar os pratos escolhidos.

while True:
    menu = int(input("""
Olá seja bem vindo, escolha seu prato: \n
CÓDIGO  |    DESCRIÇÃO    | Valor
----------------------------------
    1   | Lasanha         | 25.00
    2   | Pizza           | 30.00
    3   | Hambúrguer      | 18.00
    4   | Salada          | 15.00
    5   | Sushi           | 35.00
    6   | Musse           | 06.00
    7   | Bife com fritas | 28.00
    0   | Encerrar Pedido
"""))
    
    match menu:
        case 1:
            print("Você escolheu lasanha")
            valor = 25.00
            prato = "Lasanha"
        case 2:
            print("Você escolheu pizza")
            valor = 30.00
            prato = "Pizza"
        case 3:
            print("Você escolheu Hambúrguer")
            valor = 18.00
            prato = "Hambúrguer"
        case 4:
            print("Você escolheu salada")
            valor = 15.00
            prato = "Salada"
        case 5:
            print("Você escolheu sushi")
            valor = 35.00
            prato = "Sushi"
        case 6:
            print("Você escolheu musse")
            valor = 6.00
            prato = "Musse"
        case 7:
            print("Você escolheu bife com fritas")
            valor = 28.00
            prato = "Bife com fritas"
        case 0: 
            print(f"\nTotal do pedido: {valor:.2f}")
            break
        case _:
            print ("\nDesculpe, não existe essa opção. Digite novamente.")

    lista_pratos.append(prato)
    total += valor

    continuar = input("\nDeseja adicionar mais um pedido? (s/n): ").strip().lower()

    if continuar == "s":
        continue
    elif continuar != "n":
        print(f"\nTotal do pedido: {total:.2f}")
        print("Opção inválida, digite 's' ou 'n' ")
        break
    forma_pagamento = int(input("\nDigite a forma de pagamento:\n 1 | Á vista você ganha um desconto de 10%. \n 2 | Parcelado tem juros de 10%.\n "))

    if forma_pagamento == 1:
        desconto = total * 0.10 #aplicando desconto 
        valor_pagar = total - desconto
        print(f"O valor do seu desconto foi de: R$ {desconto:.2f}")
        print(f"\nPagamento á vista, Total: R$ {valor_pagar:.2f}")

    elif forma_pagamento == 2:
        acrescimo = total * 0.10 #aplicando acrescimo
        valor_acrescimo = acrescimo + total

        print(f"\nVocê teve um acrescimo de R$ {acrescimo:.2f} no seu pedido.")
        print(f"\nTotal: R$ {valor_acrescimo:.2f}")
    else:
        print("\nOpção inválida.")

    for prato in lista_pratos:
        print(f"Seu prato escolhido foi: {prato}")

    print("\nPedido finalizado com sucesso. Muito obrigado!! Volte sempre.")
    break