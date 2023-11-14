import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd

# Veri setini yükle
data = pd.read_csv('AnnualTicketSales.csv')

# tkinter penceresini oluştur
root = tk.Tk()
root.geometry("1000x700")
root.title("Film İnceleme Uygulaması")

# Ana pencereyi sarmalayacak bir çerçeve oluştur
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Kurs butonlarını içerecek bir çerçeve oluşturun
button_frame = tk.Frame(main_frame, width=220)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Kurs bilgilerini gösterecek bir LabelFrame oluşturun
info_frame = tk.LabelFrame(main_frame, text="Kurs Bilgileri", width=400, height=400)
info_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

course_items = ["YEAR","TICKETS SOLD","TOTAL BOX OFFICE","TOTAL INFLATION ADJUSTED BOX OFFICE","AVERAGE TICKET PRICE"]

course_buttons = {}


def create_course_buttons(keyword):
    for widget in button_frame.winfo_children():
        widget.destroy()  # Önceki kurs butonlarını temizle

    for index, row in data.iterrows():
        course_name = row['YEAR']

        if keyword in str(course_name):
            btn_single_course = tk.Label(button_frame, width=70, height = 7, bd=3, relief="raised")
            btn_single_course.pack(fill = tk.BOTH, padx=5, pady=5)

            try:
            # Resim dosyasının yolu, kurs adına bağlı olarak ayarlanmalıdır.
                image_path = f'images/download.jpg' # Bu örnekte "images" klasöründen resimleri alıyoruz.
                img = Image.open(image_path)

            except:  # if there is error use default image
                image_path = "images/download.jpg"
                img = Image.open(image_path)
            
            # Resmi aç ve istediğiniz boyuta yeniden boyutlandır
            
            img = img.resize((100, 100), Image.Resampling.LANCZOS)  # Özel boyutlandırmayı burada ayarlayabilirsiniz
            img = ImageTk.PhotoImage(img)

            # Resim etiketi oluşturun ve ekrana yerleştirin
            image_label = tk.Label(btn_single_course, image=img)
            image_label.image = img
            image_label.pack(side=tk.LEFT, padx=5, pady=5)

            # Kurs adı ve derecelendirmeyi içeren etiketi oluşturun ve ekrana yerleştirin
            course_info_label = tk.Label(btn_single_course, text=f"{course_name}\nRating: {row['YEAR']}", justify=tk.LEFT)
            course_info_label.pack(side=tk.LEFT, padx=5, pady=5)

            # Kurs butonunu oluşturun
            command = lambda name=course_name: show_course_details(name)
            button = tk.Button(btn_single_course, text="Daha Fazla Bilgi", width=15, command=command, justify=tk.RIGHT)
            button.pack(side=tk.RIGHT, padx=5, pady=5)

            # Kurs butonunu sözlüğe ekleyin
            course_buttons[course_name] = btn_single_course
            

            

def show_course_details(course_name):
    # seçilen kurs
    selected_course = data[data['YEAR'] == course_name].iloc[0]

    # Kurs ayrıntılarını görüntülemek için istediğiniz işlemi yapabilirsiniz.
    for widget in info_frame.winfo_children():
        if widget not in [search_button, search_entry]:
            widget.destroy()  # Önceki kurs bilgilerini temizle
    
    for column in course_items:
        label = tk.Label(info_frame, text=f"{column}: {selected_course[column]}", wraplength=300)
        label.pack(fill=tk.BOTH, expand=True)


def search_courses(event=None):
    keyword = search_entry.get()
    
    for key in course_buttons:
        course_buttons[key].destroy()

    course_buttons.clear()
    
    create_course_buttons(keyword)

# Kurs arama için giriş alanı
search_entry = tk.Entry(info_frame)
search_entry.pack()

# Arama düğmesi
search_button = tk.Button(info_frame, text="Filmleri Ara", command=search_courses)
search_button.pack()

# Enter tuşuna basıldığında arama yapmak için olay dinleyiciyi (event listener) ekleyin
search_entry.bind("<Return>", search_courses)

# Uygulamayı çalıştırın ve başlangıçta tüm kursları gösterin
create_course_buttons("")



# Example of triggering the chat window
if __name__ == "__main__":
    root = tk.Tk()
    chat_button = tk.Button(root, text="Open filmler", command=create_course_buttons)
    chat_button.pack()
    root.mainloop()
