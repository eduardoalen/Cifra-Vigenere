# Definição da função cifra_vigenere que cifra ou decifra um texto com base em uma chave.
def cifra_vigenere(texto, chave, cifrar=True):
    resultado = []  # Inicializa uma lista vazia para armazenar o resultado cifrado ou decifrado.
    chave = chave.upper()  # Converte a chave para letras maiúsculas para consistência.
    texto = texto.upper()  # Converte o texto para letras maiúsculas para consistência.
    chave_len = len(chave)  # Calcula o comprimento da chave para uso posterior.

    # Loop que percorre o texto original caractere por caractere.
    for i in range(len(texto)):
        char = texto[i]  # Obtém o caractere atual do texto.
        if char.isalpha():  # Verifica se o caractere é uma letra do alfabeto.
            char_idx = ord(char) - 65  # Calcula o índice da letra atual (A=0, B=1, ..., Z=25).
            chave_idx = ord(chave[i % chave_len]) - 65  # Obtém o índice da letra da chave correspondente.
            if cifrar:  # Se a ação for cifrar:
                novo_char = chr(((char_idx + chave_idx) % 26) + 65)  # Realiza a cifragem.
            else:  # Se a ação for decifrar:
                novo_char = chr(((char_idx - chave_idx) % 26) + 65)  # Realiza a decifragem.
            resultado.append(novo_char)  # Adiciona o caractere cifrado ou decifrado ao resultado.
        else:
            resultado.append(char)  # Se o caractere não for uma letra, mantém inalterado.

    return ''.join(resultado)  # Retorna o resultado (lista de caracteceres) como uma string.

# Definição da função principal do programa.
def main():
    texto = input("Digite o texto: ")  # Solicita ao usuário que digite o texto a ser cifrado ou decifrado.
    chave = input("Digite a chave: ")  # Solicita ao usuário que digite a chave.
    escolha = input("Cifrar (C) ou Decifrar (D)? ").upper()  # Solicita ao usuário que escolha cifrar ou decifrar.

    if escolha == "C":  # Se a escolha for cifrar:
        texto_cifrado = cifra_vigenere(texto, chave, cifrar=True)  # Chama a função de cifragem.
        print("Texto Cifrado:", texto_cifrado)  # Exibe o resultado cifrado.
    elif escolha == "D":  # Se a escolha for decifrar:
        texto_decifrado = cifra_vigenere(texto, chave, cifrar=False)  # Chama a função de decifragem.
        print("Texto Decifrado:", texto_decifrado)  # Exibe o resultado decifrado.
    else:  # Se a escolha não for válida:
        print("Opção inválida.")  # Exibe uma mensagem de opção inválida.

if __name__ == "__main__":
    main()  # Chama a função principal quando o programa é executado.
