# Definição da função cifra_vigenere que cifra ou decifra um texto com base em uma chave.
def cifra_vigenere(texto, chave, cifrar=True, i=0):
    # Caso base: Se i atingir o comprimento do texto, retornamos uma string vazia.
    if i == len(texto):
        return ''

    char = texto[i].upper()  # Obtém o caractere atual e converte para maiúsculas.
    if char.isalpha():  # Verifica se o caractere é uma letra.
        char_idx = ord(char) - 65  # Calcula o índice da letra atual (A=0, B=1, ..., Z=25).
        chave_idx = ord(chave[i % len(chave)].upper()) - 65  # Obtém o índice da letra da chave correspondente.

        if cifrar:
            novo_char = chr(((char_idx + chave_idx) % 26) + 65)  # Realiza a cifragem.
        else:
            novo_char = chr(((char_idx - chave_idx) % 26) + 65)  # Realiza a decifragem.

        # Retorna o caractere processado e chama a função recursivamente para o próximo caractere.
        return novo_char + cifra_vigenere(texto, chave, cifrar, i + 1)
    else:
        # Se o caractere não for uma letra, mantém inalterado e chama a função recursivamente para o próximo caractere.
        return char + cifra_vigenere(texto, chave, cifrar, i + 1)

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
