# ToDo Application

[![App Status](https://argo.alpha-coders.team/api/badge?name=todo&revision=true)](https://argo.alpha-coders.team/applications/todo)
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

**Чтобы работали логин через Вконтакте**
- Зайти на https://vk.com/dev, пункт Мои приложения
- Нажать кнопку "Создать"
- Задать любое название, выбрать пункт "сайт"
- В полях "Адрес сайта" и "Базовый домен" указать http://127.0.0.1 и Сохранить
- Перейти в "Настройки"

- В отдельной вкладке зайти в панель администратора: http://localhost:8000/admin/
- Пункт "Социальные приложения", "Добавить социальное приложение"
```bash
    Провайдер: вк
    Имя: любое
    id клиента = id приложения Вконтакте
    Секретный ключ = Защищённый ключ приложения Вконтакте
    Ключ = Сервисный ключ доступа приложения Вконтакте
    Пункт "sites" -> Добавить сайт в выбранные
 ```
    
**Чтобы работали логин через почту Google**
- Почта гугл, настройки (шестеренка), Пересылка и POP/IMAP, включить Включить IMAP
- Управление аккаунтом гугл, безопасность, включить Небезопасные приложения разрешены

- Перейти на https://developers.google.com/gmail/api/quickstart/js
- "Enable the Gmail API", задать имя, "next"
- Перейти на https://console.developers.google.com/apis/credentials
- Выбрать созданное приложение
- Перейти на Credentials, OAuth client

- В отдельной вкладке зайти в панель администратора: http://localhost:8000/admin/
- Пункт "Социальные приложения", "Добавить социальное приложение"
```bash
    Провайдер: google
    Имя: любое
    id клиента = Client ID
    Секретный ключ = Client secret
    Ключ = оставить пустым
    Пункт "sites" -> Добавить сайт в выбранные
```
- Сохранить


## CI/CD

### Создание локального образа

docker build -t todo .
### Отправка образа в GCR
docker tag todo eu.gcr.io/alpha-team-praktikum/todo_app
docker push eu.gcr.io/alpha-team-praktikum/todo_app

### Миграция базы данных
kubectl run mysql-client --rm --tty -i --restart='Never' --image  eu.gcr.io/alpha-team-praktikum/todo_app:latest --namespace alpha-space --command -- sh -c "python manage.py createsuperuser"

docker run --env-file .env-local todo sh -c "python manage.py makemigrations && python manage.py migrate"

## База данных

### Подключение к базе данных

PostgreSQL can be accessed via port 5432 on the following DNS name from within your cluster:

    postgresql.postgresql.svc.cluster.local - Read/Write connection

To get the password for "postgres" run:

    export POSTGRES_PASSWORD=$(kubectl get secret --namespace postgresql postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode)

To connect to your database run the following command:

    kubectl run postgresql-client --rm --tty -i --restart='Never' --namespace postgresql --image docker.io/bitnami/postgresql:11.11.0-debian-10-r50 --env="PGPASSWORD=$POSTGRES_PASSWORD" --command -- psql --host postgresql -U postgres -d postgres -p 5432

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace postgresql svc/postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432

## Contributors
- [Nikita](https://github.com/gaikanomer9)
- [Igor Markin](https://github.com/igor-markin)
- [Andrey Vostrikov](https://github.com/vavsar)
- [Yaroslav](https://github.com/zzstop)
- [LeushElena](https://github.com/LeushElena)
- [Angelina](https://github.com/myagkova)
- [Kirill Beliakov](https://github.com/blkvk)
