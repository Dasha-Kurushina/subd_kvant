#Тема курсовой работы: «Проектирование и разработка структуры данных подсистемы выдачи сертификатов в детском технопарке "Кванториум фотоника"».
##Цель - представить разработанную структуру, обеспечить генерацию, хранение и обработку сертификатов.
## Задачи:
1. Изучить существующие системы 
2. Изучить процесс выдачи сертификатов
3. Выбрать и обосновать СУБД
4. Спроектировать структуру данных
5. Реализовать прототип и произвести тестирование.

# Лабораторные работы:
##Блок 1 - Задачи аэропорта.

1. Поиск билетов (по заданным критериям, в том числе с одной или двумя стыковками на заданные дни на заданное количество пассажиров).
2. Продажа билетов (с проверкой наличия мест)
3. Регистрация на рейс
4. Отправка/прием самолета
1. Поиск сертификата по его номеру и фамилии учащегося
2. Система выдачи сертификата с генерацией его номера
3. Регистрация учащихся для выдачи сертификатов
4. Выдача/проверка сертификата


##Блок 2 - Задачи авиакомпании.

1. Добавление рейсов в расписание (одиночных и периодических)
2. Отмена рейса (предусмотреть поиск всех затронутых пассажиров)
3. Добавление новых типов самолетов с планировкой салона
4. Замена самолета. Предусмотреть, чтобы все проданные билеты смогли разместиться в новом самолете, при необходимости сбросить выданные посадочные талоны.
1. Добавление нового учащегося
2. Отзыв сертификата
3. Добавление нового типа сертификата
4. Прием сертификата в качестве вступительного экзамена


##Блок 3 - Статистика. 

1. Определение популярных направлений перелетов в диапазоне дат. Как за весь диапазон целиком, так и с внутренней агрегаций (за каждый из дней/месяц).
2. Статистика заполненности перелетов в диапазоне дат и в разрезе дней недели.
3. Сравнение заполненности конкретных рейсов со средней заполненностью по этим же рейсам в эти же дни недели за прошлые периоды.
4. Любой аналитический запрос к базе данных. Запрос должен иметь смысл с точки зрения предметной области.
1. Определение популярных направлений обучения 
2. Статистика загруженности преподавателей
3. Сравнение выданных сертификатов в этом году с предыдущим
4. Показать количество запросов на проверку поддельных сертификатов, или другой аналитический запрос.


Вся логика должна быть реализована в виде функций на pl/pgsql в базе данных.
Интерфейс не требуется. В рамках ЛР должны быть разработаны API для всех действий и форматы обмена данными в предположении, что указанные API будут использоваться во внешней системе.