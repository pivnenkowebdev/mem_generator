from PIL import Image, ImageDraw, ImageFont

# Список картинок
images = [
    "cat-aaaa.png",
    "cat-smile.png",
]

# Выбор картинки
print("Выберите картинку:")
for i, img_name in enumerate(images, 1):
    print(f"{i}. {img_name}")

choice = int(input("Введите номер картинки: "))
img_path = f"./img/{images[choice - 1]}"

# Открываем картинку
img = Image.open(img_path)
draw = ImageDraw.Draw(img)

# Ввод текста
top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")

# Настройка шрифта
# Можно использовать любой ttf файл, например impact.ttf
try:
    font = ImageFont.truetype("impact.ttf", size=int(img.height/10))
except:
    # Если impact не найден, используем стандартный
    font = ImageFont.load_default()

# Функция для рисования текста по центру
def draw_text_centered(draw, text, font, img_width, y):
    # Получаем размеры текста
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=2)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (img_width - text_width) / 2
    draw.text((x, y), text, font=font, fill="white", stroke_width=2, stroke_fill="black")


# Верхний текст
draw_text_centered(draw, top_text, font, img.width, y=10)

# Нижний текст
draw_text_centered(draw, bottom_text, font, img.width, y=img.height - int(img.height/10) - 10)

# Сохраняем результат
output_path = "meme_result.png"
img.save(output_path)
print(f"Мем сохранён как {output_path}")

# Показываем результат
img.show()
