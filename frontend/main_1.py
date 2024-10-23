import tkinter as tk

def place_login_component():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    Login_label = tk.Label(root, text="Log In", font=("Helvetica", 50))
    Login_label.place(x = 700, y = 100)
    # w.pack()
    root.mainloop()

place_login_component()