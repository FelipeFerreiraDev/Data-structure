## Bubble sort feito recursivamente
## O bubble sort é um algoritmo de ordenação que percorre o vetor diversas vezes, comparando elementos adjacentes e trocando-os de posição se estiverem na ordem errada.
## A ideia é que os elementos maiores "borbulhem" para o final do vetor, enquanto os menores "afundam" para o início.
## O algoritmo termina quando não houver mais trocas a serem feitas.
## O pior caso de tempo de execução é O(n^2), onde n é o número de elementos no vetor.
## O melhor caso é O(n), quando o vetor já está ordenado.

def sort(lista):
    ordered = True
    for index, x in enumerate(lista):
        if index + 1 < len(lista):
            if x > lista[index+1]:
                aux = lista[index+1]
                lista[index+1] = x
                lista[index] = aux
                ordered = False
    print(lista)
    print('------')
    if not ordered:
        sort(lista)

lista = [9, 5, 3, 7, 8, 1, 0]
sort(lista)


## Explicação do algoritmo criado
## A função sort recebe uma lista como argumento.
## A variável ordered é inicializada como True.
## O loop for percorre a lista, usando enumerate para obter o índice e o valor de cada elemento.
## Dentro do loop, é verificado se o índice + 1 é menor que o tamanho da lista.
## Se for, é verificado se o elemento atual é maior que o próximo elemento.
## Se for, os elementos são trocados de posição e a variável ordered é setada como False.
## Após o loop, é verificado se a lista está ordenada.
## Se não estiver, a função sort é chamada recursivamente.
## Se estiver, a lista é impressa e a função termina.

## O algoritmo é ineficiente, pois tem complexidade O(n^2) no pior caso.
## O algoritmo é recursivo, o que pode causar problemas de desempenho para listas muito grandes.
## O algoritmo não é estável, ou seja, elementos iguais podem trocar de posição.
## O algoritmo é simples e fácil de implementar.
## O algoritmo é eficiente para listas pequenas ou quase ordenadas.