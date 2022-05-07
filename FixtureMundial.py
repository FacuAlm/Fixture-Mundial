
import random
import os
puntos = 3
letras=["A","B","C","D","E","F","G","H",0]
grupos = [
    [['Qat', 0, 0], ['Ecu', 0, 0], ['Sen', 0, 0], ['Hol', 0, 0]],
    [['Ing', 0, 0], ['Ira', 0, 0], ['USA', 0, 0], ['Repechaje1', 0, 0]],
    [['Arg', 0, 0], ['Ara', 0, 0], ['Mex', 0, 0], ['Pol', 0, 0]],
    [['Fra', 0, 0], ['Repechaje2', 0, 0], ['Din', 0, 0], ['Tun', 0, 0]],
    [['Esp', 0, 0], ['Repechaje3', 0, 0], ['Ale', 0, 0], ['Jap', 0, 0]],
    [['Bel', 0, 0], ['Can', 0, 0], ['Mar', 0, 0], ['Cro', 0, 0]],
    [['Bra', 0, 0], ['Ser', 0, 0], ['Sui', 0, 0], ['Cam', 0, 0]],
    [['Por', 0, 0], ['Gha', 0, 0], ['Uru', 0, 0], ['Cor', 0, 0]],
]

octabosgrupos=[
    [grupos[0][0],grupos[1][1]],
    [grupos[1][0],grupos[0][1]],
    [grupos[2][0],grupos[3][1]],
    [grupos[3][0],grupos[2][1]],
    [grupos[4][0],grupos[5][1]],
    [grupos[5][0],grupos[4][1]],
    [grupos[6][0],grupos[7][1]],
    [grupos[7][0],grupos[6][1]]
]

cuartosgrupos=[
    [octabosgrupos[0][0],octabosgrupos[1][0]],
    [octabosgrupos[2][0],octabosgrupos[3][0]],
    [octabosgrupos[4][0],octabosgrupos[5][0]],
    [octabosgrupos[6][0],octabosgrupos[7][0]]
]

semifinalgrupos=[
    [cuartosgrupos[0][0],cuartosgrupos[1][0]],
    [cuartosgrupos[2][0],cuartosgrupos[3][0]]
]

finalequipos=[
    [semifinalgrupos[0][0],semifinalgrupos[1][0]]
]

tercerlugarequipos=[
    [semifinalgrupos[0][1],semifinalgrupos[1][1]]
]

def resultadollaves(i,g1,g2):
    if (g1 > g2):

        print("El ganador es: ",  i[0][0])
        i[0][1] = 1
        i[0][2]=g1
        i[1][1] = 0
        i[1][2]=g2
    elif(g1 < g2):
        print("El ganador es: ", i[1][0])
        i[1][1] = 1
        i[1][2]=g2
        i[0][1] = 0
        i[0][2]=g1
    else:
        emp = random.randint(0, 1)
        if (emp == 0):
            i[0][1] = 1
            i[0][2]=g1
            i[1][1] = 0
            i[1][2]=g1
            print("el ganador es por penales: ", i[0][0])
        else:
            i[1][1] = 1
            i[1][2]=g2
            i[0][1] = 0
            i[0][2]=g2
            print("el ganador es por penales: ", i[1][0])


def repechaje1():
    teamsRepe1 = ['Esc', 'Ucr', 'Gal']
    print('El primer partido del repechaje es: ',
          teamsRepe1[0], 'vs', teamsRepe1[1])
    partido = random.randint(0, 1)

    if (partido == 0):
        print("El ganador es: ",  teamsRepe1[0])
        print('El siguiente partido es:',  teamsRepe1[0], 'vs', teamsRepe1[2])
        partido = random.randint(0, 1)
        if (partido == 0):
            print("El ganador es ", teamsRepe1[0])
            grupos[1][3][0] = teamsRepe1[0]
        else:
            print("El ganador es ", teamsRepe1[2])
            grupos[1][3][0] = teamsRepe1[2]
    else:
        print("El ganador es ", teamsRepe1[1])
        print('El siguiente partido es:',  teamsRepe1[1], 'vs', teamsRepe1[2])
        partido = random.randint(0, 1)
        if (partido == 0):
            print("El ganador es ", teamsRepe1[1])
            grupos[1][3][0] = teamsRepe1[1]
        else:
            print("El ganador es ", teamsRepe1[2])
            grupos[1][3][0] = teamsRepe1[2]


