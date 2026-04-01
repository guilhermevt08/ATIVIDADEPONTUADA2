import os
os.system("cls")




codigos_base = [1, 2, 3, 4, 5, 6, 7]
nomes_base = ["Hemograma Completo", "Raio-X", "Ultrassonografia", "Eletrocardiograma", "Tomografia", "Ressonancia Magnetica", "Exame de Glicose"]
precos_base = [22.00, 999.00, 500.00, 120.00, 330.00, 100000.00, 50.00]


exames_escolhidos_nomes = []
exames_escolhidos_codigos = []
subtotal = 0.0

print("="*50)
print("SISTEMA DE AGENDAMENTO HOSPITALAR - V.1.0")
print("="*50)


continuar = True
while continuar:
    
    print("\nEXAMES DISPONIVEIS:")
    print(f"{'ID':<5} {'NOME':<25} {'PRECO':<10}")
    for i in range(len(codigos_base)):
        print(f"{codigos_base[i]:<5} {nomes_base[i]:<25} R$ {precos_base[i]:>8.2f}")
    
    print("-" * 30)
    entrada = input("Digite o codigo do exame (ou '0' para encerrar): ")
    
    
    if not entrada.isdigit():
        print(">> ERRO: Por favor, digite apenas numeros!")
        continue
    
    opcao = int(entrada)

    if opcao == 0:
       
        if len(exames_escolhidos_codigos) == 0:
            print("Nenhum exame selecionado. Encerrando sistema...")
            exit()
        break
    
    
    encontrado = False
    indice_achado = -1
    
    for i in range(len(codigos_base)):
        if codigos_base[i] == opcao:
            encontrado = True
            indice_achado = i
            break
    
    if encontrado:
        
        exames_escolhidos_codigos.append(codigos_base[indice_achado])
        exames_escolhidos_nomes.append(nomes_base[indice_achado])
        subtotal += precos_base[indice_achado]
        print(f"-> {nomes_base[indice_achado]} adicionado com sucesso!")
        
        
        resp = input("Deseja agendar outro exame? (S/N): ").upper()
        if resp != 'S':
            continuar = False
    else:
        print(">> CODIGO INVALIDO! Tente novamente.")


print("\n" + "="*50)
print("RESUMO DO AGENDAMENTO")
print("="*50)


print("FORMA DE PAGAMENTO:")
print("1 - Convenio (15% de desconto)")
print("2 - Particular (Valor Integral)")
print("3 - Cartao de Credito (8% de acrescimo)")

forma_valida = False
while not forma_valida:
    f_pagamento = input("Escolha a opcao (1, 2 ou 3): ")
    
    ajuste = 0.0
    label_pagamento = ""

    if f_pagamento == '1':
        label_pagamento = "Convenio"
        ajuste = - (subtotal * 0.15) 
        forma_valida = True
    elif f_pagamento == '2':
        label_pagamento = "Particular"
        ajuste = 0.0
        forma_valida = True
    elif f_pagamento == '3':
        label_pagamento = "Cartao de Credito"
        ajuste = subtotal * 0.08 
        forma_valida = True
    else:
        print("Opcao de pagamento inexistente. Selecione 1, 2 ou 3.")

valor_final = subtotal + ajuste


print("\n" + "*"*50)
print("COMPROVANTE DE AGENDAMENTO")
print("*"*50)
print("Exames selecionados:")
for j in range(len(exames_escolhidos_codigos)):
    print(f"- Cod: {exames_escolhidos_codigos[j]} | {exames_escolhidos_nomes[j]}")

print("-" * 30)
print(f"SUBTOTAL:           R$ {subtotal:.2f}")
print(f"FORMA DE PAGAMENTO: {label_pagamento}")

if ajuste < 0:
    print(f"DESCONTO APLICADO:  R$ {abs(ajuste):.2f}")
elif ajuste > 0:
    print(f"ACRESCIMO (JUROS):  R$ {ajuste:.2f}")
else:
    print(f"TAXAS/DESCONTOS:    R$ 0.00")

print("-" * 30)
print(f"TOTAL A PAGAR:      R$ {valor_final:.2f}")
print("*"*50)