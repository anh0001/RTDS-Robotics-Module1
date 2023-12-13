#import maksudnya disini adalah kendali gui dari masing masing robot 

import serial
import tkinter as tk
from tkinter import ttk

# Inisialisasi koneksi serial dengan Arduino
ser = serial.Serial('COM10', 115200)  

# Fungsi untuk mengirim perintah ke Arduino
def send_command(command):
    ser.write(command.encode())

# Membuat fungsi untuk menyalakan LED
def Gerakan_1():
    send_command('A')

def Gerakan_2():
    send_command('B')

def Gerakan_3():
    send_command('C')

def Gerakan_4():
    send_command('D')

def Reset():
    send_command('R')


# Membuat GUI
root = tk.Tk()
root.configure(bg="blanchedalmond")
root.geometry("250x200")
root.resizable(False,False)
root.title("Gambar RTDS")

# Function to display new window
def show_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    # Text content about the purpose of the GUI
    label_text = """
    The purpose of this GUI is to control the RTDS arm, allowing users to generate specific images based on their choices.

    *Kinematics of RTDS by Bagas Dwi Atmaja Achmad Fauzan*
    This GUI is designed to interact with the Kinematics of the RTDS system, which is developed by Bagas Fauzan Dwi Atmaja. 
    The Kinematics component is responsible for defining the motion and positioning of the RTDS arm.

    *GUI Design by Thufail Bariqlana Audra*
    The graphical user interface (GUI) is crafted by Thufail Bariqlana Audra. It serves as the user-friendly interaction platform that enables users
    to input their preferences and commands to the RTDS system. The design focuses on providing an intuitive and efficient way for users to control 
    the RTDS arm for generating specific images.
    
    
    """

    # Displaying the text
    label = ttk.Label(new_window, text=label_text, justify="left")
    label.pack(padx=20, pady=10)

    # Close button
    close_button = ttk.Button(new_window, text="Quit", command=new_window.destroy)
    close_button.pack(pady=10)

# Frame input
input_frame = ttk.Frame(root)
# Penempatan Grid, Pack, Place
input_frame.pack(padx=0, pady=0, expand=True)

SERVO_1 = tk.StringVar()
SERVO_2 = tk.StringVar()

# Buttons for controlling the arm
input_button = ttk.Button(input_frame, text="-", command=Gerakan_1)
input_button.pack(padx=10, pady=0, fill="x", expand=True)

input_button = ttk.Button(input_frame, text="➕", command=Gerakan_2)
input_button.pack(padx=10, pady=0, fill="x", expand=True)

input_button = ttk.Button(input_frame, text="▭", command=Gerakan_3)
input_button.pack(padx=10, pady=0, fill="x", expand=True)

input_button = ttk.Button(input_frame, text="◡", command=Gerakan_4)
input_button.pack(padx=10, pady=0, fill="x", expand=True)

input_button = ttk.Button(input_frame, text="Reset.",command=Reset)
input_button.pack(padx=10, pady=0, fill="x", expand=True)

# Button to show information about the GUI
input_button = ttk.Button(input_frame, text="About", command=show_new_window)
input_button.pack(padx=20, pady=5, fill="x", expand=True)

# Button for close the GUI
input_button = ttk.Button(input_frame, text="Quit", command=root.quit)
input_button.pack(padx=20, pady=5, fill="x", expand=True)

root.mainloop()

# Tutup koneksi saat selesai
ser.close()