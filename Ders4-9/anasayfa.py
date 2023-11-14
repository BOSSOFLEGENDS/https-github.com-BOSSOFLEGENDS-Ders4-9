import tkinter as tk
from PIL import Image, ImageTk
import client
import filmler
# # Ana pencere oluşturma
# root = tk.Tk()
# root.title("Online Kurs Yönetim Sistemi")

def make_widgets(root):
    root.title("Anasayfa")
    # Resimleri yükle
    my_Basket_image = Image.open("images/Basketim.jpg").resize((200 ,200))
    my_Basket_photo = ImageTk.PhotoImage(my_Basket_image)

    other_filmler_image = Image.open("images/filmler.jpg").resize((200, 200))
    other_filmler_photo = ImageTk.PhotoImage(other_filmler_image)

    profile_image = Image.open("images/profile.jpg").resize((200, 200))
    profile_photo = ImageTk.PhotoImage(profile_image)

    statistics_image = Image.open("images/istatistik.jpg").resize((200, 200))
    statistics_photo = ImageTk.PhotoImage(statistics_image)

    snaks_image = Image.open("images/aperatifler.jpg").resize((200, 200))
    snaks_photo = ImageTk.PhotoImage(snaks_image)

    chat_image = Image.open("images/chat.png").resize((150, 150))
    chat_photo = ImageTk.PhotoImage(chat_image)

    # Başlık etiketi
    title_label = tk.Label(root, text="Online Sinema Sistemi", font=("Arial", 24))
    title_label.grid(row=0, column=0, columnspan=4, pady=20)

    # Butonlar
    my_Basket_button = tk.Button(root, image=my_Basket_photo, command=button_click)
    my_Basket_button.grid(row=1, column=0, padx=10, pady=10)
    my_Basket_button.image = my_Basket_photo # bu kodu yazmamız zorunlu

    my_Basket_label = tk.Label(root, text="Basketim", font=("Arial", 20))
    my_Basket_label.grid(row=2, column=0, padx=10, pady=10)
    

    other_filmler_button = tk.Button(root, image=other_filmler_photo, command=button_click)
    other_filmler_button.grid(row=1, column=1, padx=10, pady=10)
    other_filmler_button.image = other_filmler_photo

    other_filmler_label = tk.Label(root, text="filmler", font=("Arial", 20))
    other_filmler_label.grid(row=2, column=1, padx=10, pady=10)


    profile_button = tk.Button(root, image=profile_photo, command=button_click)
    profile_button.grid(row=1, column=5, padx=10, pady=10)
    profile_button.image = profile_photo

    profile_label = tk.Label(root, text="Profilim", font=("Arial", 20))
    profile_label.grid(row=2, column=5, padx=10, pady=10)


    istatistik_button = tk.Button(root, image=statistics_photo, command= lambda : show_stats(root))
    istatistik_button.grid(row=1, column=3, padx=10, pady=10)
    istatistik_button.image = statistics_photo

    istatistik_label = tk.Label(root, text="İstatistikler", font=("Arial", 20))
    istatistik_label.grid(row=2, column=3, padx=10, pady=10)

    my_snaks_button = tk.Button(root, image=snaks_photo, command=button_click)
    my_snaks_button.grid(row=3, column=0, padx=10, pady=10)
    my_snaks_button.image = snaks_photo # bu kodu yazmamız zorunlu

    my_snaks_label = tk.Label(root, text="aperatifler", font=("Arial", 20))
    my_snaks_label.grid(row=4, column=0, padx=10, pady=10)

    chat_button = tk.Button(root, image=chat_photo, command=live_chat_click)
    chat_button.grid(row=3, column=3, padx=10, pady=10)
    chat_button.image = chat_photo


def live_chat_click():
    print("Live Chat button clicked")
    client.get_chat_window()

def filmler_click():
    print("Filmler button clicked")
    filmler.create_course_buttons()


# Fonksiyon: Butona tıklandığında yapılacak işlem
def button_click():
    print("buton click edildi")

def show_stats(root):
    # ders 10 da eklendi
    from stats import UserStatsApp
    stats_window = tk.Toplevel(root)  # Create a Toplevel window for stats.py
    app = UserStatsApp(stats_window)
    root.deiconify() 


    


# make_widgets(root)

# Pencereyi çalıştır
# root.mainloop()
