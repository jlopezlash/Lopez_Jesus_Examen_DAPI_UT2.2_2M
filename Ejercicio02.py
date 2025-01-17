Alumnado = {}
x = 0
A = 0
while x != 4:
    x = int(input(  '1)Añadir alumno/a '
            '2)Número de aprobados '
            '3)Mostrar todo el alumnado '))
    if x == 1:
        Nombre = input('Dime el nombre del alumno: ')
        Nota = bool(input('¿Cual es su nota? '))
        Alumnado[Nombre] = Nota
    if x == 2:
        for value in Alumnado.values():
            for nota in str(value):
                if bool(nota) >= 5:
                    A + 1
        print('El número de aprobados es ',+ A)
    if x == 3:
        l = Alumnado.keys()
        print(l)