def repechaje2():
    teamsRepe1 = ['EAU', 'Aus', 'Per']
    print('El primer partido del repechaje es: ',
          teamsRepe1[0], 'vs', teamsRepe1[1])
    partido = random.randint(0, 1)

    if (partido == 0):
        print("El ganador es: ",  teamsRepe1[0])
        print('El siguiente partido es:',  teamsRepe1[0], 'vs', teamsRepe1[2])
        partido = random.randint(0, 1)
        if (partido == 0):
            print("El ganador es ", teamsRepe1[0])
            grupos[3][1][0] = teamsRepe1[0]
        else:
            print("El ganador es ", teamsRepe1[2])
            grupos[3][1][0] = teamsRepe1[2]
    else:
        print("El ganador es ", teamsRepe1[1])
        print('El siguiente partido es:',  teamsRepe1[1], 'vs', teamsRepe1[2])
        partido = random.randint(0, 1)
        if (partido == 0):
            print("El ganador es ", teamsRepe1[1])
            grupos[3][1][0] = teamsRepe1[1]
        else:
            print("El ganador es ", teamsRepe1[2])
            grupos[3][1][0] = teamsRepe1[2]


def repechaje3():
    teamsRepe1 = ['Cos', 'Nue']
    print('El primer partido del repechaje es: ',
          teamsRepe1[0], 'vs', teamsRepe1[1])
    partido = random.randint(0, 1)
    if (partido == 0):
        print("El ganador es: ",  teamsRepe1[0])
        grupos[4][1][0] = teamsRepe1[0]
    else:
        print("El ganador es: ",  teamsRepe1[1])
        grupos[4][1][0] = teamsRepe1[1]


def verGrupos():
    n=int(0)
    for j in grupos:
        print('')
        print('Grupo ', letras[n])
        print('Equipo       Puntos      DG')
        orden = j.sort(reverse=True, key=lambda i: (i[1],i[2]))
        for orden in j:
            print(orden[0], '        ', orden[1], '         ', orden[2])
        n=n+1


def primeraFecha():
    print('Partidos de 1era fecha')

    for i in grupos:

        print(i[0][0], ' vs ', i[1][0])

        goles1 = random.randint(0, 3)
        goles2 = random.randint(0, 3)

        if (goles1 > goles2):

            print("El ganador es: ",  i[0][0])
            i[0][1] = i[0][1]+puntos
            i[0][2] = i[0][2]+goles1
            i[1][2] = i[1][2]+goles2
        elif(goles1 < goles2):
            print("El ganador es: ", i[1][0])
            i[1][1] = i[1][1]+puntos
            i[1][2] = i[1][2]+goles2
            i[0][2] = i[0][2]+goles1
        else:
            print("Es Empate")
            i[1][1] = i[1][1]+1
            i[0][1] = i[1][1]+1
            i[0][2] = i[0][2]+goles1
            i[1][2] = i[1][2]+goles1

        print(i[2][0], ' vs ', i[3][0])
        goles3 = random.randint(0, 3)
        goles4 = random.randint(0, 3)

        if (goles3 > goles4):

            print("El ganador es: ",  i[2][0])
            i[2][1] = i[2][1]+puntos
            i[2][2] = i[2][2]+goles1
            i[3][2] = i[3][2]+goles2
        elif(goles3 < goles4):
            print("El ganador es: ", i[3][0])
            i[3][1] = i[3][1]+puntos
            i[3][2] = i[3][2]+goles2
            i[2][2] = i[2][2]+goles1
        else:
            print("Es Empate")
            i[3][1] = i[3][1]+1
            i[2][1] = i[2][1]+1
            i[3][2] = i[3][2]+goles1
            i[2][2] = i[2][2]+goles1


