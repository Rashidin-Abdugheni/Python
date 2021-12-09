import tkinter as tk

root = tk.Tk()
root.title("🦅 R.A.U Genome Coverage Calculator")

canvas1 = tk.Canvas(root, width=600, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Genome Coverage Calculator')
label1.config(font=('helvetica', 14, 'bold'))
canvas1.create_window(300, 25, window=label1)

label2 = tk.Label(root, text='Formula is : (C/R)*(R/G)')
label2.config(font=('helvetica', 12, 'bold'))
canvas1.create_window(300, 45, window=label2)

label2 = tk.Label(root, text='Type your parameters：')
label2.config(font=('helvetica', 10, 'bold'))
canvas1.create_window(300, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(300, 120, window=entry1)
label3 = tk.Label(root, text='Raw Bases (bp)')
label3.config(font=('helvetica', 10, 'bold'))
canvas1.create_window(100, 120, window=label3)

entry2 = tk.Entry(root)
canvas1.create_window(300, 150, window=entry2)
label4 = tk.Label(root, text='Clean Bases (bp)')
label4.config(font=('helvetica', 10, 'bold'))
canvas1.create_window(100, 150, window=label4)

entry3 = tk.Entry(root)
canvas1.create_window(300, 180, window=entry3)
label5 = tk.Label(root, text='Genome size (bp) ')
label5.config(font=('helvetica', 10, 'bold'))
canvas1.create_window(100, 180, window=label5)

def Genome_Coverage():
    s11 = int(entry1.get())
    s22 = int(entry2.get())
    s33 = float(entry3.get())
    value = "{:.2f}".format((s22/s11)*(s11/s33))

    label3 = tk.Label(root, text='The Genome Coverage is:', font=('helvetica', 14, 'bold'))
    canvas1.create_window(300, 250, window=label3)

    label4 = tk.Label(root, text=value, font=('helvetica', 10, 'bold'))
    canvas1.create_window(300, 270, window=label4)


button1 = tk.Button(text='Click To Calculate', command=Genome_Coverage, bg='brown', fg='white',  font=('helvetica', 9, 'bold'))
canvas1.create_window(300, 250, window=button1)

root.mainloop()

