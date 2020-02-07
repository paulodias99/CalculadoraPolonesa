##########################################
#           Autor: Paulo Dias            #
##########################################

#Criação da classe Pilha()
class Pilha():
#Criação das funções da classe
    def __init__(self):
        self.__pilha=[]

    def __len__(self):
        return len(self.__pilha)

    def is_empty(self):
        return len(self.__pilha)==0

    def push(self,apender):
        self.__pilha.append(apender)

    def pop(self):
        if(self.is_empty()):
            print('A pilha está vazia.')
        else:
            return self.__pilha.pop()

    def top(self):
        if(self.is_empty()):
            print('A pilha está vazia.')
        else:
            return self.__pilha[-1]
    def show(self):
        return self.__pilha

    def mostrar(self, i):
        return self.__pilha[i]

if __name__ == '__main__':
    #Variável pilha recebe a classe Pilha() para utilizar suas funções
    pilha = Pilha()
    #ÍNICIO DA CALCULADORA POLONESA
    entrar = int(input("Digite 1 para entrar e digite SAIR para sair."))
    while (entrar == 1):
        recebe = input('Um número ou uma operação\nPara sair digite RESULTADO\n')
        pilha.push(recebe)
        #Condicional para as operações +, -, *, /
        if pilha.top() == "*":
            p1 = pilha.__len__() - 2
            p2 = pilha.__len__() - 3
            v1 = float(pilha.mostrar(p1))
            v2 = float(pilha.mostrar(p2))
            if v1 > v2:
                v3 = v1 * v2
            else:
                v3 = v2 * v1
            pilha.pop()
            pilha.pop()
            pilha.pop()
            pilha.push(v3)
        if pilha.top() == "/":
            p1 = pilha.__len__() - 2
            p2 = pilha.__len__() - 3
            v1 = float(pilha.mostrar(p1))
            v2 = float(pilha.mostrar(p2))
            if v1 > v2:
                v3 = v1 / v2
            else:
                v3 = v2 / v1
            pilha.pop()
            pilha.pop()
            pilha.pop()
            pilha.push(v3)
        if pilha.top() == "+":
            p1 = pilha.__len__() - 2
            p2 = pilha.__len__() - 3
            v1 = float(pilha.mostrar(p1))
            v2 = float(pilha.mostrar(p2))
            v3 = v1 + v2
            pilha.pop()
            pilha.pop()
            pilha.pop()
            pilha.push(v3)
        if pilha.top() == "-":
            p1 = pilha.__len__() - 2
            p2 = pilha.__len__() - 3
            v1 = float(pilha.mostrar(p1))
            v2 = float(pilha.mostrar(p2))
            if v1 > v2:
                v3 = v1 - v2
            else:
                v3 = v2 - v1
            pilha.pop()
            pilha.pop()
            pilha.pop()
            pilha.push(v3)
        if recebe == 'resultado':
            pilha.pop()
            print("================= NOTAÇÃO POLONESA =================\n"
                  "=================    RESULTADO     =================\n")
            break
    print(pilha.show())