import requests
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

print('библиотека Python: requests')


class Requests:
    url = 'https://www.tbank.ru'  # Указываем URL, на который будем отправлять GET-запрос
    response = requests.get(url)  # Отправляем GET-запрос по указанному URL
    if response.status_code == 200:  # Проверяем статус-код ответа
        data = response.url  # Если статус-код 200 (OK), получаем данные из ответа
        print(f'Статус ответа: OK [код 200]')
    else:
        print('Ошибка при выполнении запроса')  # При ошибке будет данное сообщение


print('библиотека Python: nympy')


class Numpy:
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # Создаем массив
    sum = np.sum(arr)  # Суммируем его элементы
    flip = np.flip(arr)  # Элементы массива в обратном порядке

    print(arr)
    print(sum)
    print(flip)


print('библиотека Python: matplotlib')


class Matplotlib:
    # Задаем данные по осям
    month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август']
    visitors = [1000, 980, 1200, 870, 950, 1050, 990, 1025]

    # Построение диаграммы и линейного графика
    plt.plot(month, visitors)

    plt.bar(month, visitors, label='Людей в месяц')
    plt.plot(month, visitors, color='red', marker='o', markersize=7)
    plt.xlabel('Месяц')
    plt.ylabel('Посетители')
    plt.title('Комбинация графиков')
    plt.legend()
    plt.show()


print('библиотека Python: pillow')


class Pillow:
    image = Image.open(r'C:\Users\ALEX\Desktop\Алекс1\игрушки\палатка1.jpg')
    image.show()
    resized_image = image.resize((400, 400))  # изменение размера на 400 x 400 пикселей
    resized_image.save('resized_image.png')

    # image = Image.open(r'C:\Users\ALEX\Desktop\Алекс1\игрушки\палатка1.jpg')
    blurred_image = image.filter(ImageFilter.BLUR)  # применить эффекты
    blurred_image.save('blurred_image.png')

    # сохранить в другой формат
    # image = Image.open(r'C:\Users\ALEX\Desktop\Алекс1\игрушки\палатка1.jpg')
    image.save('converted_image.jpg')  # конвертация в формат JPEG
    image.save('converted_image.gif')  # конвертация в формат GIF
