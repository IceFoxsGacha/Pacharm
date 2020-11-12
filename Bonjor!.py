import tkinter, time , random

okno = tkinter.Tk()
okno.geometry('555x555')

holst = tkinter.Canvas(okno, width=555, height=555)
holst.pack()

zvezda = holst.create_polygon(
    20,40,
    33,66,
    90,40,
    fill='#bbffbb'
)

def nikita():
    return random.randrange(1,3)



x = 1
y = 2
while 1:
    holst.move(zvezda, x, y )
    okno.update()
    time.sleep(0.01)
    k = holst.coords(zvezda)
    print(k, k[4])
    if k[4]>555:
        x = -x * nikita()
    if k[0] < 0:
        x = -x * nikita()
    if k[5]>555:
        y = -y * nikita()
    if k[1] < 0:
        y = -y * nikita()



okno.mainloop()