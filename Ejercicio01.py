def OrdenarLista(a):

    b = list(a)
    b.sort('-1')
    with open('ListaOrdenada.txt','w') as file:
        file.write(str(b))
    return()
OrdenarLista([2,3,7,5,8])

def NumeroPar():
        with open('ListaOrdenada.txt','r') as file: 
                    with open('ListaDePares.txt','w') as file:
                        file.write()
NumeroPar()