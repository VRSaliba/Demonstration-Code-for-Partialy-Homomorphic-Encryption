from lightphe import LightPHE

#build a cryptosystem
# cs = LightPHE(algoritmo)
# algorithms = [
#   "RSA",
#   "ElGamal",
#   "Exponential-ElGamal",
#   "Paillier",
#   "Damgard-Jurik",
#   "Okamoto-Uchiyama",
#   "Benaloh",
#   "Naccache-Stern",
#   "Goldwasser-Micali",
#   "EllipticCurve-ElGamal"
# ]

# print(cs_rsa.cs.keys)

print("Inicializando criptosistemas:")
# print("Criptosistema RSA")
cs_rsa = LightPHE("RSA")
# print("Criptosistema Paillier")
cs_pai = LightPHE("Paillier")
# print("Criptosistema Okamoto-Uchiyama")
cs_ouc = LightPHE("Okamoto-Uchiyama")
# print("Criptosistema Goldwasser-Micali")
cs_gom = LightPHE("Goldwasser-Micali")
# print("Criptosistema Benaloh")
cs_ben = LightPHE("Benaloh")

print("Insira um valor numérico")
valor1 = float(input())
print("Insira outro valor numérico")
valor2 = float(input())

opcao = 0
# confirmar com o prof quais algoritmos utilizar aqui
while opcao != 7:
    print()
    print("Qual operação deseja realizar sobre os valores?")
    print("1) Multiplicar valores (usando RSA) - Multiplicatively Homomorphic")
    print("2) Somar valores (usando Paillier) - Additively Homomorphic")
    print("3) Multiplicar valor com uma constante (usando Okamoto-Uchiyama) - Multiplication with a Plain Constant")
    print("4) Realizar operação XOR entre valores (usando Goldwasser-Micali) - Exclusively Homomorphic")
    print("5) Regeneration of Ciphertext")
    print("6) Mudar valores usados nas operações")
    print("7) Parar execução do código")
    print()
    print("Opção escolhida: ")

    opcao = int(input())
    print()
    match opcao:
        case 1:
            print("Multiplicando valor 1 pelo valor 2 usando RSA")
            
            print("Valor 1:", valor1, '\n' "Valor 2:", valor2)
            multiplicacao = valor1 * valor2
            print("Valor da multiplicação: ", multiplicacao, '\n')
            
            valor1_rsa = cs_rsa.encrypt(valor1)
            valor2_rsa = cs_rsa.encrypt(valor2)
            print("Valor 1 criptografado:", valor1_rsa.value, '\n' "Valor 2 criptografado:", valor2_rsa.value, '\n')
            
            multiplicacao_rsa = cs_rsa.decrypt(valor1_rsa * valor2_rsa)
            print("Resultado descriptografado:", multiplicacao_rsa)
        case 2:
            print("Adicionando valor 1 ao valor 2 usando Paillier")
            
            print("Valor 1:", valor1, '\n' "Valor 2:", valor2)
            soma = valor1 + valor2
            print("Valor da soma: ", soma, '\n')
            
            valor1_pai = cs_pai.encrypt(valor1)
            valor2_pai = cs_pai.encrypt(valor2)
            print("Valor 1 criptografado:", valor1_pai.value, '\n' "Valor 2 criptografado:", valor2_pai.value, '\n')
            
            soma_pai = cs_pai.decrypt(valor1_pai + valor2_pai)
            print("Resultado descriptografado:", soma_pai)
        case 3:
            print("Multiplicando valor 1 pelo valor de uma constante usando Okamoto-Uchiyama")
            
            valor1_ouc = cs_ouc.encrypt(valor1)
            print("Valor 1 criptografado:", valor1_ouc.value, '\n')
            
            print("Insira um valor para multiplicar: ")
            multiplicacao_ouc = cs_ouc.decrypt(valor1_ouc * float(input()))
            print("Resultado descriptografado:", multiplicacao_ouc)
        case 4:
            print("Opera um XOR (OU exclusivo) entre o valor 1 e o valor 2 usando Goldwasser-Micali")
            
            valor1_gom = cs_gom.encrypt(valor1)
            valor2_gom = cs_gom.encrypt(valor2)
            print("Valor 1 criptografado:", valor1_gom, '\n' "Valor 2 criptografado:", valor2_gom, '\n')
            
            xor_gom = cs_gom.decrypt(valor1_gom ^ valor2_gom)
            
            print("Valor XOR entre valor 1 e valor 2: ", int(valor1) ^ int(valor2))
            print("Valor XOR entre valor 1 e valor 2 criptografados: ", xor_gom)
        case 5:
            print("Gera outro valor cifrado do valor 1 usando Benaloh")
                        
            valor1_ben_original = cs_ben.encrypt(valor1)
            print("Exemplo de valor criptografado usando o valor 1: ", valor1_ben_original.value)
            
            valor1_ben_novo = cs_ben.regenerate_ciphertext(valor1_ben_original)
            print("Novo valor criptografado usando o valor 1: ", valor1_ben_novo.value)
            
            print("Valor 1 descriptografado:", cs_ben.decrypt(valor1_ben_original))
            print("Novo valor descriptografado:", cs_ben.decrypt(valor1_ben_novo))
        case 6:
            print("Insira o valor 1")
            valor1 = float(input())
            print("Insira o valor 2")
            valor2 = float(input())
        case 7:
            print("Parando execucao")
        case _:
            print("Erro, favor inserir valor valido")
