# ToDo Application

## Описание
TODO: несколько слов о проекте 

## Как поддерживать проект и присоединиться к разработке?
Перед каждым коммитом проверяйте, что в репозитории нет изменений командой git pull. Если во время работы на локальной машине ваши коллеги запушили код, то воспользуйтесь инструкцией ниже. Таким образом мы избежим конфликтов версий и не будем плодить лишние коммиты с изменениями.
- git stash - временно удалит все изменения на локальной машине
- git pull - подтянет с сервера изменения и обновит файлы
- git stash pop - вернёт все изменения обратно


## Локальный setup
Клонируем репозиторий себе на компьютер:

$ git clone https://github.com/alpha-coders-team/todo-app.git

Создаем виртуальное окружение:

$ python -m venv venv

Устанавливаем зависимости:

$ pip install -r requirements.txt

Применяем миграции:

$ python manage.py makemigrations 

$ python manage.py migrate

Запускаем локальный сервер джанго:

$ python manage.py runserver


## Contributors
- [Nikita](https://github.com/gaikanomer9)
- [Igor Markin](https://github.com/igor-markin)
- [Andrey Vostrikov](https://github.com/vavsar)
- [Yaroslav](https://github.com/zzstop)
- [LeushElena](https://github.com/LeushElena)
- [Angelina](https://github.com/myagkova)
