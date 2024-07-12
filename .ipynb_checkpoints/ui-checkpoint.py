import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import cv2
import numpy as np


class SimpleHTR_UI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("SimpleHTR UI")
        self.create_widgets()

    def create_widgets(self):
        # Create label for image file path
        self.label_file = tk.Label(self.master, text="Select an image file:")
        self.label_file.grid(row=0, column=0, padx=10, pady=10)

        # Create button to select image file
        self.button_file = tk.Button(self.master, text="Browse", command=self.browse_file)
        self.button_file.grid(row=0, column=1, padx=10, pady=10)

        # Create button to run recognition
        self.button_run = tk.Button(self.master, text="Run Recognition", command=self.run_recognition)
        self.button_run.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        # Create label for recognized text
        self.label_recognized = tk.Label(self.master, text="Recognized text:")
        self.label_recognized.grid(row=2, column=0, padx=10, pady=10)

        # Create text box for recognized text
        self.text_recognized = tk.Text(self.master, height=5, width=50)
        self.text_recognized.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

    def browse_file(self):
        # Ask user to select image file
        filename = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])

        if filename:
            # Update label with selected file path
            self.label_file.config(text=f"Selected file: {filename}")

            # Store the file path
            self.filepath = filename

    def run_recognition(self):
        try:
            # Run main.py with selected file as argument
            cmd = f"python C:\\Users\\zambogo\\Desktop\JOB\zedProjects\\simpleHTR\SimpleHTR\src\main.py {self.filepath}"
            output = subprocess.check_output(["python", "C:/Users/zambogo/Desktop/JOB/zedProjects/simpleHTR/SimpleHTR/src/main.py", "--img_file", self.filepath])

            output = output.decode('utf-8')
            recognized, probability = output.strip().split('\n')
            # Update text box with recognized text
            self.text_recognized.delete(1.0, tk.END)
            self.text_recognized.insert(tk.END, f"Recognized: {recognized}\nProbability: {probability}")
        except Exception as e:
            messagebox.showerror("Error", f"Error running recognition: {str(e)}")

if __name__ == '__main__':
    # Create main window
    root = tk.Tk()

    # Create SimpleHTR_UI instance
    app = SimpleHTR_UI(root)

    # Run main loop
    app.mainloop()
