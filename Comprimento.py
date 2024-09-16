comprimento = float(input("Digite o comprimento da cozinha:"))
largura = float(input("Digite a largura da cozinha:"))
altura = float(input("Digite a altura da cozinha:"))
area1 = comprimento * altura
area2 = largura * altura
areatotal = 2 * (area1 + area2)
areacaixa = float(input("Digite a área coberta por uma caixa de azulejos: "))
resultado = round(areatotal / areacaixa)
print(f"O número mínimo de caixas de azulejos necessárias: {resultado}")
