import csv
from encodings import utf_8

class Libro:

  def __init__(self,id,titulo,genero,isbn,editorial, autor):
    self.id =  id
    self.titulo = titulo
    self.genero = genero
    self.isbn = isbn
    self.editorial = editorial
    self.autor = autor
  def getid(self):
    return self.id
  def gettitulo(self):
    return self.titulo
  def getgenero(self):
    return self.genero    
  def geteditorial(self):
    return self.editorial
  def getisbn(self):
    return self.isbn
  def getautor(self):
    return self.autor
  def settitulo(self, titulo):
    self.titulo = titulo
  def setgenero(self, genero):
    self.genero = genero
  def setisbn(self, isbn):
    self.isbn = isbn
  def seteditorial(self, editorial):
    self.editorial = editorial
  def setautor(self, autor):
    self.autor = autor  
  def fila(self):
    print(f"{self.id}\t{self.titulo}\t{self.genero}\t{self.isbn}\t{self.editorial}\t{self.autor}")
  def write_txt(self):
    autores = "|".join(self.autor)
    return f'{self.id},{self.titulo},{self.genero},{self.isbn},{self.editorial},{autores}'

# Opción 1: Leer archivos del disco duro

libros_dd = []
titulos = ['ID','Nombre de Libro','Género Literario','ISBN','Editorial','Autor(es)']

def header():
  print()
  for head in titulos:
    print(head,end="\t")
  print()

def leer_archivo():
    archivo = input('Ingresar ruta de archivo: ')

    if (archivo[-3:len(archivo)] == "csv"):        
        with open(archivo,encoding="utf-8") as csv_file:
            csv_objeto = csv.reader(csv_file)
            for row in csv_objeto:
                libros_dd.append(Libro(row[0],row[1],row[2],row[3],row[4],row[5].split("|")))
        csv_file.close()
    elif (archivo[-3:len(archivo)] == "txt"):
        archivotxt = open(archivo,"r",encoding="utf-8")
        leer = archivotxt.readlines()
        for row in leer:
            row = row.strip("\n").split(",")
            libros_dd.append(Libro(row[0],row[1],row[2],row[3],row[4],row[5].split("|")))
        archivotxt.close()
    else:
        print("Ingrese el archivo correcto (.csv o .txt)")
    
    libros_dd.pop(0)
    
    header()
    for i in range (3):
        libros_dd[i].fila()

    fin_opciones()
# Opción 2: Listar archivos

def listar():
  header()
  for elem in libros_dd:
    elem.fila()
  
  fin_opciones()

# Opción 3: Agregar libro

def agregar_libro():
    id = int(input('\nIngresar ID de Libro:\t'))
    titulo = input('Ingrese título de libro:\t')
    genero = input('Ingrese género del libro:\t')
    isbn = input('Ingrese ISBN del libro:\t')
    editorial = input('Ingrese editorial del libro:\t')
    autor = []
    cant = int(input('Ingrese cantidad de autores:\t'))
    for i in range (1,cant+1):
      autor.append(input(f'Ingrese el {i}° autor : \t'))
    print(f'\nID de Libro: {id}\nTitulo: {titulo}\nGenero: {genero}\nISBN: {isbn}\nEditorial: {editorial}\nAutor: {autor}')
    r = int(input('¿Estas seguro que deseas ingresar este libro?\n\t1) Sí\t2) No\n'))
    if r == 1:
      libro_nuevo = Libro(id,titulo,genero,isbn,editorial,autor)
      libros_dd.append(libro_nuevo)
      fin_opciones()
    else:
      print('Lo regresaremos al menú principal')
      interfaz()

# Opción 4:

def eliminar_libro():
  try:
    id = int(input('Ingrese la ID del Libro a eliminar: '))
    encontrado = False
    for i,e in enumerate(libros_dd):
      if int(e.getid()) == id:
        r = int(input('¿Estás seguro que desea eliminar el Libro?\n1) Sí\n2)No\nIngrese respuesta:'))
        encontrado = True
        if r==1:
          libros_dd.pop(i)
          print('Libro eliminado con éxito')
          fin_opciones()
        else:
          print('Lo dirigriremos a la pantalla principal')
          interfaz()
    if encontrado == False:
      print('El libro no se encuentra en la base de datos\nSerá dirigido a la pantalla principal')
      interfaz()
  except:
    print('Ocurrió un error, por favor revise los datos ingresados\nSerá digirido a la pantalla principal...')
    interfaz()

