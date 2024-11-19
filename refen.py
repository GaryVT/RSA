# Script para ordenar referencias alfabéticamente

def ordenar_referencias(input_file, output_file):
    # Abrir el archivo de entrada en modo lectura
    with open(input_file, 'r', encoding='utf-8') as f:
        # Leer todas las líneas del archivo
        referencias = f.readlines()

    # Eliminar saltos de línea y espacios en blanco innecesarios
    referencias = [referencia.strip() for referencia in referencias]

    # Ordenar las referencias alfabéticamente
    referencias_ordenadas = sorted(referencias)

    # Guardar las referencias ordenadas en un archivo de salida
    with open(output_file, 'w', encoding='utf-8') as f:
        for referencia in referencias_ordenadas:
            f.write(referencia + '\n')

    print(f'Referencias ordenadas y guardadas en: {output_file}')

# Especifica los nombres de tus archivos
input_file = 'referencias.txt'  # Archivo de entrada con las referencias
output_file = 'referencias_ordenadas.txt'  # Archivo de salida con las referencias ordenadas

# Llamar a la función para ordenar las referencias
ordenar_referencias(input_file, output_file)
