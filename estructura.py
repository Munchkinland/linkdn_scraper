import os

def generate_directory_structure(root_dir, output_file, indent=0):
    # Indentar según el nivel de profundidad
    spaces = ' ' * (indent * 4)
    
    with open(output_file, 'w') as file:
        def write_structure(current_dir, depth):
            with os.scandir(current_dir) as it:
                for entry in it:
                    file.write(f"{spaces}{entry.name}\n")
                    if entry.is_dir():
                        write_structure(entry.path, depth + 1)

        write_structure(root_dir, indent)

# Cambia 'estructura_del_proyecto.txt' por el nombre deseado para el archivo
output_file = 'estructura_del_proyecto.txt'
root_directory = '.'  # Usar el directorio actual

generate_directory_structure(root_directory, output_file)
print(f"Estructura del proyecto guardada en {output_file}")
