# Сервис для распределения задач между студентами по алгоритмам *Algos*

## Что из себя представляет:
Это веб сайт, на котором регистрируются преподаватели, а затем их студенты, 
которые закрепляются за своим преподавателем, формируя группу.
Каждый преподаватель выкладывает для своей группы задачи, устанавливает дедлайн, балл за задачу и лимит.

## Чтоб запустить в интернете для теста:
Сначала "npm install -g localtunnel" <br />
Затем "lt --local-host 127.0.0.1 --port 8000" <br />
Там выдаст ссылку, по которой надо будет ввести свой IP

## Redis for windows:
https://github.com/tporadowski/redis/releases

## Creating DB
alembic revision --autogenerate -m "Database created" <br />
alembic upgrade head
