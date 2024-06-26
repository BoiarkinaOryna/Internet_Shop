# Інтернет-магазин

## Список учасників команди
>- Бояркіна Орина(TEAMLEAD) - [дивитися на ГітХаб](https://github.com/BoiarkinaOryna)
>- Філинська Дар'я - [дивитися на ГітХаб](https://github.com/DariaFilinskaya)
>- Гомельська Вікторія -  [дивитися на ГітХаб](https://github.com/Viktoria0228)
>- Бурлакова Аліса - [дивитися на ГітХаб](https://github.com/archalice)
>- Пілат Віктор - [дивитися на ГітХаб](https://github.com/VictorPilat)

## Що робить наш проект

#### Наш проект - це інтернет-магазин з інтегрованим Телеграм-ботом, призначений для надання інформації про товари та управління користувачами, зокрема додавання і видалення покупців, а також надання прав адміністратора.


Наш проект створений для _легкого_ доступу до товарів із _зрозумілим_ інтерфейсом та можливістю купівлі обраних продуктів. Сайт, також, має адмін-панель, що набагато облегшує _редагування, додавання та видалення_ товарів.

Для нас цей проект має велике значення, як до програмістів-початківців, тим, що ми об'єднали різні технології для його реалізування. Такі як, _Flask, GitHub, SQLite3, pandas_, telebot, HTML, CSS, та Javascript.

### Для запуску проекту необхідно завантажити :

- **Flask** - створення структури сайту
- **pandas**- завантаження товарів з таблиці
- **Flask-Login** - додавання аутентифікації до сайту
- **Flask-Migrate** - прив'язування бази даних до до проекту
- **Flask-SQLALchemy** - працює з базою данних sql3
- **Flask-Mail** - відправка email
- **telebot** - створення тулеграм-боту
- **Jinja2** - шаблонізація веб-застосунку
- **requests** - робота з http запитами


#### Щоб запустити проект локально, необхідно відкрити проект у додатку VSCode або іншому редакторі для коду та запустити файл manage.py

#### Щоб запустити проект віддалено, використайте сервер [pythonanywhere](https://www.pythonanywhere.com) для Flask та Django проектів

## Проект містить такі застосунки:

- **Home** - домашня сторінка
- **Registration** - сторінка реєстрації
- **Authorization** - сторінка для входу в акаунт
- **Shop** - каталог товарів
- **Cart** - перелік обраних товарів
- **Contacts** - перелік контактів-продавців
- **Admin** - для редагування товарів

### Створення шаблону проекту

Необхідно створити елемент класу Flask бібліотеки flask і задати йому необхідні параметри: 
import_name - назва файлу, у якому створено змінну, template-folder - шлях до папки templates та instance-path - абсолютний шлях до папки, у якій знаходиться даний файл.

### Створення веб-сторінок
Створення веб-сторінок відбувається, за допомогою класу **Blueprint**, в якому задаються параметри:
name - відповідає за назву blueprint.
import_name -  відповідає за назву теки, у якій створюється певна структура.
template_folder - відповідає за теку templates, яка містить в собі html файл.
static_folder - відповідає за теку static, яка містить в собі файли css, js розширень, картинок та ін.
static_url_path - відповідає за налаштування URL шляху до статичних файлів у додатку.
![Картинка не знайдена](path)


### Під'єднання Blueprint до Flask

До змінної-екземпляру класу Blueprint застосовуємо функцію  add_url_rule і задаемо параметри: --rule - доменний шлях до сторінки, view_func - функція показу сторінки, що включає render_template та methods - види запитів сторінки (Get, Post).

image

До змінної-екземпляру класу Flask застосовуємо функцію register_blueprint з параметром blueprint - екземпляр класу Blueprint.

image

### Застосування форм

image

У формі має бути параметр method зі значенням post. Всередину додаем теги input або textarea (для введення значень) та button (для надсилання форми). За бажанням додаємо текстові теги, щоб показати, яке саме значення має приймати input.








# Internet Shop

## List of team members

>- Boiarkina Oryna (TEAMLEAD) - [view on GitHub](https://github.com/BoiarkinaOryna) 
>- Fynska Daria - [view on GitHub](https://github.com/DariaFilinskaya)
>- Homelska Viktoria - [view on GitHub](https://github.com/Viktoria0228)
>- Burlakova Alisa - [view on GitHub](https://github.com/archalice)
>- Pilat Viktor - [view on GitHub](https://github.com/VictorPilat)


## What our project does
#### Our project is an online store with an integrated Telegram bot, designed to provide information about products and user management, including adding and removing buyers, as well as providing administrator rights.