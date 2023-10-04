

def make_negative(number):
    if number > 0:
        return (number * -1)
    else:
        return number
        
while True:
   
    num = input("Ingrese un numero (o escriba exit para finalizar): ")
    if num.lower() == "exit":
        print("Ha salido correctamente. Nos vemos! :)")
        break
    try:
        num = float(num)
        result = make_negative(num)
        print(f"El numero negativo de {num} es: {result}")
    except ValueError:
        if num != "exit":
            print("No es valido. Intente de nuevo")


