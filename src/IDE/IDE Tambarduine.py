import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from collections import deque
import os
from src.Compiler.Compiler import Compiler
from src.Lexxer.Lex import keywords, booleanOps, hits
from tkinter.filedialog import askopenfilename, asksaveasfilename


class LineNumbers(tk.Text):  # Clase para que se vea numeros al margen
	def __init__(self, master, text_widget, **kwargs):
		super().__init__(master, **kwargs)

		self.text_widget = text_widget
		self.text_widget.bind('<KeyPress>', self.on_key_press)

		self.insert(1.0, '1')
		self.configure(state='disabled')

	def on_key_press(self, event=None):
		final_index = str(self.text_widget.index(tk.END))
		num_of_lines = final_index.split('.')[0]
		line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
		width = len(str(num_of_lines))
		w1 = 1 / width
		w2 = 1 / (int(num_of_lines) - 1)
		wCorrection = w1 - w2
		textY = self.text_widget.yview()[0] - wCorrection

		self.configure(state='normal', width=width)
		self.delete(1.0, tk.END)
		self.insert(1.0, line_numbers_string)
		self.configure(state='disabled')
		self.yview('moveto', textY)

	def clear(self):
		final_index = str(self.text_widget.index(tk.END))
		num_of_lines = final_index.split('.')[0]
		line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
		width = len(str(num_of_lines))
		self.configure(state='normal', width=width)
		self.delete(1.0, tk.END)
		self.configure(state='disabled')


