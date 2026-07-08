def leer_opcion():
    try:
        entrada = int(input("Ingrese opción: "))

        if entrada < 1 or entrada > 6:
            print("Ingrese un numero entero valido")
        else:
            return entrada
        
    except ValueError:
        print("Ingrese un numero entero valido")

def copias_genero(genero, diccionario_libros, diccionario_prestamos):
    total = 0

    for codigo_libro, argumentos_libros in diccionario_libros.items():
        if argumentos_libros[2] == genero.lower():
            for codigo_prestamos, argumentos_prestamos in diccionario_prestamos.items():
                if codigo_libro == codigo_prestamos:
                    total += argumentos_prestamos[1]

    print(f"El total de copias disponibles es: {total}")

def busqueda_multa(multa_min, multa_max, diccionario_libros, diccionario_prestamos):
    arreglo_libros_encontrados = []

    for clave_prestamos, argumentos_prestamos in diccionario_prestamos.items():
        if argumentos_prestamos[0] >= multa_min and argumentos_prestamos[0] <= multa_max:
            for clave_libros, argumentos_libros in diccionario_libros.items():
                if clave_libros == clave_prestamos and argumentos_prestamos[1] != 0:
                    arreglo_libros_encontrados.append(f"{argumentos_libros[0]}--{clave_libros}")

    if arreglo_libros_encontrados == []:
        print("No hay libros en ese rango de multa")
    else:
        arreglo_libros_encontrados.sort()
        print(f"Los libros encontrados son: {arreglo_libros_encontrados}")

def buscar_codigo(codigo, diccionario_prestamos):
    for clave_libros, argumentos_libros in diccionario_prestamos.items():
        if clave_libros == codigo.upper():
            return True
        else:
            continue
    return False

# en el return ademas del statement booleano se devuelven los diccionarios, ya que segun la guia no se pueden usar variables globales
def actualizar_multa(codigo, nueva_multa, diccionario_prestamos):
    existencia = buscar_codigo(codigo, diccionario_prestamos)

    if existencia == True:
        for clave_prestamos, argumentos_prestamos in diccionario_prestamos.items():
            if clave_prestamos == codigo.upper():
                argumentos_prestamos[0] = nueva_multa
                return True, diccionario_prestamos
    else:
        return False, diccionario_prestamos

def validar_codigo(codigo):
    codigo = codigo.strip(' ')
    if codigo != '':
        return True
    else:
        return False
    
def validar_titulo(titulo):
    titulo = titulo.strip(' ')
    if titulo != '':
        return True
    else:
        return False

def validar_autor(autor):
    autor = autor.strip(' ')
    if autor != '':
        return True
    else:
        return False

def validar_genero(genero):
    genero = genero.strip(' ')
    if genero != '':
        return True
    else:
        return False

def validar_ano(ano):
    if ano > 0:
        return True
    else:
        return False

def validar_editorial(editorial):
    editorial = editorial.strip(' ')
    if genero != '':
        return True
    else:
        return False

def validar_novedad(novedad):
    if novedad.lower == 'n':
        return False
    else:
        return True
    
def validar_multa(multa):
    if multa > 0:
        return True
    else:
        return False
    
def validar_copias(copias):
    if copias >= 0:
        return True
    else:
        return False

# en el return ademas del statement booleano se devuelven los diccionarios, ya que segun la guia no se pueden usar variables globales
def agregar_libros(codigo, titulo, autor, genero, ano, editorial, es_novedad, precio_multa, copias_disponibles, diccionario_libros, diccionario_prestamos):
    
    if buscar_codigo(codigo, diccionario_prestamos) == False:
        diccionario_libros.update({codigo: [titulo, autor, genero, ano, editorial, es_novedad]})
        diccionario_prestamos.update({codigo: [precio_multa, copias_disponibles]})
        return True, diccionario_libros, diccionario_prestamos
    else:
        return False, diccionario_libros, diccionario_prestamos

# en el return ademas del statement booleano se devuelven los diccionarios, ya que segun la guia no se pueden usar variables globales
def eliminar_libro(codigo, diccionario_libros, diccionario_prestamos):
    if buscar_codigo(codigo, diccionario_prestamos) == True:
        diccionario_libros.pop(codigo.upper())
        diccionario_prestamos.pop(codigo.upper())
        return True, diccionario_libros, diccionario_prestamos
    else:
        return False, diccionario_libros, diccionario_prestamos


