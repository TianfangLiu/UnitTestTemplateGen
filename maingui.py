from tkinter import *
from tkinter.filedialog import askopenfilename
import mainprint
import getfunctionlist


def selectPath():
    path_ = askopenfilename()
    path.set(path_)


def generatetemplate():
    filename = path.get()
    filename = filename.split("/")[-1]
    filename = filename.split(".")[0]
    mainprint.mainprint(filename,author.get(),getfunctionlist.getfunctionlist(path.get()))
    return None


if __name__ == '__main__':
    root = Tk()
    root.title("UnitTestTemplateGen")
    path = StringVar()
    author = StringVar()

    Label(root, text="Source code:").grid(row=0, column=0)
    Entry(root, textvariable=path).grid(row=0, column=1)
    Button(root, text="Select", command=selectPath).grid(row=0, column=2)
    Label(root, text="Author:").grid(row=1, column=0)
    Entry(root, textvariable = author).grid(row=1, column=1)
    Button(root, text="Generate Template", command=generatetemplate).grid(row=2, column=1)
    Button(root, text="Quit", command=root.quit).grid(row=2, column=2)

    root.mainloop()
