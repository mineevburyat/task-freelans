1. папка demonisation как демонизировать celery  в продакте
2. папка dockermultiservice вариант запуска докера с несколькими демонами-приложениями
3. папка fastapi_math



## Демонизация celery для systemd
1. Склонировать проект в /opt/celery/task-freelans
2. Скопировать celery.service в /etc/systemd/system/celery.service
Обращаем внимание на:
Type=forking
User=celery
Group=celery
EnvironmentFile=/etc/conf.d/celery
WorkingDirectory=/opt/celery
3. Создаем пользователя celery с группой celery
4. Папке /opt/celery  меняем владельца со всем содержимым chown -R celery:celery /opt/celery
5. Файл с переменными окружения копируем в /etc/conf.d (если нет создаём)
Обращаем внимание на CELERY_APP="proj"
т.е. приложение у нас fastapi_math - переименовываем и эта папка должна лежать непосредственно в workdirectory.
Либо меняем WorkingDirectory
6. Копируем celery.conf в /etc/tmpfiles.d - для создания временных папок для PID и log
7. Перечитать сервисы systemctl deamon-reload
8. Разрешить стартовать при запуске systemctl enable celery.service
9. systemctl start celery.service

## Демонизация fastapi с помощью systemd
1. Создать service файл: type=simple запускать через оболочку bash

### For use project
Requires the following libraries to be installed:
* pip install fastapi[all]
* pip install uvicorn
* pip install psutil  

After installetions run it:  

* python main.py - start application in console mode with info debug
* uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 - start with workers on multiprocessor product host
* gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 - i dont now why
