import qrcode

url = input("Enter the url: ")

filename = input("The name of the url you want to save as: ")

if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)

