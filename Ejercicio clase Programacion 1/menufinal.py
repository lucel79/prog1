import json
import os



def abrir_archivo(ruta):
    if os.path.exists(ruta) == False:
        return False
    archivo = open(ruta, 'r', encoding='utf-8')
    
    contenido = archivo.read()
  
    obj_json = json.loads(contenido)
        
    archivo.close()
    return obj_json


def crear_archivo(ruta):
    if os.path.exists(ruta) == True:
        return ruta
    archivo = open(ruta, 'w')
    lista_vacia = []
    string_lista = json.dumps(lista_vacia)
    archivo.write(string_lista)
    archivo.close()
    return ruta

def escribir_archivo(ruta, datos):
        
    if os.path.exists(ruta) == False:
        return False
    archivo = open(ruta, 'w')
    string_datos = json.dumps(datos)
    archivo.write(string_datos)
    archivo.close()
    return True

      
def listar_libros(ruta):
    libros = abrir_archivo(ruta)
    if len(libros) == 0:
        print('No hay libros en la Base de Datos.')
    for libro in libros:
        print(libro)
        
                
def agregar_libros(ruta):
    libros = abrir_archivo(ruta)
    quiere_salir = False
    print('Agregar libros: ')
    while quiere_salir == False:
          
        titulo = input('Ingrese titulo del libro: ')
        autor = input('Ingrese el nombre del autor:')
        editorial = input('Ingrese la editorial: ')
        fechapubli = input('Ingrese la fecha de publicacion ')
        genero = input('Ingrese el genero del libro: ')
        cantidad = input('Ingrese la cantidad : ')
       
        
        id_newlibro =0
        if len(libros) == 0:
            id_newlibro = 1
        else:
            ultimo_libro = libros[-1]
            id_viejo = ultimo_libro["id_libro"]
            id_newlibro = int(id_viejo)+ 1   
                
        libro = {
            'titulo':titulo,
            'autor': autor,
            'editorial':editorial,
            'fechapublicacion': fechapubli,
            'id_libro': id_newlibro,
            'genero': genero,
            'cantidad': cantidad,
                 
        }
        
        libros.append(libro)
        
        quiereSalir = input('Escriba SI si quiere salir, de lo contrario cualquier cosa: ')
        if quiereSalir == 'SI':
            quiere_salir = True

    escribir_archivo(ruta, libros)
    
    


def eliminar_libros(ruta):
    libros = abrir_archivo(ruta)
    titulo_elibro = input('Ingresar el titulo del libro a eliminar: ')
    for libro in libros:
        if libro['titulo'] == titulo_elibro:
           libros.remove(libro)
    
    escribir_archivo(ruta, libros)
    
def editar_libro(ruta):
    libros = abrir_archivo(ruta)
    eliminar_libros(ruta)
    libros = abrir_archivo(ruta)
    agregar_libros(ruta)
    
    escribir_archivo(ruta, libros)    

def buscar_libro(ruta):
    libros = abrir_archivo(ruta)
    libro_buscar = input('Ingresar el titulo del libro a buscar:')
    libro_encontrada = False
    for libro in libros:
        if libro['titulo'] == libro_buscar:
            libro_encontrada = True
            print(libro)
    if libro_encontrada == False:
        print('Libro no encontrada')
        
def buscar_autor(ruta):
    libros = abrir_archivo(ruta)
    autor_buscar = input('Ingresar el autor del libro a buscar:')
    libro_encontrada = False
    for libro in libros:
        if libro['autor'] == autor_buscar:
            libro_encontrada = True
            print(libro)
    if libro_encontrada == False:
        print('Libro no encontrada')        


def buscar_genero(ruta):
    libros = abrir_archivo(ruta)
    gene_buscar = input('Ingresar el genero del libro a buscar:')
    libro_encontrada = False
    for libro in libros:
        if libro['genero'] == gene_buscar:
            libro_encontrada = True
            print(libro)
    if libro_encontrada == False:
        print('Libro no encontrada')        

def buscar_editorial(ruta):
    libros = abrir_archivo(ruta)
    edi_buscar = input('Ingresar de la editorial del libro a buscar:')
    libro_encontrada = False
    for libro in libros:
        if libro['editorial'] == edi_buscar:
            libro_encontrada = True
            print(libro)
    if libro_encontrada == False:
        print('Libro no encontrada')     

###############################################


ruta = 'libros.json'
existe = abrir_archivo(ruta)
#Si no existe
if(existe == False):
    crear_archivo(ruta)


