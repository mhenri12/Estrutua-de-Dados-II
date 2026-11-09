#include <stdio.h>



// Struct do livro

struct Livro {

char titulo[100];

char autor[100];

int ano;

};



intmain() {



struct Livro livro;



// Entrada de dados

printf("Digite o titulo do livro: ");

scanf("%s", livro.titulo);



printf("Digite o autor do livro: ");

scanf("%s", livro.autor);



printf("Digite o ano de publicacao: ");

scanf("%d", &livro.ano);



// Saída de dados

printf("\n--- Informacoes do Livro ---\n");

printf("Titulo: %s\n", livro.titulo);

printf("Autor: %s\n", livro.autor);

printf("Ano de publicacao: %d\n", livro.ano);



return0;

}
