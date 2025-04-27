#encoding qr code
import qrcode
#creating qr with link
img = qrcode.make("https://www.youtube.com/")
#qr with text
img = qrcode.make("Thailand is a country with many religions. I love Thailand.")
#save  You can name anything.
img.save("myQRCode.jpg")
