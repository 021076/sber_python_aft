# python_test_sber_api

# Запуск pytest-html отчета 
библиотеки: pytest-html
добавить в корень пустой файл conftest.py
команды в терминале
pytest test_suit --html=<путь\имя_отчета> --self-contained-html
*test_suit — название теста;
*--html=<путь\имя_отчета> — путь к папке и имя файла, с которым сохранится отчет;
*--self-contained-html — позволяет сохранять отчет одним файлом без вспомогательных css. 
PET: pytest ...<путь к проекту>\TestCases\PET\test_pet.py --html=...<путь к проекту>\Reports\pet_report.html --self-contained-html
USER: pytest ..<путь к проекту>\TestCases\USER\test_user.py --html=..<путь к проекту>\Reports\user_report.html --self-contained-html

# Параллельный запуск тестов
библиотеки: pytest-xdist
команды в терминале
pytest -n3
----где 3 - количество параллельных процессов

# Запуск allure отчета
!!!не работает на версии pytest больше 8.0!!!
доп.установки: allure-commandline - добавить в PATH, Установите Java Development Kit (JDK) Добавить в PATH и переменную JAVA-HOME
библиотеки: allure-pytest
команды в терминале для формирования данных, из которых будет сгенерироват allure отчет.
pytest test_suit --alluredir=<путь>
*test_suit — название теста;
*--alluredir=<путь> — путь к папке, куда сохранится отчет
PET: pytest ..<путь к проекту>\TestCases\PET\test_pet.py --alluredir=..<путь к проекту>\Reports
USER: pytest ..<путь к проекту>\TestCases\USER\test_user.py --alluredir=..<путь к проекту>\Reports
далее формирование allure:
в командной строке ОС
allure serve <путь к папке с отчетом>
..<путь к проекту>\Reports\



# Библиотеки, которые очень помогают в разработке автотестов:
Установка библиотек: pip install <имя_библиотеки> 
pytest — фреймворк, сильно упрощающий работу с тестами, — запуск, детализация выполнения, настройки запуска;
requests — библиотека с командами для отправки запросов REST API;
allure — удобные отчеты по результатам выполнения тестов;
dateutils — работа с датой и временем;
random — генерация случайных значений (встроенная);
pathlib — работа с путями к файлам;
configparser — если будете использовать конфиги по стендам, удобная библиотека для чтения конфигов;
pandas — чтение данных из Excel-файлов;
cx_Oracle — чтение данных из БД
pytest-html — отчеты в формате html — например, для интеграции с HP ALM;
pytest-rerunsfailures — автоматический перезапуск упавших тестов.