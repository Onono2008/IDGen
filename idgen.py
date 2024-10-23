import random
import string

# Generar un patrón de 8 números y una letra
def generar_patron():
    numeros = ''.join(random.choices(string.digits, k=8))
    letra = random.choice(string.ascii_uppercase)
    return numeros + letra

# Generar un nombre aleatorio
def generar_nombre():
    nombres = ['Juan', 'María', 'Carlos', 'Ana', 'Luis', 'Sofía', 'Pedro', 'Lucía']
    return random.choice(nombres)

# Generar dos apellidos aleatorios
def generar_apellidos():
    apellidos = ['González', 'Rodríguez', 'Fernández', 'López', 'Martínez', 'García', 'Pérez', 'Sánchez']
    apellido1 = random.choice(apellidos)
    apellido2 = random.choice(apellidos)
    return apellido1, apellido2

# Generar una dirección falsa
def generar_direccion():
    calles = ['Calle Falsa', 'Avenida Siempreviva', 'Calle Principal', 'Calle Luna', 'Calle Sol']
    numero = random.randint(1, 1000)
    ciudad = random.choice(['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao'])
    return f"{random.choice(calles)} {numero}, {ciudad}"

# Guardar la información en un archivo
def guardar_en_archivo(patron, nombre, apellidos, direccion):
    with open('datos_falsos.txt', 'w') as archivo:
        archivo.write(f"Patrón: {patron}\n")
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Apellidos: {apellidos[0]} {apellidos[1]}\n")
        archivo.write(f"Dirección: {direccion}\n")
    print("Datos guardados en 'datos_falsos.txt'.")

# Función principal
def main():
    patron = generar_patron()
    nombre = generar_nombre()
    apellidos = generar_apellidos()
    direccion = generar_direccion()
    
    guardar_en_archivo(patron, nombre, apellidos, direccion)

# Ejecutar el programa
if __name__ == '__main__':
    main()
