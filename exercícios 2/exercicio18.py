def converter_para_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def main():
    while True:
        celsius = float(input("Digite a temperatura em Celsius (ou digite -999 para sair): "))
        if celsius == -999:
            print("Saindo do programa.")
            break
            
        fahrenheit = converter_para_fahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")

main()
