import requests

def consultar_libros_por_autor():
    author = input("Ingrese el nombre del autor: ")
    url = (f"https://openlibrary.org/search.json?author={author}")

    response = requests.get(url)
    data = response.json()

    if 'docs' in data:
        for libro in data['docs']:
            print(f"Titulo: {libro['title']}")
            print(f"Autor: {libro['author_name'][0]}")
            print("---------------------------------")
    else:
        print("No se encontraron libros para ese autor.")

#consultar_libros_por_autor()