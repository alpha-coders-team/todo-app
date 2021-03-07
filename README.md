# ToDo Application

## Описание
ToDo Application — сервис, который помогает привести дела в порядок. Люди добавляют здесь задачи и сортируют по приоритету, чтобы ничего не забыть и сделать вовремя. Категории и подзадачи помогают структурировать информацию, а комментарии — не упустить детали.

## Как поддерживать проект и присоединиться к разработке?
Перед началом работы с проектом необходимо:

    Клонировать текущий репозиторий проекта
    - git clone git@github.com:alpha-coders-team/todo-app.git

    Создать новую ветку
    - cd todo-app 
    - git checkout -b add-user-to-contributors


После внесения изменений в проект необходимо:

    Отправить изменения на удаленный сервер
    - git add 'modified file'
    - git commit -m "message"
    - git push origin add-user-to-contributors

    На сайте github открыть Pull Request
    - выбрать Compare & pull request
      или
    - выбрать Pull requests => New pull request 

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
$ cd todo_app-app/
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
- [Kirill Beliakov](https://github.com/blkvk)