################MENU PRINCIPAL##################################


###############MENU LIBROS############################


def menu_libros():
    print('Menú Libros:')
    print('1: Listar libro ')
    print('2: Agregar libros')
    print('E: Editar libros')
    print('3: Borrar libro ')
    print('4: Buscar libro por titulo ')
    print('D: Buscar libro por autor')
    print('H: Buscar libro por genero')
    print('I: Buscar libro por editorial')
    
    print('5: Salir')

    accion_usuario = input('Seleccione una opción: ')
    
    if accion_usuario == '1':
            listar_libros(ruta)
    elif accion_usuario == '2':
            agregar_libros(ruta)
            listar_libros(ruta)                 
    elif accion_usuario == '3':
            eliminar_libros(ruta)
            listar_libros(ruta)
    elif accion_usuario == 'E':
            editar_libro(ruta)        
    elif accion_usuario == '4':
            buscar_libro(ruta)
    elif accion_usuario == 'D':    
            buscar_autor(ruta)
    elif accion_usuario == 'H':    
            buscar_genero(ruta)
    elif accion_usuario == 'I':    
            buscar_editorial(ruta)                     
    else:
        print('Opción inválida. Por favor, seleccione una opción válida.')
    accion_usuario = input('Seleccione una opción: ')    

################SOCIOS########################



def abrir_archivo(listado):
    if os.path.exists(listado) == False:
        return False
    archivo = open(listado, 'r', encoding='utf-8')
    
    contend = archivo.read()
  
    objson = json.loads(contend)
        
    archivo.close()
    return objson


def crear_archive(listado):
    
    if os.path.exists(listado) == True:
        return listado
    
    archiv = open(listado, 'w')
    lista_empty = []
    
    string_list = json.dumps(lista_empty)
    
    archiv.write(string_list)
    
    archiv.close()
    return listado

def escribir_archive(listado, dato):
        
    if os.path.exists(listado) == False:
        return False
    
    archiv = open(listado, 'w')
    
    string_dato = json.dumps(dato)
    
    archiv.write(string_dato)
   
    archiv.close()
    return True

def listar_socios(listado):
    socios = abrir_archivo(listado)
    if len(socios) == 0:
        print('No hay socios en la Base de Datos.')
    for persona in socios:
        print(persona)
        
def agregar_socios(listado):
    socios = abrir_archivo(listado)
    quiere_salir = False
    print('Agregar socio: ')
    while quiere_salir == False:
        
        
        nombre = input('Ingrese Nombre: ')
        apellido = input('Ingrese Apellido:')
        fechanac = input('Ingrese la fecha de nacimiento: ')
        direccion = input('Ingrese su direccion: ')
        email = input('Ingrese su correo electronico: ')
        tel = input('Ingrese su tel: ')
        
        id_newsocio = 0
        if len(socios) == 0:
            id_newsocio = 1
        else:
            ultimo_socio = socios[-1]
            id_viejosoc = ultimo_socio["id_socio"]
            id_newsocio = int(id_viejosoc)+ 1     
        
        persona = {
            'id_socio': id_newsocio,
            'nombre':nombre,
            'apellido':apellido,
            'fechanac': fechanac,
            'direccion': direccion,
            'email': email,
            'tel': tel,
                
        }
        
        socios.append(persona)
        
        quiereSalir = input('Escriba SI para salir, de lo contrario cualquier cosa: ')
        if quiereSalir == 'SI':
            quiere_salir = True

    escribir_archive(listado, socios)

def eliminar_socios(listado):
    socios = abrir_archivo(listado)
    eapellido_persona = input('Ingresar el apellido de la persona a eliminar:')
    for persona in socios:
        if persona['apellido'] == eapellido_persona:
            socios.remove(persona)
    
    escribir_archive(listado, socios)
    
def editar_socio(listado):
    socios = abrir_archivo(listado)
    eliminar_socios(listado)
    socios = abrir_archivo(listado)
    agregar_socios(listado)  
    
    escribir_archive(listado, socios)     
    

def buscar_socio(listado):
    socios = abrir_archivo(listado)
    apellido_persona = input('Ingresar el apellidos de la persona a buscar')
    persona_encontrada = False
    for persona in socios:
        if persona['apellido'] == apellido_persona:
            persona_encontrada = True
            print(persona)
    if persona_encontrada == False:
        print('Persona no encontrada')
                

listado = 'socio.json'
existe = abrir_archivo(listado)

if(existe == False):
    crear_archive(listado)

