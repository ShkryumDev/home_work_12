# Создаем функцию для сохранения картинок при загрузке постов в папку uploads
def save_picture(picture) -> str:
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path
