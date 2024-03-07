class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = {}

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("El libro con ISBN", isbn, "ha sido eliminado de la biblioteca.")
        else:
            print("El libro con ISBN", isbn, "no está disponible en la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios_registrados[usuario.user_id] = usuario
        print("El usuario", usuario.nombre, "se ha registrado en la biblioteca.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios_registrados:
            del self.usuarios_registrados[user_id]
            print("El usuario con ID", user_id, "ha sido dado de baja.")
        else:
            print("El usuario con ID", user_id, "no está registrado en la biblioteca.")

    def prestar_libro(self, isbn, user_id):
        if isbn in self.libros_disponibles:
            if user_id in self.usuarios_registrados:
                libro = self.libros_disponibles[isbn]
                usuario = self.usuarios_registrados[user_id]
                usuario.libros_prestados.append(libro)
                del self.libros_disponibles[isbn]
                print("El libro", libro.titulo, "ha sido prestado a", usuario.nombre)
            else:
                print("El usuario con ID", user_id, "no está registrado en la biblioteca.")
        else:
            print("El libro con ISBN", isbn, "no está disponible en la biblioteca.")

    def devolver_libro(self, isbn, user_id):
        if user_id in self.usuarios_registrados:
            usuario = self.usuarios_registrados[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print("El libro", libro.titulo, "ha sido devuelto.")
                    return
            print("El usuario no tiene prestado un libro con ISBN", isbn)
        else:
            print("El usuario con ID", user_id, "no está registrado en la biblioteca.")

    def buscar_libros_por_titulo(self, titulo):
        libros_encontrados = []
        for libro in self.libros_disponibles.values():
            if libro.titulo.lower() == titulo.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def buscar_libros_por_autor(self, autor):
        libros_encontrados = []
        for libro in self.libros_disponibles.values():
            if libro.autor.lower() == autor.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def buscar_libros_por_categoria(self, categoria):
        libros_encontrados = []
        for libro in self.libros_disponibles.values():
            if libro.categoria.lower() == categoria.lower():
                libros_encontrados.append(libro)
        return libros_encontrados

    def listar_libros_prestados_a_usuario(self, user_id):
        if user_id in self.usuarios_registrados:
            usuario = self.usuarios_registrados[user_id]
            print("Libros prestados a", usuario.nombre, ":")
            for libro in usuario.libros_prestados:
                print(libro.titulo)
        else:
            print("El usuario con ID", user_id, "no está registrado en la biblioteca.")


# Función para mostrar el menú y manejar las opciones del usuario
def mostrar_menu():
    print("\n--- Menú de la Biblioteca Digital ---")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros por título")
    print("8. Buscar libros por autor")
    print("9. Buscar libros por categoría")
    print("10. Listar libros prestados a un usuario")
    print("11. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            nuevo_libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(nuevo_libro)
            print("El libro ha sido agregado a la biblioteca.")
        elif opcion == "2":
            isbn = input("Ingrese el ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            user_id = input("Ingrese el ID del usuario: ")
            nuevo_usuario = Usuario(nombre, user_id)
            biblioteca.registrar_usuario(nuevo_usuario)
        elif opcion == "4":
            user_id = input("Ingrese el ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(user_id)
        elif opcion == "5":
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            user_id = input("Ingrese el ID del usuario: ")
            biblioteca.prestar_libro(isbn, user_id)
        elif opcion == "6":
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            user_id = input("Ingrese el ID del usuario: ")
            biblioteca.devolver_libro(isbn, user_id)
        elif opcion == "7":
            titulo = input("Ingrese el título del libro a buscar: ")
            libros_encontrados = biblioteca.buscar_libros_por_titulo(titulo)
            if libros_encontrados:
                print("Libros encontrados con el título", titulo, ":")
                for libro in libros_encontrados:
                    print(libro.titulo)
            else:
                print("No se encontraron libros con el título", titulo)
        elif opcion == "8":
            autor = input("Ingrese el autor del libro a buscar: ")
            libros_encontrados = biblioteca.buscar_libros_por_autor(autor)
            if libros_encontrados:
                print("Libros encontrados del autor", autor, ":")
                for libro in libros_encontrados:
                    print(libro.titulo)
            else:
                print("No se encontraron libros del autor", autor)
        elif opcion == "9":
            categoria = input("Ingrese la categoría del libro a buscar: ")
            libros_encontrados = biblioteca.buscar_libros_por_categoria(categoria)
            if libros_encontrados:
                print("Libros encontrados en la categoría", categoria, ":")
                for libro in libros_encontrados:
                    print(libro.titulo)
            else:
                print("No se encontraron libros en la categoría", categoria)
        elif opcion == "10":
            user_id = input("Ingrese el ID del usuario para listar sus libros prestados: ")
            biblioteca.listar_libros_prestados_a_usuario(user_id)
        elif opcion == "11":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
    #FUNCIONALIDADES AÑADIDAS:Añadir/quitar libros, Registrar/dar de baja usuarios, Prestar/devolver libros, Buscar libros.
    #INTERFAZ DE USUARIO: Se crea una función mostrar_menu() para mostrar un menú interactivo con las opciones disponibles para el usuario.
    #Eambien en la función main(), se utiliza un bucle while para permitir que el usuario seleccione opciones del menú y se realiza la lógica correspondiente según la opción seleccionada.