class Window:
	def __init__(self, master):
		self.rutina = ''
		self.master = master
		self.master.option_add("*Font", "Verdana 11")  # Letra

		self.Compiler = Compiler()

		self.stack = deque(maxlen=10)
		self.stackcursor = 0

		# ---------

		self.T1 = Text(self.master, width=66, height=20)  # Cuadro de entrada de texto del IDE
		self.LineN = LineNumbers(self.master, self.T1, width=1, height=20)

		self.T1["yscrollcommand"] = self.autoScroll
		self.LineN["yscrollcommand"] = self.autoScroll

		self.LineN.place(x=90, y=50)
		self.T1.place(x=115, y=50)

		self.T1.tag_configure("orange", foreground="orange", font="Verdana 12")
		self.T1.tag_configure("blue", foreground="blue", font="Verdana 12")
		self.T1.tag_configure("purple", foreground="purple", font="Verdana 12")
		self.T1.tag_configure("green", foreground="green", font="Verdana 12")
		self.T1.tag_configure("red", foreground="red", font="Verdana 12")

		self.tags = ["orange", "blue", "purple", "green", "red"]

		self.wordlist = [
			["class", "Def", "for", "If", "Else", "elif", "import", "from", "as", "break", "while", "Set", "Exec"],
			["int", "string", "float", "bool", "__init__", "@x"],
			["pygame", "tkinter", "sys", "os", "mysql"],
			["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
			["+", "=", "-", "*", "**", "/", "//", "%"]]

		self.T1.bind("<Return>", lambda event: self.indent(event.widget))

		# ---------

		self.menu = Menu(self.master)
		self.menu.add_command(label="Undo", command=self.undo)
		self.menu.add_command(label="Redo", command=self.redo)
		self.menu.add_command(label="Save File", command=self.FileNameS)
		self.menu.add_command(label="Open File", command=self.FileNameL)

		self.master.config(menu=self.menu)

		# Botones
		self.B1 = Button(self.master, text="Compilar", command=self.display)
		self.B1.place(x=160, y=425)

		self.B2 = Button(self.master, text="Clear", command=self.clear)
		self.B2.place(x=670, y=425)

		self.B3 = Button(self.master, text="Ejecutar y Compilar", command=self.ExecDisplay)
		self.B3.place(x=370, y=425)

		# Cuadro de salida
		self.printwindow = Text(self.master, width=70, height=10, background="black", fg="white")
		self.printwindow.place(x=90, y=460)

	def tagHighlight(self):  # Funcion para demarcar con color las palabras o simbolos reservados
		start = "1.0"
		end = "end"

		for mylist in self.wordlist:
			num = int(self.wordlist.index(mylist))

			for word in mylist:
				self.T1.mark_set("matchStart", start)
				self.T1.mark_set("matchEnd", start)
				self.T1.mark_set("SearchLimit", end)

				mycount = IntVar()

				while True:
					index = self.T1.search(word, "matchEnd", "SearchLimit", count=mycount, regexp=False)

					if index == "": break
					if mycount.get() == 0: break

					self.T1.mark_set("matchStart", index)
					self.T1.mark_set("matchEnd", "%s+%sc" % (index, mycount.get()))

					preIndex = "%s-%sc" % (index, 1)
					postIndex = "%s+%sc" % (index, mycount.get())

					if self.check(index, preIndex, postIndex):
						self.T1.tag_add(self.tags[num], "matchStart", "matchEnd")

	def check(self, index, pre, post):  # Funcion de revision del abecedario
		letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
		           "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

		if self.T1.get(pre) == self.T1.get(index):
			pre = index
		else:
			if self.T1.get(pre) in letters:
				return 0

		if self.T1.get(post) in letters:
			return 0

		return 1

	def scan(self):  # Funcion que escanea las palabras en cada linea
		start = "1.0"
		end = "end"
		mycount = IntVar()

		regex_patterns = [r'".*"', r'#.*']

		for pattern in regex_patterns:
			self.T1.mark_set("start", start)
			self.T1.mark_set("end", end)

			num = int(regex_patterns.index(pattern))

			while True:
				index = self.T1.search(pattern, "start", "end", count=mycount, regexp=True)

				if index == "": break

				if (num == 1):
					self.T1.tag_add(self.tags[4], index, index + " lineend")
				elif (num == 0):
					self.T1.tag_add(self.tags[3], index, "%s+%sc" % (index, mycount.get()))

				self.T1.mark_set("start", "%s+%sc" % (index, mycount.get()))

	def indent(self, widget):  # Funcion que identa las linea para indicar en cual se encuentra

		index1 = widget.index("insert")
		index2 = "%s-%sc" % (index1, 1)
		prevIndex = widget.get(index2, index1)

		prevIndentLine = widget.index(index1 + "linestart")
		print("prevIndentLine ", prevIndentLine)
		prevIndent = self.getIndex(prevIndentLine)
		print("prevIndent ", prevIndent)

		if prevIndex == ":":
			widget.insert("insert", "\n" + "     ")
			widget.mark_set("insert", "insert + 1 line + 5char")

			while widget.compare(prevIndent, ">", prevIndentLine):
				widget.insert("insert", "     ")
				widget.mark_set("insert", "insert + 5 chars")
				prevIndentLine += "+5c"
			return "break"

		elif prevIndent != prevIndentLine:
			widget.insert("insert", "\n")
			widget.mark_set("insert", "insert + 1 line")

			while widget.compare(prevIndent, ">", prevIndentLine):
				widget.insert("insert", "     ")
				widget.mark_set("insert", "insert + 5 chars")
				prevIndentLine += "+5c"
			return "break"

	def getIndex(self, index):
		while True:
			if self.T1.get(index) == " ":
				index = "%s+%sc" % (index, 1)
			else:
				return self.T1.index(index)

	def update(self):
		self.stackify()
		self.tagHighlight()
		self.scan()

	def ExecDisplay(self):
		self.display()
		File = open("Rutina.py", "w")
		File.write(self.Compiler.code)
		File.close()
		# from src.IDE.Rutina import main as Objective
		exec(self.Compiler.code, {'IDE': self})

	def display(self):
		self.printwindow.delete("1.0", tk.END)
		self.printwindow.insert("1.0", "Compilando...")
		self.Compiler.Parse(self.T1.get("1.0", "end"))
		self.printwindow.insert("2.0", "\n")
		text = ''
		if type(self.Compiler.status) == tuple:
			for i in self.Compiler.status:
				text += i
		else:
			text = self.Compiler.status
		self.printwindow.insert("3.0", text)
		# self.printwindow.insert("6.0", self.T1.get("1.0", "end"))
		self.printwindow.insert("7.0", "\n")
		print(self.T1.get("1.0", "end"))
		self.Compiler.lexer.lineno = 0

	def clear(self):
		self.T1.delete("1.0", "end")
		self.LineN.clear()

	def stackify(self):
		self.stack.append(self.T1.get("1.0", "end - 1c"))
		if self.stackcursor < 9: self.stackcursor += 1

	def undo(self):
		if self.stackcursor != 0:
			self.clear()
			if self.stackcursor > 0: self.stackcursor -= 1
			self.T1.insert("0.0", self.stack[self.stackcursor])

	def redo(self):
		if len(self.stack) > self.stackcursor + 1:
			self.clear()
			if self.stackcursor < 9: self.stackcursor += 1
			self.T1.insert("0.0", self.stack[self.stackcursor])

	def FileNameS(self):
		NameS = asksaveasfilename()
		if NameS != "":
			print(NameS)
			self.SaveCode(NameS)
		else:
			showerror("Error",
			          "No se ha escrito el nombre del archivo")

	def FileNameL(self):
		NameL = askopenfilename()
		if NameL != "":
			print(NameL)
			self.LoadCode(NameL)
		else:
			showerror("Error",
			          "No se ha escrito el nombre del archivo")

	def ObtenerNameS(self):
		fileName = self.NameFileS.get()
		path = fileName + ".txt"
		if fileName != "":
			print(path)
			self.SaveCode(path)
			self.winS.destroy()
		else:
			showerror("Error",
			          "No se ha escrito el nombre del archivo")

	def ObtenerNameL(self):
		fileName = self.NameFileS.get()
		path = fileName + ".txt"
		if fileName != "":
			print(path)
			self.LoadCode(path)
			self.winL.destroy()
		else:
			showerror("Error",
			          "No se ha escrito el nombre del archivo")

	def LoadCode(self, FName):
		path = FName
		print(path)
		file = open(path)  # abrir
		content = file.readlines()  # lectura de las lineas
		lines = ''

		for i in content:
			lines += i

		print(lines)
		self.T1.insert("0.0", lines)
		file.close()  # cerrar
		return content

	def SaveCode(self, FName):
		path = FName
		print(path)
		# with open(path,'r+') as f:
		# f.truncate(0)
		file = open(path, "a")  # a->append
		file.write(self.T1.get("1.0", "end - 1c") + "\n")  # escribe el dato en el file
		file.close()

	def print_stack(self):
		i = 0
		for stack in self.stack:
			print(str(i) + " " + stack)
			i += 1

	def autoScroll(self, *args):
		print(args)
		if float(args[0]) == 0.0:
			if float(self.T1.yview()[1]) > 0.15:
				return
		self.T1.yview('moveto', float(args[0]))
		self.LineN.yview('moveto', float(args[0]))

	def print(self, *arg):
		text = ''
		for i in arg:
			text += str(i)
		line = self.printwindow.count("1.0", END, "lines")[0]
		print(line)
		self.printwindow.insert(str(line) + ".0", text)


def load_image(name):
	rute = os.path.join(name)
	image = PhotoImage(file=rute)
	return image


root = Tk()
root.title("Tambarduine")
root.geometry("880x650")
root.resizable(False, False)
bgroot = load_image("BgRoot.png")

P_canvas0 = Canvas(root, width=880, height=650, bg="black")
P_canvas0.place(x=0, y=0)
global ImgCanvas
ImgCanvas = P_canvas0.create_image(0, 0, anchor=NW, image=bgroot)
window = Window(root)

root.bind("<Key>", lambda event: window.update())
root.mainloop()
