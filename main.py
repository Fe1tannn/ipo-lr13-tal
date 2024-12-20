from imaginaze.imageFunction import Imagine
from PIL import Image
import tkinter as tk


class Application(tk.Tk): # Класс наследует tkinter 
    def __init__(self):
        super().__init__()
        self.title('Работа с фото') # Титульник дял программы
        first_label = tk.Label(self, text="Работа с фото", font=10) # Лейбл для программы
        first_label.pack(pady=2, padx=2) # Размещение лейбла в окне
        self.image_handler = Imagine(master=self) # Создание обьекта класса
        self.image_handler.pack(pady=5, padx=5) # Размещение окна обьекта в главном окне программы

        

app = Application() # Создание обькта класса
app.mainloop() # Вывод главного окна