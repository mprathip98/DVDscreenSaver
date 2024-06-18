from tkinter import *
import time
import random

window = Tk()
window.geometry("1400x700")
window.title("helloTest")
window.config(background="black")

Width = 1400
Height = 700
xVelocity = 5
yVelocity = 5

canvas = Canvas(window, width=Width, height=Height, bg='black')
canvas.pack()

photoImage = PhotoImage(file='dvd.png')
imgX = random.randrange(1,1399)
imgY = random.randrange(1,699)
my_image = canvas.create_image(imgX,imgY,image=photoImage,anchor= NW)

imgWidth = photoImage.width()
imgHeight = photoImage.height()
print(imgWidth)


while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if coordinates[0] + imgWidth >= Width or coordinates[0]<= 0:
        xVelocity = -xVelocity

    if coordinates[1] + imgHeight >= Height or coordinates[1]<= 0:
        yVelocity = -yVelocity

    canvas.move(my_image, xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)



window.mainloop()