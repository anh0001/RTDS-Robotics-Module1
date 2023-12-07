#import maksudnya disini adalah kendali gui dari masing masing robot 

import serial
import tkinter as tk

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
    send_command('c')


# Membuat GUI
root = tk.Tk()
root.configure(bg="blanchedalmond")
root.geometry("300x300")
root.resizable(False,False)
root.title("About")

# Function to display new window
def show_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    # Text content about the purpose of the GUI
    label_text = """
    The purpose of this GUI is to control the RTDS arm, allowing users to generate specific images based on their choices.

    *Kinematics of RTDS by Bagas Fauzan Dwi Atmaja*
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

on_button = tk.Button(root, text="–", command=Gerakan_1)
on_button.grid(row=0, column=0, padx=10,pady=10)

on_button = tk.Button(root, text="◡", command=Gerakan_2)
on_button.grid(row=1, column=0, padx=10,pady=10)

on_button = tk.Button(root, text="▭", command=Gerakan_3)
on_button.grid(row=2, column=0, padx=10,pady=10)

quit_button = tk.Button (root, text="Quit", command=root.quit)
quit_button.grid(row=4, column=2, padx=10,pady=10)

root.mainloop()

# Tutup koneksi saat selesai
ser.close()