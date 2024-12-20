from PIL import Image
from .imageProcessor import ImageProcessor  


class ImageHandler():
    def __init__(self):
        self.img = None  
        self.file_path = None  


    def load_image(self,file_path):
        self.img = Image.open(self.file_path)
        

    # Метод сохранения в файл
    def save_to_file(self,file_path):
        self.img.save(self.file_path)  # Обновление старого файла на новый


    # Метод поворота на 90 градусов
    def turn(self,img):
        self.img  = self.img.rotate(90) # Поворот и присвоение обьекту


    def apply_black_and_white_filter_load(self,img):
        filter = ImageProcessor(self.img)  # Экземпляр дочернего класса
        self.img = filter.apply_black_and_white_filter()  # Изменения цвета на ЧБ


    def crop_image(self, width=150, height=150):
        original_width, original_height = self.img.size
        left = (original_width - width) / 2
        top = (original_height - height) / 2
        right = (original_width + width) / 2
        bottom = (original_height + height) / 2
        self.img = self.img.crop((left, top, right, bottom)) # Применяем метод
        return self.img


    def add_text_load(self):
        filter = ImageProcessor(self.img) # Экземпляр дочернего класса
        self.img = filter.add_text("Вариант 2", (10, 10), color="black") # Добавления текста в левый угол
        return self.img