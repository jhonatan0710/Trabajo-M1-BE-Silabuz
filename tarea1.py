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