def menu_socio():
    print('Menú socio:')
    print('1: Listar socio: ')
    print('2: Agregar socio:')
    print('3: Borrar socio: ')
    print('4: Buscar socio: ')
    print('5: Editar socio:')
    print('6: Salir')

    accion_user = input('Seleccione una opción: ')
    
    if accion_user == '1':
            listar_socios(listado)
    elif accion_user == '2':
            agregar_socios(listado)
            listar_socios(listado)
    elif accion_user == '3':
            eliminar_socios(listado)
            listar_socios(listado)
    elif accion_user == '4':
            buscar_socio(listado)
    elif accion_user == '5':
            editar_socio(listado)        
    else:
        print('Opción inválida. Por favor, seleccione una opción válida.')
    accion_user = input('Seleccione una opción: ')



############ PRESTAMOS DEVOLUCIONES################ 

def abrir_archivo(listad):
    if os.path.exists(listad) == False:
        return False
    archivo = open(listad, 'r', encoding='utf-8')
    contenido = archivo.read()
    obj_json = json.loads(contenido)
    archivo.close()
    return obj_json


def crear_archivo(listad):
    
    if os.path.exists(listad) == True:
        return listad
    archivo = open(listad, 'w')
    lista_vacia = []
    string_lista = json.dumps(lista_vacia)
    archivo.write(string_lista)
    archivo.close()
    return listad

def escribir_archivo(listad, datos):
        
    if os.path.exists(listad) == False:
        return False
    
    archivo = open(listad, 'w')
    string_datos = json.dumps(datos)
    
    archivo.write(string_datos)
    archivo.close()
    return True

def listar_prestamo(listad):
    prestamo = abrir_archivo(listad)
    if len(prestamo) == 0:
        print('No hay personas en la Base de Datos.')
    for prestdev in prestamo:
        print(prestdev)
        
def agregar_prestamo(listad):
    prestamo = abrir_archivo(listad)
    quiere_salir = False
    print('Agregar datos del prestamo: ')
    while quiere_salir == False:
         
        idsocio = input('Ingrese el id del socio: ')
        estadopres = input('Ingrese el estado(EN CURSO) O (DEVUELTO): ')
        fechaprestamo = input('Ingrese la fecha del prestamo(dd/mm/aaaa): ')
        idlibro = input('Ingrese id del libro: ')
        fechdevo = input('Ingrese la fecha de devolucion: ')
        costo = input('Ingrese el costo : ')
        
        ultimo_prestamo = 0
        id_newprestamo = 0
        if len(prestamo) == 0:
            id_newprestamo = 1
        else:
            ultimo_prestamo = prestamo[-1]
            id_viejosoc = ultimo_prestamo["id_prestamo"]
            id_newprestamo = int(id_viejosoc)+ 1 
        
        
        prestdev = {
            'id_prestamo':id_newprestamo, 
            'idsocio':idsocio,
            'estadopres':estadopres,
            'fechaprestamo': fechaprestamo,
            'idlibro': idlibro,
            'fechdevo': fechdevo,
            'costo': costo,  
            
        }
        
        prestamo.append(prestdev)
       
        quiereSalir = input('Escriba SI para salir, de lo contrario cualquier cosa: ')
        if quiereSalir == 'SI':
            quiere_salir = True

    escribir_archivo(listad, prestamo)

def eliminar_prestamo(listad):
    prestamo = abrir_archivo(listad)
    id_prestamodev = input('Ingresar el id del prestamo a eliminar:')
    for prestdev in prestamo:
        if prestdev['id_prestamo'] == id_prestamodev:
           prestamo.remove(prestdev)
    
    escribir_archivo(listad, prestamo)


        

listad = 'prestamos1.json'
existe = abrir_archivo(listad)

if(existe == False):
    crear_archivo(listad)

def menu_prestamo():
    print('Menú prestamo:')
    print('1: Reporte de prestamo y devoluciones:')
    print('2: Agregar prestamo:')
    print('3: Eliminar prestamo:')
    
    print('5: Salir')

    accion_use = input('Seleccione una opción: ')
    while accion_use != 0:
        if accion_use == '1':
            listar_prestamo(listad)
        elif accion_use == '2':
            agregar_prestamo(listad)
            listar_prestamo(listad)
        elif accion_use == '3':
            eliminar_prestamo(listad)
            listar_prestamo(listad)
        elif accion_use == '5':
            print('Gracias por usar nuestro programa.')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida.')
        accion_use = input('Seleccione una opción: ') 

