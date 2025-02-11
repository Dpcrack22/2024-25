from PIL import Image
import numpy as np

def image_to_ascii(image_path, width=100):
    # Conjunto de caracteres con mejor contraste
    ascii_chars = "⣿⩶⩴⩦⩤⩀⠿⠛⠉ "
    
    # Cargar imagen y convertir a escala de grises
    image = Image.open(image_path).convert("L")
    
    # Ajustar la altura proporcionalmente para evitar distorsión
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio * 0.6)  # Ajuste de proporción
    image = image.resize((width, new_height))
    
    # Convertir píxeles a ASCII
    pixels = np.array(image)
    ascii_image = "\n".join(
        "".join(ascii_chars[pixel // 32] for pixel in row) for row in pixels
    )
    
    return ascii_image

if __name__ == "__main__":
    image_path = input("Escribe la ruta de la imagen: ")
    ascii_art = image_to_ascii(image_path)
    print(ascii_art)