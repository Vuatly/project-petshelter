# Инструкция по запуску на локальном сервере.
1. Создать postgresql базу данных и подключить её в settings.py
2. Провести миграции в базу данных. ( python manage.py migrate )
3. Создать суперпользователя. ( python manage.py createsuperuser )
4. Запустить проект. ( python manage.py runserver )
