from tkinter import Tk,Button,Frame,Label,filedialog,messagebox
from zipfile import ZipFile
from os import path

root = Tk()
root.geometry("230x200+700+200")
root.title("Zarchiver")

def open_File(): # Function
    global file_paths
    file_paths = filedialog.askopenfilenames()


def zip_file():
    zip_path = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")])

    with ZipFile(zip_path, 'w') as l:
        for x in file_paths:
            path_1 = path.basename(x)
            l.write(x, arcname=path_1)
    messagebox.showinfo('Success','Files zipped successfully!')
    Done_popup.config(text='Done')



frame_1 = Frame(root)
frame_1.place(x=10,y=10)

browse_btn = Button(frame_1,command=open_File,width=8,text='Browse',background="#636363",foreground="white",font=('arial',10))
browse_btn.grid(row=0,column=0,padx=10,pady=10)

Done_popup = Label(root,text="Ready")
Done_popup.place(x=70,y=80)

strt_btn = Button(root,command=zip_file,width=8,text='Zip',background="#636363",foreground="white",font=('arial',11))
strt_btn.place(x=100,y=150)


root.mainloop()