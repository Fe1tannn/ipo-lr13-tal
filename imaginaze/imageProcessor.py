from PIL import ImageFilter, ImageDraw, ImageOps


class ImageProcessor:
    def __init__(self, img):
        self.img = img  


    def apply_black_and_white_filter(self): 
        self.img = self.img.convert('L')  # Фильтр ЧБ
        return self.img  
 

    def add_text(self, text="Вариант 2", position=(10, 10), font=None, font_size=20, color="black"):
        draw = ImageDraw.Draw(self.img)
        draw.text(position, text, fill=color) # Добавление текста
        return self.img