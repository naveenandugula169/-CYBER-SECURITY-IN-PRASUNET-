import os
from PIL import Image

def encrypt_image(input_path, output_path, key):
    try:
        # Open the image
        image = Image.open(input_path)
        pixels = image.load()

        # Get the size of the image
        width, height = image.size

        # Encrypt the image by adding the key to each pixel value
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

        # Save the encrypted image
        image.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except FileNotFoundError:
        print(f"File not found: {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(input_path, output_path, key):
    try:
        # Open the encrypted image
        image = Image.open(input_path)
        pixels = image.load()

        # Get the size of the image
        width, height = image.size

        # Decrypt the image by subtracting the key from each pixel value
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

        # Save the decrypted image
        image.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except FileNotFoundError:
        print(f"File not found: {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Use relative paths or dynamic paths based on your setup
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_image_path = os.path.join(current_directory, 'input.jpg')
    encrypted_image_path = os.path.join(current_directory, 'encrypted.jpg')
    decrypted_image_path = os.path.join(current_directory, 'decrypted.jpg')
    key = 42

    # Encrypt the image
    encrypt_image(input_image_path, encrypted_image_path, key)

    # Decrypt the image
    decrypt_image(encrypted_image_path, decrypted_image_path, key)
