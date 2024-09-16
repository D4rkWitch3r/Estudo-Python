while True:

    num1 = float(input("Me informe o primerio número: "))
    operador = input("Escolha um operador para a operação ( + , - , * , / ): ")
    num2 = float(input("Me informe o segundo número: ")) 
    if operador == '+':
        resultado = num1 + num2 
        print(f"O resultado da opereção é \n{resultado}")
        
    elif operador == '-':
        resultado = num1 - num2
        print(f"O resultado da opereção é \n{resultado}")
        
    elif operador == '*':
        resultado = num1 * num2
        print(f"O resultado da opereção é \n{resultado}")
        
    else:
        resultado = num1 / num2
        print(f"O resultado da opereção é \n{resultado}")
    
    continuar = input("Você deseja fazer outra operação? (Sim ou não): ")
    if continuar != 'Sim':
        break

print ("Calculadora encerrada!")
    