def segundaFecha():
    print('Partidos de 2da fecha')

    for i in grupos:

        print(i[0][0], ' vs ', i[2][0])
        goles1 = random.randint(0, 3)
        goles2 = random.randint(0, 3)

        if (goles1 > goles2):

            print("El ganador es: ",  i[0][0])
            i[0][1] = i[0][1]+puntos
            i[0][2] = i[0][2]+goles1
            i[2][2] = i[2][2]+goles2
        elif(goles1 < goles2):
            print("El ganador es: ", i[2][0])
            i[2][1] = i[2][1]+puntos
            i[2][2] = i[2][2]+goles2
            i[0][2] = i[0][2]+goles1
        else:
            print("Es empate")
            i[2][1] = i[2][1]+1
            i[0][1] = i[1][1]+1
            i[0][2] = i[0][2]+goles1
            i[2][2] = i[2][2]+goles1

        print(i[1][0], ' vs ', i[3][0])
        goles3 = random.randint(0, 3)
        goles4 = random.randint(0, 3)

        if (goles3 > goles4):

            print("El ganador es: ",  i[1][0])
            i[1][1] = i[1][1]+puntos
            i[1][2] = i[1][2]+goles1
            i[3][2] = i[3][2]+goles2
        elif(goles3 < goles4):
            print("El ganador es: ", i[3][0])
            i[3][1] = i[3][1]+puntos
            i[3][2] = i[3][2]+goles2
            i[1][2] = i[1][2]+goles1
        else:
            print("Es Empate")
            i[3][1] = i[3][1]+1
            i[1][1] = i[1][1]+1
            i[3][2] = i[3][2]+goles1
            i[1][2] = i[1][2]+goles1


def terceraFecha():
    print('Partidos de 3da fecha')

    for i in grupos:

        print(i[0][0], ' vs ', i[3][0])
        goles1 = random.randint(0, 3)
        goles2 = random.randint(0, 3)

        if (goles1 > goles2):

            print("El ganador es: ",  i[0][0])
            i[0][1] = i[0][1]+puntos
            i[0][2] = i[0][2]+goles1
            i[3][2] = i[3][2]+goles2
        elif(goles1 < goles2):
            print("El ganador es: ", i[3][0])
            i[3][1] = i[3][1]+puntos
            i[3][2] = i[3][2]+goles2
            i[0][2] = i[0][2]+goles1
        else:
            print("Es empate")
            i[3][1] = i[3][1]+1
            i[0][1] = i[1][1]+1
            i[0][2] = i[0][2]+goles1
            i[3][2] = i[3][2]+goles1

        print(i[1][0], ' vs ', i[2][0])
        goles3 = random.randint(0, 3)
        goles4 = random.randint(0, 3)

        if (goles3 > goles4):

            print("El ganador es: ",  i[1][0])
            i[1][1] = i[1][1]+puntos
            i[1][2] = i[1][2]+goles1
            i[2][2] = i[2][2]+goles2
        elif(goles3 < goles4):
            print("El ganador es: ", i[2][0])
            i[2][1] = i[2][1]+puntos
            i[2][2] = i[2][2]+goles2
            i[1][2] = i[1][2]+goles1
        else:
            print("Es Empate")
            i[2][1] = i[2][1]+1
            i[1][1] = i[1][1]+1
            i[2][2] = i[2][2]+goles1
            i[1][2] = i[1][2]+goles1


def octabosdefinal():
    print('Partidos de octavos de final')

    for i in octabosgrupos:

        print(i[0][0], ' vs ', i[1][0])
        goles1 = random.randint(0, 3)
        goles2 = random.randint(0, 3)

        resultadollaves(i,goles1,goles2)


def cuartosdefinal():
    print('Partidos de cuartos de final')

    for i in cuartosgrupos:

        print(i[0][0], ' vs ', i[1][0])
        goles1 = random.randint(0, 3)
        goles2 = random.randint(0, 3)

        resultadollaves(i,goles1,goles2)


def semifinal():
    print('Partidos de semifinal')

    for i in semifinalgrupos:

        print(i[0][0], ' vs ', i[1][0])
        goles1 = random.randint(0, 3)
        goles2 = random.randint(0, 3)

        resultadollaves(i,goles1,goles2)


