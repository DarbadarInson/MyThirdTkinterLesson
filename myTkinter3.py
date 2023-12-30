import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("@imdevana")
root.geometry("300x150")

photo = tk.PhotoImage(file="Assets/images.png")
photo2 = Image.open("Assets/images.png")
resized_image = photo2.resize((300,150), Image.ADAPTIVE)
converted_image = ImageTk.PhotoImage(resized_image)


label = tk.Label(root, image=converted_image, text="This is the label widget", width=300, height=150,
                 bg="black", fg="yellow")
label.pack()

root.mainloop()























