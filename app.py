import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Canvas, ttk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from chat import get_response


class MyFirstGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("500x800")
        self.title("Covid-19 HelpBot")
        self.first_frame = tk.Frame(self, bg="sky blue")
        self.first_frame.pack(fill="both", expand=True)
        app_icon = Image.open('icon.ico')
        app_icon = ImageTk.PhotoImage(app_icon)
        self.iconphoto(False, app_icon)
    
        container = tk.Frame(self)
        container.place(x=40, y=120, width=450, height=550)
        self.canvas = tk.Canvas(container, bg="#595656")
        self.scrollable_frame = tk.Frame(self.canvas, bg="#595656")

        scrollable_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        def configure_scroll_region(e):
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))

        def resize_frame(e):
            self.canvas.itemconfig(scrollable_window, width=e.width)

        self.scrollable_frame.bind("<Configure>", configure_scroll_region)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.yview_moveto(1.0)
        
        scrollbar.pack(side="right", fill="y")
        self.canvas.bind("<Configure>", resize_frame)
        self.canvas.pack(fill="both", expand=True)
        #Welcom message
        self.m_frame = tk.Frame(self.scrollable_frame, bg="#595656")

        self.m_frame.columnconfigure(1, weight=1)

        self.t_label = tk.Label(self.m_frame, bg="#595656",fg="white", text=datetime.now().strftime('%H:%M'), font="lucida 7 bold",
                           justify="left", anchor="w")
        self.t_label.grid(row=0, column=1, padx=2, sticky="w")

        self.m_label = tk.Label(self.m_frame, wraplength=250,fg="black", bg="#c5c7c9", text="Welcom to CoronaHelpBot", font="lucida 9 bold", justify="left",
                           anchor="w")
        self.m_label.grid(row=1, column=1, padx=2, pady=2, sticky="w")

        self.m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")

        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)
        #entry 
        self.entry = tk.Text(self, font="lucida 10 bold", width=38, height=2,highlightcolor="blue", highlightthickness=1)
        self.entry.place(x=40, y=681)
        self.entry.focus_set()
        send_button = tk.Button(self, text="Send", fg="#83eaf7", font="lucida 11 bold", bg="#7d7d7d", padx=10,relief="solid",command=self.sent_message_format)
        send_button.place(x=400, y=680)
        self.mainloop()

    def sent_message_format(self, event=None):

        message = self.entry.get('1.0', 'end-1c')

        if message:
            if event:
                message = message.strip()
            self.entry.delete("1.0", "end-1c")
            m_frame = tk.Frame(self.scrollable_frame, bg="#595656")

            m_frame.columnconfigure(0, weight=1)

            t_label = tk.Label(m_frame, bg="#595656", fg="white", text=datetime.now().strftime('%H:%M'),font="lucida 7 bold", justify="right", anchor="e")
            t_label.grid(row=0, column=0, padx=2, sticky="e")

            m_label = tk.Label(m_frame, wraplength=250, text=message, fg="black", bg="#40C961",font="lucida 9 bold", justify="left",anchor="e")
            m_label.grid(row=1, column=0, padx=2, pady=2, sticky="e")

            i_label = tk.Label(m_frame, bg="#595656")
            i_label.grid(row=0, column=1, rowspan=2, sticky="e")

            m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")
            self.received_message_format(get_response(message))
            self.canvas.update_idletasks()
            self.canvas.yview_moveto(1.0)
            
            
                
            
            
    def received_message_format(self, data):

        message = data
        m_frame = tk.Frame(self.scrollable_frame, bg="#595656")

        m_frame.columnconfigure(1, weight=1)

        t_label = tk.Label(m_frame, bg="#595656",fg="white", text=datetime.now().strftime('%H:%M'), font="lucida 7 bold",
                           justify="left", anchor="w")
        t_label.grid(row=0, column=1, padx=2, sticky="w")

        m_label = tk.Label(m_frame, wraplength=250,fg="black", bg="#c5c7c9", text=message, font="lucida 9 bold", justify="left",
                           anchor="w")
        m_label.grid(row=1, column=1, padx=2, pady=2, sticky="w")

        m_frame.pack(pady=10, padx=10, fill="x", expand=True, anchor="e")

        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)


MyFirstGUI()