def final():
    print('Partido de final')
    print(finalequipos[0][0][0], ' vs ', finalequipos[0][1][0])
    goles1 = random.randint(0, 3)
    goles2 = random.randint(0, 3)
    if (goles1 > goles2):
        print("El ganador es de la copa del mundo: ", finalequipos[0][0][0],"por ",goles1)
    elif(goles1 < goles2):
        print("El ganador es de la copa del mundo: ", finalequipos[0][1][0],"por ",goles2)
    else:
        emp = random.randint(0, 1)
        if (emp == 0):
            print("el ganador es de la copa del mundo por penales: ", finalequipos[0][0][0])
        else:
            print("el ganador es de la copa del mundo por penales: ", finalequipos[0][1][0])


def tercerlugar():
    print('Partidos de tercer lugar')
    print(tercerlugarequipos[0][0][0], ' vs ', tercerlugarequipos[0][1][0])
    goles1 = random.randint(0, 3)
    goles2 = random.randint(0, 3)

    if (goles1 > goles2):
        print("El Tercer lugar es: ", tercerlugarequipos[0][0][0],"por ",goles1)
    elif(goles1 < goles2):
        print("El tercer lugar: ", tercerlugarequipos[0][1][0],"por ",goles2)
    else:
        emp = random.randint(0, 1)
        if (emp == 0):
            print("el El tercer lugar por penales: ", tercerlugarequipos[0][0][0])
        else:
            print("el El tercer lugar por penales: ", tercerlugarequipos[0][1][0])


def vergruposoctavos():
    print('\n\nPartidos de octavos de final')
    for i in octabosgrupos:
        print(i[0][0], ' vs ', i[1][0])


def vergruposcuartos():
    print('\n\nPartidos de cuartos de final')
    for i in cuartosgrupos:
        print(i[0][0], ' vs ', i[1][0])


def vergrupossemifinal():
    print('\n\nPartidos de semifinal')
    for i in semifinalgrupos:
        print(i[0][0], ' vs ', i[1][0])


def vergruposfinal():
    print('\n\nPartidos de final')
    for i in finalequipos:
        print(i[0][0], ' vs ', i[1][0])


def vertercerlugar():
    print('\n\nTercer lugar')
    for i in tercerlugarequipos:
        print(i[0][0], ' vs ', i[1][0])


def resultadosoctavos():
    n=int(0)
    for j in octabosgrupos:
        print('')
        print('llave ', letras[n])
        print('Equipo       Puntos      DG')
        orden = j.sort(reverse=True, key=lambda i: (i[1],i[2]))
        for orden in j:
            print(orden[0], '        ', orden[1], '         ', orden[2])
        n=n+1


def resultadoscuartos():
    n=int(0)
    for j in cuartosgrupos:
        print('')
        print('llave ', letras[n])
        print('Equipo       Puntos      DG')
        orden = j.sort(reverse=True, key=lambda i: (i[1],i[2]))
        for orden in j:
            print(orden[0], '        ', orden[1], '         ', orden[2])
        n=n+1


def resultadossemifinal():
    n=int(0)
    for j in semifinalgrupos:
        print('')
        print('llave ', letras[n])
        print('Equipo       Puntos      DG')
        orden = j.sort(reverse=True, key=lambda i: (i[1],i[2]))
        for orden in j:
            print(orden[0], '        ', orden[1], '         ', orden[2])
        n=n+1


def resultadostercerlugar():
    n=int(0)
    for j in tercerlugarequipos:
        print('')
        print('llave ', letras[n])
        print('Equipo       Puntos      DG')
        orden = j.sort(reverse=True, key=lambda i: (i[1],i[2]))
        for orden in j:
            print(orden[0], '        ', orden[1], '         ', orden[2])
        n=n+1        

repechaje1()
repechaje2()
repechaje3()


primeraFecha()
segundaFecha()
terceraFecha()

verGrupos()

vergruposoctavos()
octabosdefinal()
resultadosoctavos()

vergruposcuartos()
cuartosdefinal()
resultadoscuartos()

vergrupossemifinal()
semifinal()
resultadossemifinal()

tercerlugar()

final()
