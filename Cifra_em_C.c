#include <stdio.h>
#include <string.h>

// Função que cifra ou decifra um texto com base em uma chave.
void cifraVigenere(char texto[], char chave[], int cifrar) {
    int textoLen = strlen(texto);
    int chaveLen = strlen(chave);

    for (int i = 0; i < textoLen; i++) {
        char c = texto[i];
        if (isalpha(c)) {  // Verifica se o caractere é uma letra do alfabeto.
            int charIdx = c - 'A';  // Obtém o índice da letra no alfabeto.
            int chaveIdx = chave[i % chaveLen] - 'A';  // Obtém o índice da letra da chave.
            char novoChar;
            
            if (cifrar) {
                // Fórmula para cifrar: (posição_da_letra_no_texto + posição_da_letra_na_chave) % 26.
                novoChar = ((charIdx + chaveIdx) % 26) + 'A';
            } else {
                // Fórmula para decifrar: (posição_da_letra_no_texto - posição_da_letra_na_chave + 26) % 26.
                novoChar = ((charIdx - chaveIdx + 26) % 26) + 'A';
            }
            
            texto[i] = novoChar;  // Atualiza o caractere no texto.
        }
    }
}

int main() {
    char texto[1000];
    char chave[100];
    char escolha;
    
    printf("Digite o texto: ");
    scanf("%s", texto);
    
    printf("Digite a chave: ");
    scanf("%s", chave);
    
    printf("Cifrar (C) ou Decifrar (D)? ");
    scanf(" %c", &escolha);
    
    if (escolha == 'C') {
        cifraVigenere(texto, chave, 1);  // Chama a função para cifrar.
        printf("Texto Cifrado: %s\n", texto);
    } else if (escolha == 'D') {
        cifraVigenere(texto, chave, 0);  // Chama a função para decifrar.
        printf("Texto Decifrado: %s\n", texto);
    } else {
        printf("Opção inválida.\n");
    }
    
    return 0;
}