# Opción 5:
def buscar_isbn_titulo():
  try:
    print("Elija opción de busqueda:\n 1 = ISBN\n 2 = TÍTULO")
    opcion = int(input("Escriba la opción elegida: "))
    resultado = []
    if opcion == 1:
        isbnlibro = input("ingrese el ISBN del libro: ")
        for elemento in libros_dd:
            if (elemento.getisbn() == isbnlibro):
                resultado.append(elemento)
    elif opcion == 2:
        titulolibro = input("ingrese el TÍTULO del libro: ")
        resultado = []
        for elemento in libros_dd:
            if (elemento.gettitulo() == titulolibro):
                resultado.append(elemento)
    print('\nResultados de la búsqueda')
    header()
    for i in resultado:
      i.fila()
  except:
    print('Ocurrió un problema')
  finally:
    fin_opciones()

# Opción 6:

def ordenar_titulo():
  index = [i for i in range (len(libros_dd))]
  titulos = [elemento.gettitulo() for elemento in libros_dd]
  zipped = zip(titulos,index)
  print('Lista ordenada por título de libro:')
  header()
  for t,i in sorted(zipped):
    libros_dd[i].fila()
  fin_opciones()

# Opcion 7
def buscar_autor_editorial_genero():
  try:
    print("Elija la opción a buscar:\n 1 = AUTOR\n 2 = EDITORIAL\n 3 = GÉNERO")
    opcion = int(input("Seleccione la forma de busqueda"))
    resultado = []
    if opcion == 1:
          autorlibro = input("Ingrese el NOMBRE del autor buscado")
          for elemento in libros_dd:
              if autorlibro in elemento.getautor():
                  resultado.append(elemento)
    elif opcion == 2:
        editoriallibro = input("Ingrese el nombre de la EDITORIAL a buscar ")
        for elemento in libros_dd:
            if (elemento.geteditorial() == editoriallibro):
                resultado.append(elemento)
    elif opcion == 3:
          generolibro = input("Ingrese el GÉNERO a buscar")
          for elemento in libros_dd:
              if (elemento.getgenero() == generolibro):
                  resultado.append(elemento)
    print('\nResultados de la búsqueda')
    header()
    for i in resultado:
      i.fila()
  except:
    print('\nOcurrió un problema')
  finally:
    fin_opciones()

# Opcion 8
def buscar_nro_autores():
  try:
    numerodeautores = int(input("ingrese la NÚMERO de autores buscados"))
    resultado = []
    for elemento in libros_dd:
      if (len(elemento.getautor()) == numerodeautores):
        resultado.append(elemento)
    print('\nResultados de la búsqueda')
    header()
    for i in resultado:
      i.fila()
  except:
    print('\nOcurrión un problema')
  finally:
    fin_opciones()
# Opcion 9

def editar_libro():
  try: 
    id = int(input('Ingrese el ID del Libro a editar: '))
    encontrado = False
    for index, elemento in enumerate(libros_dd):
      if int(elemento.getid()) == id:
        indice = index
        encontrado = True
        break
    if encontrado==True:
      print(f'\nDatos actuales del libro de ID = {id} ')
      header()
      libros_dd[indice].fila()
      libros_dd[indice].settitulo(input('Ingrese título:\t'))
      libros_dd[indice].setgenero(input('Ingrese género literario:\t'))
      libros_dd[indice].setisbn(input('Ingrese ISBN:\t'))
      libros_dd[indice].seteditorial(input('Ingrese la editorial:\t'))
      r = int(input('Ingresar la cantidad de autores:\t'))
      autor=[]
      for i in range (1,r+1):
        autor.append(input(f'Ingrese el {i}° autor:\t'))
      libros_dd[indice].setautor(autor)
      print(f'\nDatos actualizados del libro de ID = {id} ')
      header()
      libros_dd[indice].fila()
    else:
      print('\nLibro no encontrado')
  except:
    print('\nIngrese una ID de Libro correcta.')
  finally:
    fin_opciones()

