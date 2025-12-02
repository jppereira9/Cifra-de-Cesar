# Executa a criptografia ou descriptografia da Cifra de César.
def cifra_de_cesar(texto, chave, modo):

    resultado = ''  # A priori resultado é vazio
    # Esse trecho realiza a criptografia
    if modo == 'd':
        chave = -chave

    for char in texto:
        if char.isalpha():
            # Determina o ponto de partida (A ou a)
            inicio = ord('A') if char.isupper() else ord('a')

            # Converte o caractere para seu deslocamento baseado em 0 (0-25)
            # Aplica o deslocamento e o módulo 26
            # Converte de volta para caractere
            novo_ord = (ord(char) - inicio + chave) % 26 + inicio
            resultado += chr(novo_ord)
        else:
            # Mantém caracteres não-alfabéticos como estão (espaços, pontuação, números)
            resultado += char

    return resultado
    # Retorna o texto criptografado


def descriptografia_forca_bruta(texto_cifrado):

    # Tenta as 26 chaves possiveis para a criptografia
    # texto_cifrado: A string a ser descriptografada.
    # return: Uma lista de tuplas (chave, texto_tentado).

    tentativas = []
    # A Cifra de César tem um alfabeto de 26 letras, então só há 26 chaves
    for chave in range(26):  # Loop para testar cada chave
        texto_tentado = cifra_de_cesar(texto_cifrado, chave, 'd')
        # Adiciona na lista o texto descriptografado com base na chave
        tentativas.append((chave, texto_tentado))
    return tentativas


def menu_principal():  # Menu de opções

    print("\n--- Menu de Opções ---")
    print("1 - Criptografar texto")
    print("2 - Descriptografar texto (Chave conhecida)")
    print("3 - Descriptografar texto (Brute Force)")
    print("0 - Sair do Programa")
    print("------------------------")


def executar_programa():
    # Função principal que gerencia o menu.
    while True:
        menu_principal()

        escolha = input("Digite sua opção (0 a 3): ")

        # Tenta converter a entrada para um inteiro
        try:
            opcao = int(escolha)
        except ValueError:
            print("\n Opção inválida. Digite um número de 0 a 3.")
            continue  # Volta para o início do loop

        # --- 0 - Sair do programa ---
        if opcao == 0:
            print("\nObrigado por usar o programa!")
            break  # Sai do loop while

        # 1 - Criptografar texto
        elif opcao == 1:
            print("\n 1 - Critografar texto")

            # Recebe o texto para ser criptografado
            texto_plano = input("Digite a mensagem para criptografar: ")

            # Garante que a chave seja um número
            try:
                chave = int(
                    input("Digite a chave (número) para criptografar: "))
            except ValueError:
                print("\n Chave inválida. Digite um número inteiro.")
                continue

            # Criptografa texto
            texto_criptografado = cifra_de_cesar(texto_plano, chave, 'c')
            # Exibe o texto original, a chave escolhida e o texto criptografado
            print(f"Texto Original: {texto_plano}")
            print(f"Chave de Criptografia: {chave}")
            print(f" Texto Cifrado: {texto_criptografado}\n")

        # 2 - Descriptografar texto (Chave conhecida)
        elif opcao == 2:
            print("\nDescriptografando texto (Chave conhecida)")
            texto_cifrado = input("Digite o texto para descriptografar: ")

            # Garante que a chave seja um número
            try:
                chave = int(input("Digite a chave (número) conhecida: "))
            except ValueError:
                print("\n Chave inválida. Digite um número inteiro.")
                continue

            texto_descriptografado = cifra_de_cesar(texto_cifrado, chave, 'd')

            print(f"Texto Cifrado: {texto_cifrado}")
            print(f"Chave de Descriptografia: {chave}")
            print(f"Texto Descriptografado: {texto_descriptografado}\n")

        # 3 - Descriptografar texto (Brute Force)
        elif opcao == 3:
            print("\n Descriptografando (Brute Force)")

            texto_para_bruteforce = input("Digite o texto criptografado: ")

            # Chama a função de Força Bruta
            tentativas = descriptografia_forca_bruta(texto_para_bruteforce)

            # Imprime todos os resultados
            for chave, texto in tentativas:
                print(f" Chave {chave+1:}: {texto}")

            print("\nAnálise concluída. Procure pelo resultado legível acima.")

        # Opção Inválida
        else:
            # Captura qualquer número que não esteja entre a opções válidas
            print(
                f"\n Opção *{opcao}* inválida. Por favor, escolha uma opção entre 0 e 3.")

        print("-" * 24)


# Chama a função principal para iniciar o programa
executar_programa()
