import tkinter as tk


class message():
    def __init__(self):
        text1='時間割ファイルが無いので作成します'
        text2='scombにログインしてください。その後は操作は必要ないです。'
        self.root = tk.Tk()
        self.root.geometry('350x60')
        button = tk.Button(self.root, 
                            text = 'OK', 
                            command=self.quit)
        label1=tk.Label(text=text1)
        label2=tk.Label(text=text2)
        label1.pack()
        label2.pack()
        button.pack()
        self.root.mainloop()

    def quit(self):
       self.root.destroy()

