# rest1
## Описание проекта:
#####Простой контроллер добавления Книг в список, по принципу CRUD.
Стек: Python 3, Django, Git.

Разработан по классической MVT архитектуре. 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/qwantilium/hw05_final.git
```

Cоздать и активировать виртуальное окружение(Linux):

```
python3 -m venv env
```
для linux
```
source env/bin/activate
```
или windows
```
source venv/Scripts/activate
```
далее
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в рабочую директорию
```
cd yatube
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
