import math

usb_size = int(input('Enter USB size (GB): '))

size_byte = usb_size * 1000000000

gif_size = 800*600/5
jpeg_size = 800*600*3/25
png_size = 800*600*3/8
tiff_size = 800*600*6


print(format(math.floor(size_byte/gif_size), '>5'), 'images in GIF format can be stored')
print(format(math.floor(size_byte/jpeg_size), '>5'), 'images in JPEG format can be stored')
print(format(math.floor(size_byte/png_size), '>5'), 'images in PNG format can be stored')
print(format(math.floor(size_byte/tiff_size), '>5'), 'images in TIFF format can be stored')