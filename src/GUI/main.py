import serial
import time

# Inisialisasi komunikasi serial dengan Arduino (sesuaikan port dan baud rate)
arduino_port = '/dev/ttyUSB0'  # Ganti dengan port serial yang sesuai di komputer Anda
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

try:
    while True:
        # Kirim perintah ke Arduino
        command = input("Masukkan perintah (Contoh: M 300 100): ")
        
        # Tambahkan opsi untuk menghentikan program
        if command.lower() == 'exit':
            print("Program berhenti")
            break

        ser.write(command.encode('utf-8'))

        # Tunggu sebentar agar pesan terkirim
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program berhenti")
    ser.close()
except Exception as e:
    print("Terjadi kesalahan:", e)
finally:
    ser.close()
