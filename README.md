YaMDb (Яндекс.Практикум)
=====

Описание проекта
----------
Командный проект создан в рамках учебного курса Яндекс.Практикум.

Проект YaMDb собирает отзывы пользователей на произведения.

<details>
<summary>Подробнее</summary>

Описание
----

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).

Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

Ресурсы API YaMDb
---

Ресурс **auth**: аутентификация.

Ресурс **users**: пользователи.

Ресурс **titles**: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

Ресурс **categories**: категории (типы) произведений («Фильмы», «Книги», «Музыка»). Одно произведение может быть привязано только к одной категории.

Ресурс **genres**: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.

Ресурс **reviews**: отзывы на произведения. Отзыв привязан к определённому произведению.

Ресурс **comments**: комментарии к отзывам. Комментарий привязан к определённому отзыву.

Каждый ресурс описан в документации: указаны эндпоинты (адреса, по которым можно сделать запрос), разрешённые типы запросов, права доступа и дополнительные параметры, когда это необходимо.


Пользовательские роли и права доступа
---

**Аноним** — может просматривать описания произведений, читать отзывы и комментарии.

**Аутентифицированный пользователь** (`user`) — может читать всё, как и **Аноним**, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.

**Модератор** (`moderator`) — те же права, что и у **Аутентифицированного пользователя**, плюс право удалять и редактировать любые отзывы и комментарии.

**Администратор** (`admin`) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.

Суперюзер **Django** должен всегда обладать правами администратора, пользователя с правами `admin`. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.

</details>

Установка проекта из репозитория
----------

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/Maltassarus/api_yamdb.git

cd api_yamdb
```
2. Cоздать и активировать виртуальное окружение:
* Windows
```bash
python -m venv venv

source venv/Scripts/activate
```
* Mac
```bash
python3 -m venv venv

source venv/bin/activate
```
3. Установить зависимости из файла ```requirements.txt```:
```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
cd api_yamdb

python manage.py migrate
```
5. Запустить проект:
```bash
python manage.py runserver
```
Документация к проекту
----------
Документация для API доступна после запуска по адресу [`http://127.0.0.1:8000/redoc/`](http://127.0.0.1:8000/redoc/).
