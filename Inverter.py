import chardet
import os

# Limpia la terminal en función del OS
def clear():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

# Detecta la codificación del archivo
def detectar_codificacion(archivo):
    with open(archivo, 'rb') as f:
        resultado = chardet.detect(f.read())
    return resultado['encoding']

# Lee el archivo seleccionado linea a linea, invierte el orden de la lista de palabras y las guarda en un nuevo archivo
def inversor(archivo_entrada, archivo_salida):
    try:
        # Detecta la codificación del archivo de entrada
        codificacion = detectar_codificacion(archivo_entrada)
        
        # Lee el archivo con la codificación detectada
        with open(archivo_entrada, 'r', encoding=codificacion) as entrada:
            lineas = entrada.readlines() # Lee todas las líneas
        
        # Limpia e invierte las líneas
        lineas_invertidas = [linea.strip() for linea in lineas][::-1]
        
        # Escribe la lista invertida en el archivo de salida
        with open(archivo_salida, 'w', encoding='utf-8') as salida:
            salida.write('\n'.join(lineas_invertidas))  # Escribe cada palabra en una nueva línea
        
        print(f"\nEl archivo '{archivo_salida}' se ha creado con éxito.\n")  
    except FileNotFoundError:
        print(f"\nEl archivo '{archivo_entrada}' no se encuentra.\n")
    except Exception as e:
        print(f"\nOcurrió un error: {e}\n")

# Comienzo
clear()
print("\n******************** BIENVENIDO/A A SU INVERSOR DE LISTAS ********************\n")

# Recogemos las extensiones permitidas
print("Extensiones permitidas: .txt .doc .docx .xls .xlsx .csv\n\n")
extensiones_permitidas = ('.txt', '.doc', '.docx', '.xls', '.xlsx', '.csv')

# Nombre del archivo original
archivo_entrada = input("Introduzca el nombre del archivo con su extensión: ")
# Nombre del nuevo archivo
archivo_salida = input("\nIndique el nombre del nuevo archivo invertido con su extensión: ")

# Comprobamos la extensión, y si es correcta ejecutamos la función inversor
if archivo_entrada.endswith(extensiones_permitidas) and archivo_salida.endswith(extensiones_permitidas):
    inversor(archivo_entrada, archivo_salida)
elif not archivo_entrada.endswith(extensiones_permitidas) and archivo_salida.endswith(extensiones_permitidas):
    print("\nExtensión del archivo original no permitida\n")
elif not archivo_salida.endswith(extensiones_permitidas) and archivo_entrada.endswith(extensiones_permitidas):
    print("\nExtensión del nuevo archivo invertido no permitida\n")
else:
    print("\nExtensión de ambos archivos no permitida\n")