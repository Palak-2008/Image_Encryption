# STEP 1 : Import Required Module
from PIL import Image


# STEP 2 : Open Image

# Open image file (make sure image exists in same folder)
image = Image.open("input.jpeg.jpg")

# Display Image
image.show()

print("Image Loaded Successfully")

# STEP 3 : Convert Image into Pixels

pixels = image.load()

width, height = image.size

print("Image Size:", width, "x", height)

# STEP 4 : Encrypt Image Pixels

key = 50   # Secret Key (you can change)

for x in range(width):
    for y in range(height):

        r, g, b = pixels[x, y]

        # Encrypt RGB values
        r = (r + key) % 256
        g = (g + key) % 256
        b = (b + key) % 256

        pixels[x, y] = (r, g, b)

print("Image Encrypted Successfully")

# STEP 5 : Save Encrypted Image

image.save("encrypted_image.jpg")

print("Encrypted Image Saved Successfully")

# Show Encrypted Image
image.show()

# STEP 6 : Decrypt Image

# Open Encrypted Image
encrypted_image = Image.open("encrypted_image.jpg")

pixels = encrypted_image.load()

width, height = encrypted_image.size

key = 50   # SAME KEY MUST BE USED

for x in range(width):
    for y in range(height):

        r, g, b = pixels[x, y]

        # Reverse Encryption
        r = (r - key) % 256
        g = (g - key) % 256
        b = (b - key) % 256

        pixels[x, y] = (r, g, b)

encrypted_image.save("decrypted_image.jpg")

print("Image Decrypted Successfully")

encrypted_image.show()




