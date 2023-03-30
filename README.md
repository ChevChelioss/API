# Проект тестирования интерфейса (API)
#### предназначен для тестирования API-функционала с использованием библиотеки pytest, фреймворка requests и библиотеки для валидации данных voluptuous. В проекте реализовано несколько тестовых сценариев, которые покрывают основные CRUD-операции (создание, чтение, обновление и удаление) для ресурса "Пользователи" (users) в рамках REST API сервиса [Reqres](https://reqres.in/).


<!-- Технологии -->

### Используемые технологии
<p  align="center">
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/python.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/pytest.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/pycharm.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/selene.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/allure_testops.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/allure_report.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/jenkins.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/selenium.png"></code>
<code><img height="50" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/jira.png"></code>
</p>

### Для запуска тестов необходимо установить следующие зависимости:

- Python 3
- Библиотеки pytest, requests, allure-pytest, voluptuous
- WebDriver для браузера Chrome
- Приложение Allure для формирования отчетов

### Для API-тестирования функционала используются следующие тесты:
- Тест на проверку успешного создания пользователя
- Тест на проверку успешного обновления данных пользователя
- Тест на проверку успешной регистрации пользователя
- Тест на проверку неудачной регистрации пользователя
- Тест на проверку успешного удаления пользователя


<!-- Jenkins -->

## <img height="30" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/jenkins.png"> Jenkins
### [JOB](https://jenkins.autotests.cloud/job/API_testing_qa_guru_python_3_jenkins/)
##### Кликните "Собрать сейчас"
запущенную сборку вы увидите в "Истории сборки" 

там же рядом появятся две кнопки - зеленая откроет для нас allure test ops, а желтая allure report  
![This is an image](screenshots/jenkins_job.PNG)

<!-- Allure TestOps -->

## <img height="30" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/allure_testops.png"> Allure TestOps
### [DASHBOARD](https://allure.autotests.cloud/launch/21112)
##### предоставляет общий обзор о процессе тестирования проекта, а также предоставляет различные метрики и отчеты для принятия решений на основе данных тестирования. Он позволяет визуализировать результаты тестирования и обнаруживать проблемы в продукте, что может помочь командам разработки улучшить качество своего продукта
![This is an image](screenshots/testOps_dashboards.PNG)

##### описывает тест-кейсы, которые должны быть выполнены для тестирования конкретной функциональности продукта. Это позволяет лучше структурировать и организовать процесс тестирования, а также легко отслеживать прогресс и результаты тестирования
![This is an image](screenshots/testOps_test_cases.PNG)

<!-- Allure report -->

## <img height="30" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/allure_report.png"> Allure Report
### [ALLURE REPORT](https://allure.autotests.cloud/launch/21112)
##### это инструмент для генерации отчетов о результатах тестирования, которые позволяют наглядно отображать статус выполнения тестов, результаты прохождения их шагов, а также информацию о возможных проблемах и ошибках
![This is an image](screenshots/allure_report.PNG)


<!-- Jira -->

## <img height="30" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/jira.png"> Интеграция с Jira
![This is an image](screenshots/jira.PNG)

<!-- Telegram -->

## <img height="30" src="https://github.com/ChevChelioss/ChevChelioss/blob/main/logo/tg.png"> Telegram
##### в проект добавлена функция отправки Allure report с ключевой информацией в Telegram
![This is an image](screenshots/telegram.PNG)
