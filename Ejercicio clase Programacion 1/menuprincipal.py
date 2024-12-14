from menufinal import menu_libros 
from menufinal import menu_prestamo
from menufinal import menu_socio
from API import consultar_libros_por_autor




def menu_principal(menu_libros,menu_socio,menu_prestamo):
    print('Menú Principal:')
    print('A: Libros')
    print('B: Socios')
    print('C: Préstamos')
    print('D: CONSULTAR API')
    print('0: Salir')

    accion = input('Seleccione una opción: ')
    
    if accion == 'A':
        menu_libros()
    elif accion == 'B':
        menu_socio()
    elif accion == 'C':
        menu_prestamo()
    elif accion == 'D':
        consultar_libros_por_autor()  
    elif accion == '0':
        print('Gracias por usar nuestro programa.')
    else:
        print('Opción inválida. Por favor, seleccione una opción válida.')
menu_principal(menu_libros, menu_socio, menu_prestamo)     