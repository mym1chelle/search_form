[![](https://img.shields.io/badge/python-v3.11-green)](https://img.shields.io/badge/python-v3.11-green)
<a href="https://codeclimate.com/github/mym1chelle/search_form/maintainability"><img src="https://api.codeclimate.com/v1/badges/61797893cb1706cf3f3a/maintainability" /></a>
<a href="https://codeclimate.com/github/mym1chelle/search_form/test_coverage"><img src="https://api.codeclimate.com/v1/badges/61797893cb1706cf3f3a/test_coverage" /></a>  

# Тестовое задание по вакансии разработчик Python

[Вакансия](https://hh.ru/vacancy/74409375)

## Установка
1. [Установить Poetry](https://python-poetry.org/docs/)
2. [Установить Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
3. Клонировать проект в локальную директорию:
```
git clone git@github.com:mym1chelle/search_form.git
```
4. В директории клонированного проекта, установить зависимости командой:
```
make install
```

## Запуск проекта
Проект запускается командой
```
make run
```

## Запуск тестов
Тесты запускаются командой
```
make test
```

## Выполнение запросов
Для выполнения запросов можно использовать утилиту curl, предварительно ее [установив](https://curl.se/download.html).

Пример:

```
curl -X POST 'http://127.0.0.1:8000/get_form'  -d 'user_email=ivanov@gmail.com&user_phone=%2B7 921 461 75 63&user_info=pawpaw'  -H "Content-Type: application/x-www-form-urlencoded"
```
> **Note**
> Клиент, отправляющий запрос, должен его кодировать, например, знак "+" должен быть заменён на код "%2B".
