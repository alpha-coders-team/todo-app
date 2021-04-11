# ToDo Application

[![App Status](https://argo.alpha-coders.team/api/badge?name=todo&revision=true)](https://argo.alpha-coders.team/applications/todo)
## Описание
ToDo Application — сервис, который помогает привести дела в порядок. Люди добавляют здесь задачи и сортируют по приоритету, чтобы ничего не забыть и сделать вовремя. Категории и подзадачи помогают структурировать информацию, а комментарии — не упустить детали.

## Как поддерживать проект и присоединиться к разработке?

### Что можно делать?

Основной источник задач - это issues в Github https://github.com/alpha-coders-team/todo-app/issues

Выбирайте задачку по душе и спрашивайте в комментариях свободна ли она для вас. Если вы готовы ее взять, вас назначат исполнителем. Если будут любые вопросы, их можно обсудить в issue к задаче либо в дискорде проекта. Приглашение доступно у [Никиты Завьялова](https://github.com/gaikanomer9)

**Как еще можно помочь проекту?**

Если нет времени писать код, то можно тестировать приложение или создавать новые issues. Можно создавать задачки на рефакторинг текущего кода, либо предлагать улучшения. Так что, если нашли баг или у вас есть идеи по улучшению приложения, смело открывайте новый issue на страничке проекта.
### Работа с Pull Request

Перед началом работы с проектом необходимо:

    Сделать форк проекта (на главной странице проекта нажать кнопку fork)

    Клонировать форк репозитория к себе
    - git clone git@github.com:your-user-name/todo-app.git

    Создать новую ветку
    - cd todo-app
    - git checkout -b add-user-to-contributors


После внесения изменений в проект необходимо:

    Отправить изменения на удаленный сервер в свой форк
    - git add 'modified file'
    - git commit -m "message"
    - git push origin add-user-to-contributors

    Открыть Pull Request на странице https://github.com/alpha-coders-team/todo-app/compare
    - Выбрать созданную ветку в своем форке как compare и master ветку как base

### Первый Pull Request

В качестве первого Pull Request добавьте себя в список Contributors внизу Readme.md страницы и откройте Pull Request. Попросить помощи можно здесь https://github.com/alpha-coders-team/todo-app/issues/62
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
