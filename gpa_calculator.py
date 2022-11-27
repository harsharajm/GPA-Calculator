from tkinter import *

class MyFrame():
	def __init__(self,win,sem,subjects,credits):
		self.gpa = 5.00
		self.subjects = subjects
		self.credits = credits

		self.frame = LabelFrame(win,text = sem,font = 30)

		self.scales = []
		for i in range(len(self.subjects)):
			Label(self.frame,text = self.subjects[i],justify = "right").grid(row = i,column = 1)
			scale = Scale(self.frame,from_ = 0, to_ = 10, orient = 'horizontal',activebackground = "cyan",command = lambda x:self.getgpa())
			scale.grid(row = i, column = 2)
			scale.set(5)
			self.scales.append(scale)
		Label(self.frame,text = "SGPA :",font=40).grid(row = i+1,column=1,ipady =30)
		self.gpa_label = Label(self.frame,text = 5,font = 40)
		self.gpa_label.grid(row = i+1,column = 2)

	def getgpa(self):
		global l,l1,f1,f2,f3,f4
		self.gpa = float("{:.2f}".format(sum(self.scales[i].get()*self.credits[i] for i in range(len(self.credits)))/sum(self.credits)))
		self.gpa_label.configure(text = self.gpa,bg = 'white')
		
		#######
		cgpa = (f1.gpa+f2.gpa+f3.gpa+f4.gpa)/4
		#######		
		l.configure(text = "CGPA:  "+str("{:.2f}".format(cgpa)))

		#For labels at the bottom
		x = 0
		if cgpa < 6.5:
			x = "{:.2f}".format(((6.5*6)-(f1.gpa+f2.gpa+f3.gpa+f4.gpa))/2)
			if float(x)>10:
				l1.configure(text = '6.5 not possible bro')
			else:
				l1.configure(text = str(x)+" in 3rd year for SGPA 6.5") 
		if cgpa < 7.5:
			x = "{:.2f}".format(((7.5*6)-(f1.gpa+f2.gpa+f3.gpa+f4.gpa))/2)
			if float(x)> 10:
				l2.configure(text = '7.5 not possible bro')
			else:
				l2.configure(text = str(x)+" in 3rdyear for SGPA 7.5")

win = Tk()
win.title("GPA Calculator")

l = Label(win,font = 100,bg = "White")
l.grid(row = 0 ,column = 5)
l1 = Label(win)
l1.grid(row = 2 ,column = 1)
l2 = Label(win)
l2.grid(row = 2 ,column = 3)

######Change the subjects and credits here if needed.#########
######Enter credits in the same order as the subjects.########
f1 = MyFrame(win,"SEM 1",["M1","Chem","BEE","EWS","ENG","EC LAB","ENG LAB","BEE LAB"],(4,4,3,2.5,2,1.5,1,1))
f1.frame.grid(row = 0,column = 1,ipadx = 10,ipady = 22)
f2 = MyFrame(win,"SEM 2",["M2","AP","PPS","EG","AP LAB","PPS LAB"],[4,4,4,3,1.5,1.5])
f2.frame.grid(row = 0,column = 2,ipadx =10,ipady = 63)
f3 = MyFrame(win,"SEM 3",["ADE","DS","MSF","COA","PP","ADE LAB","DS LAB","ITW LAB","PP LAB"],[3,4,4,3,2,1.5,1.5,1.5,1.5])
f3.frame.grid(row = 0,column = 3,ipadx =10,ipady = 0)
f4 = MyFrame(win,"SEM 4",["DM","BEFA","OS","CN","JAVA","OS LAB","CN LAB","JAVA LAB"],[3,3,3,4,4,1.5,1.5,1])
f4.frame.grid(row = 0,column = 4,ipadx =10,ipady = 21)

win.mainloop()