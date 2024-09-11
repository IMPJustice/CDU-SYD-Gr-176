from PIL import Image
import time

current_time=int(time.time())
generated_number=(current_time %100) +50

if generated_number %2 == 0:
    
    generated_number +=10
    
print(generated_number)

n=generated_number

img = Image.open('chapter1.jpg')
pixels = img.load()

width, height = img.size
red_sum = 0

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        # Modify the pixel values
        new_r = min(r + n, 255)
        new_g = min(g + n, 255)
        new_b = min(b + n, 255)
        # Set the new pixel value
        pixels[i, j] = (new_r, new_g, new_b)
        # Accumulate the red value
        red_sum += new_r
        
img.save('chapter1out.jpg')

print("Sum of red pixels in the new image:", red_sum)