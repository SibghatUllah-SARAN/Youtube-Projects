import tkinter as tk
win=tk.Tk()

win.title("CodeNovaX GUI")

win.config(bg="#050E3C")

heading=tk.Label(text=" CodeNovaX ",bg="#050E3C",fg="#FFE100",font=("Arial",30,"bold"))
heading.pack(padx=15,pady=15)

hello=tk.Label(text="\t\t\n Hello Friends this my Own made GUI ",bg="#002455",fg="white",font=("Arial",24))
hello.pack(padx=20,pady=20)

Name_Enter=tk.Label(text=" Enter your Name : ",bg="#002455",fg="white",font=("Arial",18))
Name_Enter.pack(padx=10,pady=10)


name=tk.Entry(bg="#002455",fg="white",font=("Arial",18))
name.pack(padx=10,pady=10)

button2=tk.Button(text=" Subscribe ",bg="#0044CC",fg="white",font=("Arial",18),command=lambda:wellcome.config(text=" Well Come to my subscriber : "+name.get()))
button2.pack(padx=10,pady=10)

wellcome=tk.Label(text="",bg="#002455",fg="white",font=("Arial",23))
wellcome.pack(padx=10,pady=10)


button=tk.Button(text="More",bg="#0044CC",fg="white",font=("Arial",18),command=lambda:more.config(text=" Subscribed for more "))

button.pack(padx=10,pady=10)   
more=tk.Label(text="",bg="#002455",fg="white",font=("Arial",23))
more.pack(padx=10,pady=10) 

button1=tk.Button(text=" Total Subscribers ",bg="#0044CC",fg="white",font=("Arial",18),command=lambda:show_subscribers.config(text=" My total subscribers are only 25 "))

button1.pack(padx=10,pady=10)
show_subscribers=tk.Label(text="",bg="#002455",fg="white",font=("Arial",23))
show_subscribers.pack(padx=10,pady=10)

win.mainloop()