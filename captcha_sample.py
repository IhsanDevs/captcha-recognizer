from PIL import Image, ImageDraw, ImageFont
import random

def generate_multicolor_captcha(width, height, font_path, font_size=25):
    # Membuat gambar blank dengan latar belakang putih
    captcha_image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(captcha_image)

    # Menggunakan font pixel
    pixel_font = ImageFont.truetype(font_path, font_size)

    # Menghasilkan teks numerik acak 4 digit
    captcha_text = ''.join(random.choices('0123456789', k=4))

    # Menentukan posisi awal teks
    text_x = 10
    text_y = (height - font_size) // 2

    # Menambahkan teks ke gambar dengan warna acak
    for char in captcha_text:
        text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.text((text_x, text_y), char, font=pixel_font, fill=text_color)
        text_x += font_size  # Menggeser posisi untuk karakter selanjutnya

    # Menambahkan noise pada gambar dengan warna acak
    for _ in range(width * height // 10):  # Jumlah pixel yang akan diubah menjadi noise
        noise_x = random.randint(0, width - 1)
        noise_y = random.randint(0, height - 1)
        noise_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.point((noise_x, noise_y), fill=noise_color)

    # Menampilkan gambar
    captcha_image.show()

    # Menyimpan gambar ke file
    # captcha_image.save('captcha_multicolor.png')

# Path font pixel
font_path = './rainyhearts.ttf'

# Panggil fungsi untuk menghasilkan captcha multicolor
generate_multicolor_captcha(128, 48, font_path)
exit()