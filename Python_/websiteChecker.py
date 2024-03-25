import urllib.request
import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlparse
from datetime import datetime

HISTORY_FILE = "website_history.txt"

def check(event=None):
    try:
        web = url.get()
        if not web.startswith(('http://', 'https://')):
            web = 'http://' + web
        req = urllib.request.Request(
            web, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        website_is_up = status_code == 200
        if website_is_up:
            messagebox.showinfo("Website Status", "Website is up and running")
        else:
            messagebox.showwarning("Website Status", "Website is down")
        
        # Save to history file
        with open(HISTORY_FILE, "a") as file:
            file.write(f"{datetime.now()} - {web} - {'Up' if website_is_up else 'Down'}\n")
    except urllib.error.URLError as e:
        messagebox.showerror("Error", f"Error: {e.reason}")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

window = tk.Tk()
window.geometry("600x600")
window.title("Website Connectivity Checker")

head_label = tk.Label(
    window, text="Website Connectivity Checker", font=("Calibri", 20))
head_label.pack(pady=10)

url = tk.StringVar()
url_entry = tk.Entry(window, textvariable=url, width=40, font=("Calibri", 14))
url_entry.pack(pady=5)
url_entry.focus_set()

check_button = tk.Button(window, text="Check", command=check, font=("Calibri", 14))
check_button.pack(pady=5)

# Setting anchor to center the labels
head_label.configure(anchor='center')
url_entry.configure(justify='center')
check_button.configure(anchor='center')

window.bind("<Return>", check)

window.mainloop()
