# Not Complete This Projet Cuz I'm Not a App Developer


from tkinter import *
from tkinter import ttk


class todo():
	def __init__(self, root):
		self.root = root
		self.root.title("To Do List")
		self.root.geometry("650x410+200+150") 
		self.label = Label(self.root, text='Text To Do List', font='ariel, 25 bold',
			width=10, bd=5, bg='orange', fg='black')
		self.label.pack(side='top', fill=BOTH)
		self.labe2 = Label(self.root, text='Add Task', font='ariel, 10 bold',
			width=10, bd=5, bg='orange', fg='black')
		self.labe2.place(x=40, y=54)


def main():
	root = Tk()
	ui = todo(root)
	root.mainloop()


if __name__ == '__main__':
	main()