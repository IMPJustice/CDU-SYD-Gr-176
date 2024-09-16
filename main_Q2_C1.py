from Question2_chapter1 import *
def main():
    n=generated_number
    
    #Load image data
    img = Image.open('chapter1.jpg')
    pixels = img.load()
    width, height = img.size
    red_sum = 0
    
    # Start modifying image
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
if __name__ == "__main__":
    main()