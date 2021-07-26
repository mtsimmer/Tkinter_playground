import tkinter
from PIL import ImageTk,Image


### #Solution using Canvas
### root = tkinter.Tk()
### root.attributes('-fullscreen', True)
### canvas = tkinter.Canvas(root)
### canvas.pack()
### img = ImageTk.PhotoImage(Image.open(r""))
### canvas.create_image(2,2,anchor=tkinter.NW,image=img)
### root.mainloop()

#Solution using Label
root = tkinter.Tk()
root.attributes('-fullscreen', True)
#Opening Image
#Fitting into size
img = Image.open(r"")
label_size = size_labels(root,num_labels=4)
#img = img.resize(label_size, Image.ANTIALIAS)
img.thumbnail(label_size, Image.ANTIALIAS)
img = ImageTk.PhotoImage(master=root,image=img)
label = tkinter.Label(master=root, image=img).grid(row=0,column=0)
#label.pack()

##Creating ExtraWindow ()
menu = tkinter.Toplevel(root)
#menu.geo
lbl = tkinter.Label(menu, text="menu")
amount = tkinter.Entry(menu,bd=2)
apply_btn = tkinter.Button(menu, text="apply", command=draw_check_boxes)
apply_btn.pack()
amount.pack()
#print(amount.get())
lbl.pack()

root.mainloop()


def size_labels(root,num_labels=4):
	"""This function determines the sizes of the labels 
	labels - the stuff the contains the pics
	param: root - a Tk object wich represents a window 
	param: num_labels - how many labels you plan on setting 
	returns: a tuple like (x,y) => (w,h)
	"""
	screen_w = root.winfo_screenwidth()
	screen_h = root.winfo_screenheight()
	#TODO add maximum %num==0 to determine maximal height devider
	return(int(screen_w/2),int(screen_h/2))

def draw_check_boxes():
	"""Called on change of the amount in the menu"""
	#TODO: Update the grid on the main page
	#TODO: 
	print(amount.get())

#|				|				|
#|				|				|
#|				|				|
#|				|				|
#|				|				|
#|--------------|---------------|
#|				|				|
#|				|				|
#|				|				|
#|				|				|
#|				|				|
