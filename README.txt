Nome: Gustavo Fernandes de Barros
Matrícula: 521430

Fiz algumas modificações devido aos simbolos usados na linguagem e nas formação das expressões regulares:

    * O simbolo de multiplicação foi substituído pelo jogo da velha(#), já que o asterísco(*) é usado como simbolo do fecho de Kleene
        * EX: 5 # 4 = 20 ;
    * Ao invés de delimitar as constantes por aspas(""), identifico elas pelo arroba(@) no começo da palavra, visto que as aspas já são utilizadas nativamente na linguagem em que programei.
        * EX: string c = @teste ;

Devido a problemas técnicos, estou usando vários DFA's menores ao invés de um só DFA contendo toda a linguagem para fazer a tokenização.