libros = { 
    'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False], 
    'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True], 
    'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False], 
    'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False], 
    'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True], 
    'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False], 
}

prestamos = { 
    'L001': [500, 4], 
    'L002': [700, 0], 
    'L003': [300, 10], 
    'L004': [400, 2], 
    'L005': [600, 1], 
    'L006': [350, 6], 
}

while (True):

    print("========== MENÚ PRINCIPAL ==========") 
    print("1. Copias por género") 
    print("2. Búsqueda de libros por rango de multa") 
    print("3. Actualizar multa de libro") 
    print("4. Agregar libro") 
    print("5. Eliminar libro") 
    print("6. Salir") 
    print("=====================================") 

    opcion = leer_opcion()

    if opcion == 1:
        genero = input("Ingrese genero a consultar: ")
        copias_genero(genero, libros, prestamos)

    elif opcion == 2:
        while(True):
            try:
                #no se aplica restriccion de numeros enteros positivos, ya que el enunciado no dice explicitamente numeros enteros positivos, si no solo numeros enteros, por lo tanto solo se usa el try de ValueError
                valor_min = int(input("Ingrese multa mínima: "))
                valor_max = int(input("Ingrese multa máxima: "))
                busqueda_multa(valor_min, valor_max, libros, prestamos)
                break
            except ValueError:
                print("Debe ingresar valores enteros")

    elif opcion == 3:
        while(True):
            nuevo_codigo = input("Ingrese codigo del libro: ")
            try:
                nueva_multa = int(input("Ingrese nueva multa: "))
            except ValueError:
                print("Ingrese un valor entero positivo")
            
            validacion, prestamos = actualizar_multa(nuevo_codigo, nueva_multa, prestamos)

            if validacion == True:
                print("Si")
            else:
                print("No")
            repeticion = input("¿Desea actualizar otra multa (s/n)?:")
            if repeticion.lower() == 's':
                continue
            else:
                break

    elif opcion == 4:
        try:
            codigo = input("Ingrese código del libro: ").upper()
            titulo = input("Ingrese título: ")
            autor = input("Ingrese autor: ")
            genero = input("Ingrese género: ")
            ano = int(input("Ingrese año de publicación: "))
            editorial = input("Ingrese editorial: ")
            es_novedad = input("¿Es novedad? (s/n): ")
            precio_multa = int(input("Ingrese precio de multa: "))
            copias_disponibles = int(input("Ingrese copias disponibles: "))
        except ValueError:
            print("Ingrese numeros enteros validos")

        if validar_codigo(codigo) == False:
            print("El codigo no es valido")

        if validar_titulo(titulo) == False:
            print("El titulo no es valido")
        
        if validar_autor(autor) == False:
            print("El autor no es valido")

        if validar_genero(genero) == False:
            print("El genero no es valido")

        if validar_ano == False:
            print("El año no es valido")
        
        if validar_editorial(editorial) == False:
            print("La editorial no es valida")

        if validar_multa(precio_multa) == False:
            print("El precio de la multa no es valido")

        if validar_copias(copias_disponibles) == False:
            print("Las copias no son validas")

        if validar_novedad(es_novedad) == True:
            es_novedad = True
        else:
            es_novedad = False
        # se llama nuevamente a las funciones ya que se evita crear nuevas variables y usar mas memoria, esto debido a que la guia indica que los mensajes de validacion se deben realizar fuera de las funciones
        if validar_codigo(codigo) and validar_titulo(titulo) and validar_autor(autor) and validar_genero(genero) and validar_ano(ano) and validar_editorial(editorial) and validar_multa(precio_multa) and validar_copias and validar_copias(copias_disponibles):
            agregado, libros, prestamos = agregar_libros(codigo, titulo, autor, genero, ano, editorial, es_novedad, precio_multa, copias_disponibles, libros, prestamos)
        else:
            continue

        if agregado:
            print("Libro agregado")
        else:
            print("El código ya existe")

    elif opcion == 5:
        codigo = input("Ingrese codigo: ")
        codigo_encontrado, libros, prestamos = eliminar_libro(codigo, libros, prestamos)
        if codigo_encontrado == True:
            print("Libro eliminado")
        else:
            print("El código no existe")
            
    elif opcion == 6:
        print("Programa finalizado.")
        break