# Opcion 10
def guardar():
  try:
    archivo = input('Ingresar ruta de archivo: ')

    if (archivo[-3:len(archivo)] == "csv"):   
      archivocsv = open(archivo,"w",encoding="utf-8",newline="")
      campos = ['ID','Nombre de Libro','Género Literario','ISBN','Editorial','Autor(es)']
      escribir = csv.DictWriter(archivocsv,fieldnames=campos)
      escribir.writeheader()
      data = []
      for elem in libros_dd:
        autor = "|".join(elem.getautor())
        aux = {titulos[0]:elem.getid(), titulos[1]:elem.gettitulo(), titulos[2]:elem.getgenero(), titulos[3]:elem.getisbn(), titulos[4]:elem.geteditorial(), titulos[5]:autor}
        data.append(aux)
      escribir.writerows(data)
      archivocsv.close()
      print('\n:: Archivo guardado con éxito ::')
    elif (archivo[-3:len(archivo)] == "txt"):
      archivotxt = open(archivo,"w",encoding="utf-8",newline="")
      data=[]
      campos = [F'ID,Nombre de Libro,Género Literario,ISBN,Editorial,Autor(es)']
      for elem in libros_dd:
        autores = "|".join(elem.getautor())
        aux = f'\n{elem.getid()},{elem.gettitulo()},{elem.getgenero()},{elem.getisbn()},{elem.geteditorial()},{autores}'
        data.append(aux)
      data = campos + data
      archivotxt.writelines(data)
      archivotxt.close()
      print('\n:: Archivo guardado con éxito ::')
  except:
    print('Ocurrió un error')
  finally:
    fin_opciones()
  
# Interfaz
def interfaz():
  try:
    print("\nBACKEND - Modulo 1 - Trabajo final\nAutores: Jhonatan Panta | Kelly Romero\n")
    print(f'Opción 1) Leer archivo (csv o txt)\nOpción 2) Listar libros\nOpción 3) Agregar libro\nOpción 4) Elminar libro\nOpción 5) Buscar libro por ISBN o Título\nOpción 6) Ordenar libros por título\nOpción 7) Buscar libros por autor, editorial o género\nOpción 8) Buscar libro por número de autores\nOpción 9) Editar libro\nOpción 10) Guardar libros en archivo csv O txt')
    opcion = int(input('\nIngresar el número de opción: '))

    if opcion==1:
      print('\n:: LEER ARCHIVO csv o txt ::\n')
      leer_archivo()

    elif opcion==2:
      print('\n:: LISTAR LIBROS ::\n')
      listar()
    elif opcion==3:
      print('\n:: AGREGAR LIBRO ::\n')
      agregar_libro()
    elif opcion==4:
      print('\n:: ELIMINAR LIBRO ::\n')
      eliminar_libro()
    elif opcion==5:
      print('\n:: BUSCAR LIBRO POR ISBN O TÍTULO ::\n')
      buscar_isbn_titulo()
    elif opcion==6:
      print('\n:: ORDENAR LIBROS POR TÍTULO ::\n')
      ordenar_titulo()
    elif opcion==7:
      print('\n:: BUSCAR LIBROS POR AUTOR, EDITORIAL O GÉNERO ::\n')
      buscar_autor_editorial_genero()
    elif opcion==8:
      print('\n:: BUSCAR LIBROS POR CANTIDAD DE AUTORES ::\n')
      buscar_nro_autores()
    elif opcion==9:
      print('\n:: EDITAR LIBROS ::\n')
      editar_libro()
    elif opcion==10:
      print('\n:: GUARDAR LIBROS EN ARCHIVO ::\n')
      guardar()
  except:
    print('Ingrese la opción correcta...')
    fin_opciones()

def fin_opciones():
  r = int(input(f'\n¿Desea regresar a la interfaz?:\n1) Sí\n2) No\n\nIngrese el número de la opción: '))
  if r==1:
    interfaz()
  else:
    print('Gracias por usar nuestro aplicativo')

interfaz()