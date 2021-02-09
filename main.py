import re
import webbrowser
from tkinter import filedialog



memoria = []
objectos = []
lista_ayuda = []
nuev_lista = []



class Linea:
    def __init__(self, id, lista, instruccion1=False, instruccion2=None):
        self.id = id
        self.lista = lista
        self.instruccion1 = instruccion1
        self.instruccion2 = instruccion2

    def imprimir(self):

        if self.instruccion2 == None:
            print(str(self.id) + str(self.lista) + str(self.instruccion1))
        else:
            print(str(self.id) + str(self.lista) + str(self.instruccion1) + str(self.instruccion2))
    """
    def ordenar(self):
        lista1 = self.lista
        #print(lista1)
        if self.instruccion1 == False:
            return
        else:
            cadena = ''
            for i in range(len(lista1)):
                peque = min(lista1)
                cadena += peque + ', '
                lista1.remove(peque)
            return cadena
    """
    """
    def buscar(self):
        nuev_lista = self.lista
        #print(nuev_lista)
        if self.instruccion2 == None:
            return
        else:
            contador = 0
            validos = '{'
            #print(self.lista)
            for elemento in self.lista:
                contador += 1
                if elemento == self.instruccion2:
                    validos = validos + str(contador)
                    if contador < (len(nuev_lista) - 1):
                        validos += ','
                else:
                    continue
            validos += '}'
            return validos
    """

def ordenar(Linea):
    for elemao in Linea.lista:
        lista_ayuda.append(elemao)
    #lista_ayuda = Linea.lista
    #print(lista1)
    if Linea.instruccion1 == False:
        return
    else:
        cadena = ''
        for i in range(len(lista_ayuda)):
            peque = min(lista_ayuda)
            cadena += peque + ', '
            lista_ayuda.remove(peque)
        lista_ayuda.clear()
        return cadena

def buscar(Linea):
    for elemao in Linea.lista:
        nuev_lista.append(elemao)
    if Linea.instruccion2 == None:
        return
    else:
        contador = 0
        validos = '{'
        for elemento in Linea.lista:
            contador += 1
            if elemento == Linea.instruccion2:
                validos = validos + str(contador)
                if contador < (len(nuev_lista) - 1):
                    validos += ','
            else:
                continue
        validos += '}'
        nuev_lista.clear()
        if validos == '{}':
            return 'Ninguna coincidencia'
        else:
            return validos

"""
#print(archivo.readlines())
file = filedialog.askopenfile(title="abrir")
#file = open('entrada.txt', 'r')
for line in file:
    memoria.append(line.replace('\n', ''))
print(memoria)
#print(len(memoria))
#for com in memoria:
    #print(com)


for com in memoria:
    inst1 = False
    entrada = str(com)
    if re.search(r"[A-z]+[0-9]*", entrada):
        id = re.search(r"[A-z]+[0-9]*", entrada).group()
        #print(id)

    if re.search(r"=([0-9]*,*)+", entrada):
        nlista = re.search(r"=([0-9]*,*)+", entrada).group().replace('=', '')
        lista = list(nlista.split(','))
        # print(lista)

    if re.search(r"ORDENAR", entrada):
        inst1 = True
        #print(inst1)

    if re.search(r"BUSCAR [0-9]*", entrada):
        inst2 = re.search(r"BUSCAR [0-9]*", entrada).group().replace('BUSCAR', '').replace(' ', '')
        #print(inst2)

    elif not re.search(r"BUSCAR [0-9]*", entrada):
        inst2 = None

    a = Linea(id, lista, inst1, inst2)
    objectos.append(a)

print(objectos)

"""

