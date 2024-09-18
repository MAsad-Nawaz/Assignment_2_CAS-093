from tkinter import Image
image_path = 'home/assignment/softwar_now/image.png'

def process_string(s):
    number_str = ''.join([ch for ch in s if ch.isdigit()])
    letter_str = ''.join([ch for ch in s if ch.isalpha()])

    even_numbers = [int(n) for n in number_str if int(n) % 2 == 0]
    even_numbers_ascii = [ord(str(n)) for n in even_numbers]

    uppercase_letters = [ch for ch in letter_str if ch.isupper()]
    uppercase_ascii = [ord(ch) for ch in uppercase_letters]

    return even_numbers_ascii, uppercase_ascii


def modify_image(image_path, n):
    with Image.open(image_path) as img:
        pixels = img.load()
        for i in range(img.width):
            for j in range(img.height):
                r, g, b, a = pixels[i, j]
                pixels[i, j] = (r + n) % 256, (g + n) % 256, (b + n) % 256, a
        img.save("/mnt/data/sample1.png")
    return img


def sum_red_values(image):
    total_red = 0
    pixels = image.load()
    for i in range(image.width):
        for j in range(image.height):
            r, g, b, a = pixels[i, j]
            total_red += r
    return total_red


s = "56aAwW1984sktr235270aYmn145s785fsq31D0"
even_numbers_ascii, uppercase_ascii = process_string(s)
print("Even Numbers ASCII:", even_numbers_ascii)
print("Uppercase Letters ASCII:", uppercase_ascii)
n = sum(even_numbers_ascii + uppercase_ascii)
modified_image = modify_image(image_path, n)
