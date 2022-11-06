import requests 

# Opc1. Listar pokemones por egneración (Ignresar int) OK
# Opc2. Listar pokemones por forma (sugerir valores) -- Kelly
# Opc3. Listar pokemones por habilidad -- Kelly
# Opc4. Listar pokemones por habitat -- Jhonatan
# Opc5. Listar pokemones por tipo -- Jhonatan

def opciones():
    r = int(input('\n¿Desea regresar a la pantalla principal? 1) Sí 2) No : '))
    if r==1:
        intefaz()
    else:
        print('\nMuchas gracias por usar nuestro aplicativo')

def intefaz():
    # Se pone las 5 opciones para la elección del usuario
    pass

def pokemon_generacion():
    try:
        print('Seleccione la generación que desea listar')
        r = int(input('Ingrese de la 1era a la 8va generación: '))
        url = "https://pokeapi.co/api/v2/generation/"+str(r)+"/"
        r = requests.get(url)
        data = r.json()

        for indice, elemento in enumerate (data['pokemon_species']):
            print(indice+1,'->',elemento['name'])
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
            print(indice+1,'->',elemento['name'])
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
            print(indice+1,'->',elemento['pokemon']['name'])
    except:
        print('Ocurrió un error, por favor inténtelo denuevo')
    finally: 
        opciones()