import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter import filedialog as fd
from tkinter import simpledialog
from PIL import Image, ImageTk 
from .imageHandler import ImageHandler


class Imagine(tk.Frame,ImageHandler):
    def __init__(self, master=None):
        super().__init__(master)
        self.initUI()


    def initUI(self):
        self.pack()
        
        # Визуал кнопок для взаимодействия с обьектами  fill.x растягивание кнопки 
        ttk.Button(self, text='Файл', command=self.load_image_gui).pack(fill=tk.X)
        ttk.Button(self, text='Сохранить', command=self.save_to_file_gui).pack(fill=tk.X)
        ttk.Button(self, text='Поворот на 90', command=self.turn_gui).pack(fill=tk.X)
        ttk.Button(self, text='Черно-белое', command=self.apply_black_and_white_filter_load_gui).pack(fill=tk.X)
        ttk.Button(self, text='Обрезка', command=self.crop_image_gui).pack(fill=tk.X)
        ttk.Button(self, text='Добавить текст', command=self.add_text_gui).pack(fill=tk.X)


        # Лейбл для вывода изображения при изменении/загрузке
        self.label_photo = ttk.Label(self)
        self.label_photo.pack(pady=10)
    

    def load_image_gui(self):
        self.file_path = fd.askopenfilename(title="Выберите нужный вам формат", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*")])  # Окно переход в проводник для выбора нужного файла вручную
        try:
            self.load_image(self.file_path)
            self.update_label(self.img)  # Вывод на лейбл изображения
        except:
            showerror("Ошибка", "Файл не удалось открыть") # Вывод при ошибоке


    # Метод обновления лейбла
    def update_label(self, img):
        self.img_tk = ImageTk.PhotoImage(img)  # Метод ткинтера
        self.label_photo.config(image=self.img_tk)  # Обновление лейбла


    def save_to_file_gui(self):
        try:
            self.save_to_file(self.file_path)
        except:
             showerror("Ошибка", "Не удалось Сохранить изображение") # Вывод при ошибке


    def turn_gui(self):
        try:
            self.turn(self.img)
            self.update_label(self.img)  # Сохранение на лейбл
        except:
            showerror("Ошибка", "Не удалось изменить ориентацию изображения") # Вывод при ошибке


    # метод повышения резкости изображения
    def apply_black_and_white_filter_load_gui(self):
            try:
                self.apply_black_and_white_filter_load(self.img)
                self.update_label(self.img)  # Меняем лейбл
            except:
                showerror("Ошибка", "Не удалось  применить фильтр черно-белое") # Вывод при ошибке


    def crop_image_gui(self): 
        try:
            self.crop_image() 
            self.update_label(self.img)  # Меняем лейбл
        except:
            showerror("Ошибка", "Не удалось обрезать изображение") # Вывод при ошибке


    def add_text_gui(self):
        try:
            self.add_text_load() 
            self.update_label(self.img) # Меняем лейбл
        except:
            showerror("Ошибка", "Не удалось добавить текст") # Вывод при ошибке
