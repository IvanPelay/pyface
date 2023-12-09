from PIL import Image
import os

def redimensionar_y_rotar(imagen_path, salida_path, nuevo_tamano, rotar=False):
    # Abre la imagen
    imagen = Image.open(imagen_path)
    
    # Redimensiona la imagen
    nueva_imagen = imagen.resize(nuevo_tamano)
    
    # Rotar la imagen si se especifica
    if rotar:
        nueva_imagen = nueva_imagen.rotate(-90)  # Rotación de 90 grados en sentido de las manecillas del reloj
    
    # Guarda la nueva imagen
    nueva_imagen.save(salida_path)

def redimensionar_carpeta(carpeta_entrada, carpeta_salida, nuevo_tamano, rotar=False):
    # Asegúrate de que la carpeta de salida exista
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Lista todos los archivos en la carpeta de entrada
    archivos = os.listdir(carpeta_entrada)

    for archivo in archivos:
        # Ruta completa de la imagen de entrada
        entrada_path = os.path.join(carpeta_entrada, archivo)

        # Ruta completa de la imagen de salida
        salida_path = os.path.join(carpeta_salida, archivo)

        # Redimensiona y rota la imagen
        redimensionar_y_rotar(entrada_path, salida_path, nuevo_tamano, rotar)

if __name__ == "__main__":
    # Especifica la carpeta de entrada y salida, así como el nuevo tamaño y si se debe rotar
    carpeta_entrada = r"C:\Users\pelay\Desktop\proyecto toro\n"
    carpeta_salida = r"C:\Users\pelay\Desktop\proyecto toro\nn"
    nuevo_tamano = (40 , 40)  # Cambia esto al tamaño deseado
    rotar_imagenes = True

    # Redimensiona y rota la carpeta completa
    redimensionar_carpeta(carpeta_entrada, carpeta_salida, nuevo_tamano, rotar_imagenes)