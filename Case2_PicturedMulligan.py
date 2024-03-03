# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:52:14 2024

@author: admin
"""

#https://svgdb.me/assets/cards/en/C_125131020.png
from PIL import Image
import urllib.request
import requests  
#import urllib2
urllib.request.urlretrieve(
  'https://svgdb.me/assets/cards/en/C_125131010.png',
   "a1.png")
urllib.request.urlretrieve(
  'https://svgdb.me/assets/cards/en/C_125131020.png',
   "a2.png")  


site = 'https://svgdb.me/assets/cards/en/C_125131010.png'
hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
req = urllib.request(site, headers=hdr)
req = urllib.request(site)
img = Image.open("a1.png")
img.show()


img = Image.open("Mulligan2.png")
img2 = Image.open("Rey.png")
img.paste(img2)
img.show()


def get_concat_h(im1, im2, im3):
    dst = Image.new('RGBA', (im1.width + im2.width + im3.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    dst.paste(im3, (im1.width + im2.width, 0))
    return dst

im1 = Image.open("Follow - Rey.png")
im2 = Image.open("Spell - Funfact.png")
im3 = Image.open("Amulet - Laincrest.png")

im1 = Image.open("1.png")
im2 = Image.open("2.png")
im3 = Image.open("1.png")
dst = get_concat_h(im1,im2,im3)
dst.show()
dst.save('Test.png')



img_url = 'https://svgdb.me/assets/cards/en/C_125131010.png'
path = 'download.png'
r = requests.get(img_url, stream=True)
img = Image.open("download.png")
img.show()




import requests

url = 'https://svgdb.me/assets/cards/en/C_128114010.png'
r = requests.get(url)
with open('Spell - Funfact.png', 'wb') as outfile:
    outfile.write(r.content)
im1 = Image.open('0580_s03_qp_1.png')
im1.show()