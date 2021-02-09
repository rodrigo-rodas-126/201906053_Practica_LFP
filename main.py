import re
import webbrowser

memoria = []
objectos = []

class Linea:
    def __init__(self, id, lista, instruccion1=False, instruccion2=None):
        self.id = id
        self.lista = lista
        self.instruccion1 = instruccion1
        self.instruccion2 = instruccion2

    def imprimir(self):
        print(self.id)
        print(self.lista)
        print(self.instruccion1)

        if self.instruccion2 == None:
            print('None')
        else:
            print(self.instruccion2)

    def ordenar(self):
        if self.instruccion1 == False:
            return
        else:
            cadena = ''
            lista1 = self.lista
            for i in range(len(lista1)):
                peque = min(lista1)
                cadena += peque + ', '
                lista1.remove(peque)
            return cadena

    def buscar(self):
        if self.instruccion2 == None:
            return
        else:
            contador = 0
            validos = '{'
            for elemento in self.lista:
                contador += 1
                if elemento == self.instruccion2:
                    validos = validos + str(contador)
                    if contador < (len(self.lista) - 1):
                        validos += ','
                else:
                    continue
            validos += '}'
            return validos

"""
file = open('entrada.txt', 'r')
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
    a.imprimir()
    #print(objectos)
"""
"""
while True:
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

    if comando == '2':
        for obj in objectos:
            if obj.ordenar != None:
                print(obj.id + ': ' + 'ORDENADOS = ' + obj.ordenar )

    if comando == '3':
        for obj in objectos:
            if obj.buscar != None:
                print(obj.id + ': ' + 'BUSQUEDA' + ' obj.instruccion2 = ' + obj.buscar )

    if comando == '4':
        for obj in objectos:
            if obj.ordenar != None:
                print(obj.id + ': ' + 'ORDENADOS = ' + obj.ordenar )
            elif obj.buscar != None:
                print(obj.id + ': ' + 'BUSQUEDA' + ' obj.instruccion2 = ' + obj.buscar )

    if comando == '5':
        with open('reporte.html', 'w') as reporte:
            reporte.write('<html>')
            reporte.write('<head>')
            reporte.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
            reporte.write('<body>')
            reporte.write('<center>')
            for obj in objectos:
                if obj.ordenar() != None:
                    reporte.write('<p>' + str(obj.id) + ': ' + 'ORDENADOS = ' + str(obj.ordenar) + '</p>')
                else:
                    if obj.buscar() == None:
                        continue
                    else:
                        reporte.write('<p>' + str(obj.id) + ': ' + 'BUSQUEDA' +  str(obj.instruccion2) + ' = '  + str(obj.buscar) + '</p>')
            reporte.write('</center>')
            reporte.write('</body>')
            reporte.write('</html>')

            webbrowser.open('reporte.html')

    if comando == '6':
        print('=============')
        print('201906053')
        print('Jose Rodrigo Rodas Palencia')
        print('rodrigito49@gmail.com')
        print('Lenguajes Formales y de Programacion')
        print('=============')

    else:
        print('Comando desconocido')
        continue
"""