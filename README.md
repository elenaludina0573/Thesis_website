### Необходимо создать сайт для компании медицинской диагностики. 
Сайт должен быть сверстан и подключен к админке. 
Для выполнения задачи необходимо использовать Django и Bootstrap. 
Сайт должен содержать основные разделы, необходимые для
функционирования медицинской диагностической компании.

### Установка:

1. #### Убедитесь, что у вас установлен python 3.11 или более новая версия

1. #### Убедитесь, что у вас установлен PostgreSQL и запущен локальный сервер для базы данных

1. #### Склонировать репозиторий

1. #### Установить зависимости командой `pip install -r requirements.txt`

1. #### В файле .env.sample заполнить данные для работы с проектом и переименовать его в .env

1. #### Запустить через команду `python manage.py runserver`

1. #### Запустить команду `python manage.py ccsu`, зайти в админку под администратором для заполнения данных в базе данных и прав доступа.

    * ####    _Анонимный пользователь может просматривать главную страницу с общей информацией по услугам. врачей и записаться на прием._

    * ####    _Зарегистрированный пользователь может просматривать вкладку диагностика с результатами обследования, стоимость услуг и записаться на прием._

    * ####    _Модератор может просматривать, редактировать, создавать, удалять клиентов и записи на прием, просматривать диагностику и управлять услугами (кроме удаления)._

    * ####    _Администратор может просматривать, создавать, редактировать и удалять любые услуги, записи на прием, диагностику, клиентов и докторов (в админке)_

### Используемый стэк:

* #### HTML-вёрстка

* #### CSS на основе шаблонов bootstrap

* #### База данных PostgreSQL

* #### Кеширование двух контроллеров: список докторов и список услуг

* #### Django
