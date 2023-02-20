# Django + Stripe API бэкенд

## Описание проекта stripe_payment
Данный проект реализует Django + Stripe API бэкенд с возможностью покупки предметов (Item) через платежную систему Stripe с использованием Stripe Payment Intent API. Кроме того, реализованы модели для заказов (Order), скидок (Discount) и налогов (Tax), которые могут быть применены к заказу.

API предоставляет следующие методы:

- GET '' - главная страница проекта которая позволяет получить HTML-страницы со списком всех Items.
- GET /item/{id}/ - позволяет получить HTML-страницу с информацией о выбранном Item и кнопкой Buy. При нажатии на кнопку Buy происходит запрос на /buy/{id}/, получение payment_intent.id и редирект на страницу оплаты через библиотеку Stripe.
- GET /buy/{id}/- позволяет получить Stripe Payment Intent ID для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe выполняется запрос stripe.PaymentIntent.create(...) и полученный payment_intent.id возвращается в результате запроса.
- GET /order/{id}/- Подробная информация об конкретном заказе.

### Развёрнутый проект

```
http://158.160.42.241/admin/
http://158.160.42.241
```

## Запуск проекта

Для запуска проекта необходимо выполнить следующие шаги:

1. Установить Docker на свой компьютер, если он еще не установлен. Инструкции по установке можно найти на официальном сайте Docker.

2. Клонировать репозиторий на свой компьютер с помощью команды:
```
git clone https://github.com/umar1593/stripe_payment.git
```
3. Перейти в папку проекта:
```
cd stripe_payment
```
4. Создать файл .env в корневой директории проекта и добавить в него свои значения для переменных окружения:
```
SECRET_KEY=your_secret_key
STRIPE_API_KEY=your_stripe_api_key
```
При этом необходимо заменить your_secret_key, your_stripe_api_key и your_stripe_webhook_secret на свои значения.

5. Собрать и запустить контейнеры Docker с помощью команды:
```
docker-compose up --build
```
6. Создать суперпользователя Django:
```
docker-compose exec web python manage.py createsuperuser
```
7. Открыть веб-браузер и перейти по адресу http://127.0.0.1:8000/admin/. Войти в Django Admin панель с помощью созданного суперпользователя.

### Над проектом работал:  _[< Умар Ширваниев >](https://github.com/umar1593)_
