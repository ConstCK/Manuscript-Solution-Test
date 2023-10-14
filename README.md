Скопируйте проект к себе на ПК при помощи: git clone https://github.com/ConstCK/Manuscript-Solution-Test.git
Создайте виртуальное окружение (python -m venv venv) и активируйте его (venv\scripts\activate)
Установите все зависимости при помощи pip install -r requirements.txt в терминале
Создайте файл .env в каталоге проекта и пропишите в нем SECRET_KEY = Сгенерированный ключ
Ключ для Django можно сгенерировать по пути https://djecrety.ir/
Запустите сервер из каталога проекта (python manage.py runserver)

Маршрут для создания БД из xlsx файла (занимает около 1,5 мин):
http://127.0.0.1:8000/data_in/


Маршрут для создания tsv файла:
http://127.0.0.1:8000/data_out/

Маршрут для доступа к панели администрирования
http://127.0.0.1:8000/admin/
login/password : admin

Примечание:
В data.xlsx в колонке ID_TOVAR (строка 841) была ошибка (исправил в исходнике). 