Скопируйте проект к себе на ПК при помощи: git clone
Создайте виртуальное окружение (python -m venv venv) и активируйте его (venv\scripts\activate)
Установите все зависимости при помощи pip install -r requirements.txt в терминале
Создайте файл .env в каталоге проекта и пропишите в нем SECRET_KEY = Сгенерированный ключ
Ключ для Django можно сгенерировать по пути https://djecrety.ir/
Запустите сервер из каталога проекта (python manage.py runserver)

Маршрут для создания БД из xlsx файла (params: filename=Имя файла, sheet=Имя листа)
http://127.0.0.1:8000/create_db/?filename=data.xlsx&sheet=ManuSnab1

Маршрут для создания tsv файла (params: filename=Имя файла)
http://127.0.0.1:8000/create_file/?filename=data.tsv

Маршрут для доступа к панели администрирования
http://127.0.0.1:8000/admin/
login/password : admin
