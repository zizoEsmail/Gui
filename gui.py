import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            tts = gTTS(text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "open output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def clear_text():
    text_entry.delete("1.0", tk.END)

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("400x300")

# Create a text entry widget
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text_entry.pack(pady=10)

# Create buttons
play_button = tk.Button(root, text="Play", command=play_text)
play_button.pack(pady=5)

set_button = tk.Button(root, text="Set", command=clear_text)
set_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)

# Run the application
root.mainloop()