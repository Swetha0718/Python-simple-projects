import qrcode
img=qrcode.make("https://mail.google.com/mail/u/0/#inbox")
img.save("qr.jpg")