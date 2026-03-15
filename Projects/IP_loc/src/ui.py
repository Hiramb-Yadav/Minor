#This prg is to prseent location wtih a nice GUI 
import customtkinter as ctk 

def present(lat, lng):
    win = ctk.CTk() #win for windows 
    win.geometry("300x100")
    win.title("User Location")

    text = ctk.CTkLabel(win, text=f"Latitude: {lat}\nLongitude:{lng}")
    text.pack(pady=20)

    win.mainloop()
