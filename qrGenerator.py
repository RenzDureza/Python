import qrcode

img = qrcode.make("I love you baby<3")
type(img)
img.save("qr.png")