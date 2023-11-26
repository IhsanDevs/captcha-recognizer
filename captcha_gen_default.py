from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import random
import os
from captcha.image import ImageCaptcha

import config

TEST_SIZE = 1000
TRAIN_SIZE = 50000
VALID_SIZE = 20000

#FLAGS = None
from PIL import Image, ImageDraw, ImageFont
import random

def generate_multicolor_captcha(captcha_text, path_to_save, width, height, font_path, font_size=28):
    # Membuat gambar blank dengan latar belakang putih
    captcha_image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(captcha_image)

    # Menggunakan font pixel
    pixel_font = ImageFont.truetype(font_path, font_size)

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

    # Menyimpan gambar ke file
    captcha_image.save(path_to_save, format='png')

# Path font pixel
font_path = './rainyhearts.ttf'

def gen(gen_dir, total_size, chars_num):
  if not os.path.exists(gen_dir):
    os.makedirs(gen_dir)
  for i in range(total_size):
    label = ''.join(random.sample(config.CHAR_SET, config.CHARS_NUM))
    # image.write(label, os.path.join(gen_dir, label+'_num'+str(i)+'.png'))
    generate_multicolor_captcha(label, os.path.join(gen_dir, label+'_num'+str(i)+'.png'), config.IMAGE_WIDTH, config.IMAGE_HEIGHT, font_path, font_size=28)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Change default value')

  parser.add_argument('--tedr',type=str,default='./data/test_data',help='Test data-set directory address')
  
  parser.add_argument('--tesz',type=int,default=TEST_SIZE,help='Number of test data-set')
  
  parser.add_argument('--trdr',type=str,default='./data/train_data',help='Train data-set directory adddress')
  
  parser.add_argument('--trsz',type=int,default=TRAIN_SIZE,help='Number of train data-set')
  
  parser.add_argument('--vadr',type=str,default='./data/valid_data',help='Validation data-set directory address')
  
  parser.add_argument('--vasz',type=int,default=VALID_SIZE,help='Number of validation data-set')


  FLAGS, unparsed = parser.parse_known_args()
  print('>> generate %d captchas in %s' % (FLAGS.tesz, FLAGS.tedr))
  gen(FLAGS.tedr, FLAGS.tesz, config.CHARS_NUM)
  print ('>> generate %d captchas in %s' % (FLAGS.trsz, FLAGS.trdr))
  gen(FLAGS.trdr, FLAGS.trsz, config.CHARS_NUM)
  print ('>> generate %d captchas in %s' % (FLAGS.vasz, FLAGS.vadr))
  gen(FLAGS.vadr, FLAGS.vasz, config.CHARS_NUM)
  print ('>> generate Done!')
