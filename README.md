# ToDo Application

## Описание
TODO: несколько слов о проекте 

## Как поддерживать проект и присоединиться к разработке?
Перед каждым коммитом проверяем, что в репозитории нет изменений командой git pull. Если получаем ошибку, пользуемся инструкцией ниже: таким образом избегаем конфликтов версий и не плодим коммиты.
- git stash - временно удалит все изменения на локальной машине
- git pull - подтянет с сервера изменения и обновит файлы
- git stash pop - вернёт все изменения обратно


## Локальный setup
**Клонируем репозиторий себе на компьютер:**
```bash
$ git clone https://github.com/alpha-coders-team/todo-app.git
```

**Переходим в папку приложения:**
```bash
$ cd todo-app/
```

**Создаем виртуальное окружение:**
```bash
$ python -m venv venv
```

**Запускаем виртуальное окружение:**

(Для пользователей Windows)
```bash
$ source venv/Scripts/activate
```
(Для пользователей Linux)
```bash
$ source venv/bin/activate
```

**Устанавливаем зависимости:**
```bash
$ pip install -r requirements.txt
```

**Применяем миграции:**
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

**Запускаем локальный сервер джанго:**
```bash
$ python manage.py runserver
```


## Contributors
- [Nikita](https://github.com/gaikanomer9)
- [Igor Markin](https://github.com/igor-markin)
- [Andrey Vostrikov](https://github.com/vavsar)
- [Yaroslav](https://github.com/zzstop)
- [LeushElena](https://github.com/LeushElena)
- [Angelina](https://github.com/myagkova)
