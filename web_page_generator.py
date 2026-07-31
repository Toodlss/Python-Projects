import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.lbl = Label(self.master, text="Enter custom HTML text:")
        self.lbl.grid(row=0, column=0, columnspan=200, pady=(10, 5))

        self.entry = Entry(width=100)
        self.entry.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, padx=(10,10), pady=(10,10))

        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=2, column=1, padx=(10,10), pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        htmlText = self.entry.get()

        if htmlText == "":
            htmlText = "You forgot to put an entry"

        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