while True:
    print('\n')
    print('========Menu=========')
    print('1. Cargar archivo de entrada')
    print('2. Desplegar listas ordenadas')
    print('3. Desplegar búsquedas')
    print('4. Desplegar todas')
    print('5. Desplegar todas a archivo')
    print('6. Salir')
    comando = input('Ingrese una opcion: ')

    if comando == '1':
        memoria.clear()
        objectos.clear()
        file = open('entrada.txt', 'r')
        for line in file:
            memoria.append(line.replace('\n', ''))
        #print(memoria)
        #print(len(memoria))
        #for com in memoria:
            #print(com)
        for com in memoria:
            inst1 = False
            entrada = str(com)
            if re.search(r"[A-z]+[0-9]*", entrada):
                id = re.search(r"[A-z]+[0-9]*", entrada).group()
                #print(id)
        
            if re.search(r"=([0-9]*,*)+", entrada):
                nlista = re.search(r"=([0-9]*,*)+", entrada).group().replace('=', '')
                lista = list(nlista.split(','))
                # print(lista)
        
            if re.search(r"ORDENAR", entrada):
                inst1 = True
                #print(inst1)
        
            if re.search(r"BUSCAR [0-9]*", entrada):
                inst2 = re.search(r"BUSCAR [0-9]*", entrada).group().replace('BUSCAR', '').replace(' ', '')
                #print(inst2)
        
            elif not re.search(r"BUSCAR [0-9]*", entrada):
                inst2 = None
                
            a = Linea(id, lista, inst1, inst2)
            objectos.append(a)

    if comando == '2':
        contador1 = -1
        for obj in objectos:
            contador1 += 1
            if obj.instruccion1 == False:
                continue
            elif obj.instruccion1 == True:
                print(memoria[contador1] + ' | ' + str(obj.id) + ': ' + 'ORDENADOS = ' + str(ordenar(obj)))

    if comando == '3':
        contador2 = -1
        for obj in objectos:
            contador2 += 1
            if obj.instruccion2 != None:
                print(memoria[contador2] + ' | ' + str(obj.id) + ': ' + 'BUSQUEDA ' + str(obj.instruccion2) + ' = ' + buscar(obj))

    if comando == '4':
        contador3 = -1
        for obj in objectos:
            contador3 += 1
            if obj.instruccion1 is True:
                if obj.instruccion2 != None:
                    print(memoria[contador3] + ' | ' + str(obj.id) + ': ' + 'ORDENADOS = ' + str(ordenar(obj)) + 'BUSQUEDA ' + str(obj.instruccion2) + ' = ' + buscar(obj))
                elif obj.instruccion2 == None:
                    print(memoria[contador3] + ' | ' + str(obj.id) + ': ' + 'ORDENADOS = ' + str(ordenar(obj)) )

            elif obj.instruccion2 !=None:
                print(memoria[contador3] + ' | ' + str(obj.id) + ': ' + 'BUSQUEDA ' + str(obj.instruccion2) + ' = ' + buscar(obj))

            else:
                continue

    if comando == '5':
        with open('reporte.html', 'w') as reporte:
            reporte.write('<html>' + '\n')
            reporte.write('<head>' + '\n')
            reporte.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">' + '\n')
            reporte.write('</head>' + '\n')
            reporte.write('<body>' + '\n')
            reporte.write('<center>' + '\n')
            reporte.write('<table class="table table-hover table-striped">')
            reporte.write('<thead>')
            reporte.write('<tr>')
            reporte.write('<th>No.</th>')
            reporte.write('<th> Instruccion | Resultado </th>')
            reporte.write('</tr>')
            reporte.write('</thead>')
            reporte.write('<tbody>')
            contador4 = -1
            for obj in objectos:
                reporte.write('<tr>')
                reporte.write('<th class="row">' + str(contador4 + 1) + '</th>')
                contador4 += 1
                if obj.instruccion1 is True:
                    if obj.instruccion2 != None:
                        reporte.write('<td>' + memoria[contador4] + ' | ' + str(obj.id) + ': ' + 'ORDENADOS = ' + str(ordenar(obj)) + 'BUSQUEDA ' + str(obj.instruccion2) + ' = ' + buscar(obj) + '</td>')
                    elif obj.instruccion2 == None:
                        reporte.write('<td>' + memoria[contador4] + ' | ' + str(obj.id) + ': ' + 'ORDENADOS = ' + str(ordenar(obj))+ '</td>')

                elif obj.instruccion2 != None:
                    reporte.write('<td>' + memoria[contador4] + ' | ' + str(obj.id) + ': ' + 'BUSQUEDA ' + str(obj.instruccion2) + ' = ' + buscar(obj) + '</td>')

                else:
                    continue
                reporte.write('</tr>')

            reporte.write('</tbody>')
            reporte.write('</table>')
            reporte.write('</center>' + '\n')
            reporte.write('</body>' + '\n')
            reporte.write('</html>' + '\n')

            webbrowser.open('reporte.html')

    if comando == '6':
        print('=============')
        print('201906053')
        print('Jose Rodrigo Rodas Palencia')
        print('rodrigito49@gmail.com')
        print('Lenguajes Formales y de Programacion')
        print('=============')
        quit()

