#entrada 

#função de menu para o usuario escolher o que ele quer fazer
def menu():
    print("Escolha uma operação: ")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
    print("")

def calcular(operador,num1,num2):
    #if-elif-else
    if operador == 1:
        return num1 + num2
    
    elif operador == 2:
        return num1 - num2

    elif operador == 3:
        return num1*num2

    elif operador == 4:
        if num2 != 0:
            return num1/num2
        else: ("Erro divisão por zero")

    else:
        return "saindo! Encerrando o program... "
    
def main():
    while True:
        menu()
        opcao = int(input("Escolha uma das opcoes acima: "))
        if opcao > 5:
            print("Erro! Digite uma opção válida")
            return main()
        elif opcao == 5:
            print("Saindo do programa")
            break

        num1 =  float(input("digite um numero: "))
        num2 =  float(input("digite um numero: "))

        resultado = calcular(opcao,num1,num2)

        print(f"O resultado é: {resultado}")

        continuaounao = input("Deseja continuar:? (s/n): ")

        if continuaounao.lower != 's':
            print("Obrigado por usar a calculadora. Encerrando... ")
            break


#processamento


#saida
main()