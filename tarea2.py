import requests 

def opciones():
    r = int(input('\n¿Desea regresar a la pantalla principal? 1) Sí 2) No : '))
    if r==1:
        interfaz()
    else:
        print('\nMuchas gracias por usar nuestro aplicativo')

def interfaz():
    print('\nQUIÉN ES ESE POKEMON - MODULO 1 - BACK END - SILABUZ')
    print('Creadores: Jhonatan Panta | Kelly Romero')
    print('\nSeleccione la opción de la búsqueda que desea realizar:')
    print('\nOpción 1) Búsqueda por Generación\nOpción 2) Búsqueda por forma\nOpción 3) Búsqueda por habilidad\nOpción 4) Búsqueda por Hábitat\nOpción 5) Búsqueda por Tipo')
    op = int(input('Ingrese el número de la opción elegida: '))
    if op == 1:
        print('\n:: LISTADO DE POKEMONES POR GENERACIÓN ::')
        pokemon_generacion()
    elif op == 2:
        print('\n:: LISTADO DE POKEMONES POR FORMA ::')
        pokemon_forma()
    elif op == 3:
        print('\n:: LISTADO DE POKEMONES POR HABILIDADES ::')
        pokemon_habilidades()
    elif op == 4:
        print('\n:: LISTADO DE POKEMONES POR HABITAT ::')
        pokemon_habitat()
    elif op == 5:
        print('\n:: LISTADO DE POKEMONES POR TIPO ::')
        pokemon_tipo()
    else:
        opciones()

def pokemon_generacion():
    try:
        print('\nSeleccione la generación que desea listar')
        r = int(input('Ingrese de la 1era a la 8va generación: '))
        url = "https://pokeapi.co/api/v2/generation/"+str(r)+"/"
        r = requests.get(url)
        data = r.json()

        for indice, elemento in enumerate (data['pokemon_species']):
            print(indice+1,'->','Nombre: ',elemento['name'],'| URL: ', elemento['url'])
    except:
        print('Ocurrió un error, por favor inténtelo denuevo')
    finally:
        opciones()

def pokemon_habitat():
    try:
        print('Seleccione el habitat que desea listar\nOpción 1) Cave\nOpción 2) Forest\nOpción 3) Grassland\nOpción 4) Mountain\nOpción 5) Rare\nOpción 6) Rough-terrain\nOpción 7) Sea\nOpción 8) Urban\nOpción 9) Waters-edge')
        r = int(input('Ingrese el número de opción elegida: '))
        url = "https://pokeapi.co/api/v2/pokemon-habitat/"+str(r)+"/"
        print('\n == RESULTADOS DE BÚSQUEDA ==\n')        
        r = requests.get(url)
        data = r.json()
        for indice, elemento in enumerate (data['pokemon_species']):
            print(indice+1,'->','Nombre: ',elemento['name'],'| URL: ', elemento['url'])
    except:
        print('Ocurrió un error, por favor inténtelo denuevo')
    finally: 
        opciones()

def pokemon_tipo():
    try:
        url_opc = 'https://pokeapi.co/api/v2/type'
        data_opc = requests.get(url_opc).json()
        print('Seleccione el habitat que desea listar')
        for ind, elem in enumerate (data_opc['results']):
            print('Opción',ind+1,")",elem['name'])
        num = int(input('Ingrese el número de la opción elegida: '))
        print('\n == RESULTADOS DE BÚSQUEDA ==\n')
        url = "https://pokeapi.co/api/v2/type/"+str(num)+"/"
        r = requests.get(url)
        data = r.json()
        for indice, elemento in enumerate (data['pokemon']):
            print(indice+1,'->',elemento['pokemon']['name'], "| URL: ",elemento['pokemon']['url'] )
    except:
        print('Ocurrió un error, por favor inténtelo denuevo')
    finally: 
        opciones()

def pokemon_habilidades():
    try:
        url_opc = 'https://pokeapi.co/api/v2/ability/?offset=0&limit=267'
        data_opc = requests.get(url_opc).json()
        print('Seleccione la habilidad que desea listar')
        for ind, elem in enumerate (data_opc['results']):
            print('Opción',ind+1,")",elem['name'])
        num = int(input('Seleecione la opción que desea listar: '))
        print('\n == RESULTADOS DE BÚSQUEDA ==\n')
        url = "https://pokeapi.co/api/v2/ability/"+str(num)+"/"
        r  = requests.get(url)
        data = r.json()
        for indice, elemento in enumerate (data['pokemon']):
            print(indice+1,'->',elemento['pokemon']['name'], "| URL: ",elemento['pokemon']['url'] )
    except:
        print('Ocurrió un error, por favor inténtelo denuevo')
    finally:
        opciones()

def pokemon_forma():
    try:
        url_opc = 'https://pokeapi.co/api/v2/pokemon-form/?offset=0&limit=1323'
        data_opc = requests.get(url_opc).json()
        print('Seleccione la forma del pokemon que desea listar')
        for ind, elem in enumerate (data_opc['results']):
            print('Opción',ind+1,")",elem['name'])
        num = int(input('Seleecione la opción que desea listar: '))
        if num>905:
            num += 9095
        print('\n == RESULTADOS DE BÚSQUEDA ==\n')    
        url = "https://pokeapi.co/api/v2/pokemon-form/"+str(num)+"/"
        r  = requests.get(url)
        data = r.json()
        print('Pokemon :',data['pokemon']['name'])
        print('Nombre de forma : ',data['form_name'])
        print('Tipos : ',end="")
        for i in data['types']:
            print(i['type']['name'],end=" | ")
    except:
        print('Ocurrió un error, por favor inténtelo denuevo')
    finally:
        opciones()

interfaz()