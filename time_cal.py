# to calculate 4-digits hour easily, with GUI
from datetime import datetime, timedelta
from tkinter import *


root = Tk()
root.geometry("300x200")
root.title('Time Calculator - By Klaus')

# function here
def cal_t_b(): 
	# calculate time duration here in hrs
	# modify here!!!
	box_text = enter_box.get()

	# analyze text obtained
	try: 
		st = box_text.split(' ')[0]
		et = box_text.split(' ')[1]
	except IndexError: 
		info_l.config(text='Add space between times! ', fg='red')

	try: 
		dtst = datetime.strptime(st, "%H%M")
		dtet = datetime.strptime(et, "%H%M")
	except ValueError: 
		info_l.config(text='Wrong Data Type! ', fg='red')

	t_diff = round(timedelta.total_seconds(dtet-dtst)/3600, 2)
	# print(t_diff)
	info_l.config(text=str(t_diff)+' hrs', fg='blue')

	return

def cal_t(event): 
	# inherit all from button function
	# NO NEED TO CHANGE HERE!
	cal_t_b()

# visual stuff here
title_text = Label(root, text='Enter the 2 time in box below: ', font=("Comic Sans MS", 16))
title_text.pack()

enter_box = Entry(root, width=20, font=("Comic Sans MS", 12))
enter_box.pack()

button = Button(root, text='Convert', command=cal_t_b, pady=10, 
	padx=20, font=("Comic Sans MS", 14, 'bold'))
button.pack()

info_l = Label(root, text='Result will be shown here! ', font=("Comic Sans MS", 12))
info_l.pack()

root.bind('<Return>', cal_t)

root.mainloop()

