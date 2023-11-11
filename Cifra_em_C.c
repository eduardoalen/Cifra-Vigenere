#include <stdio.h>
#include <string.h>

// Função que cifra ou decifra um texto com base em uma chave.
void cifraVigenere(char texto[], char chave[], int cifrar) {
    int textoLen = strlen(texto);
    int chaveLen = strlen(chave);

    for (int i = 0; i < textoLen; i++) {
        char c = texto[i];
        if (isalpha(c)) {
            int charIdx = c - 'A';
            int chaveIdx = chave[i % chaveLen] - 'A';
            char novoChar;
            
            if (cifrar) {
                novoChar = ((charIdx + chaveIdx) % 26) + 'A';
            } else {
                novoChar = ((charIdx - chaveIdx + 26) % 26) + 'A';
            }
            
            texto[i] = novoChar;
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
        cifraVigenere(texto, chave, 1);
        printf("Texto Cifrado: %s\n", texto);
    } else if (escolha == 'D') {
        cifraVigenere(texto, chave, 0);
        printf("Texto Decifrado: %s\n", texto);
    } else {
        printf("Opção inválida.\n");
    }
    
    return 0;
}
