# 👋 Django Greeting App

**Кейс-задача № 3** — Веб-приложение на Django для персонализированного приветствия пользователей.

---

## 📋 Описание

Простое веб-приложение на фреймворке Django, которое позволяет пользователям вводить своё имя через форму, сохраняет его в базе данных и отображает персонализированное приветствие на главной странице.

---

## ✨ Функциональность

### Реализованные возможности:

1. **Форма ввода имени** — пользователь вводит имя в текстовое поле
2. **Сохранение в базу данных** — имя сохраняется в модели Django (SQLite)
3. **Персонализированное приветствие** — отображение "Привет, [Имя]! 👋" после отправки
4. **Валидация формы** — проверка на пустое поле с выводом ошибки
5. **Защита от CSRF** — использование `{% csrf_token %}` для безопасности
6. **Современная стилизация** — градиентный фон, скругленные углы, эффекты hover
7. **Обработка ошибок** — отображение понятных сообщений об ошибках

---

## 🏗️ Структура проекта

```
greeting_3/
├── greeting/                         # Django приложение
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py           # Создание таблицы UserName
│   ├── templates/
│   │   └── greeting/
│   │       └── index.html            # Главная страница
│   ├── __init__.py
│   ├── admin.py                      # Админ-панель
│   ├── apps.py                       # Конфигурация приложения
│   ├── forms.py                      # Форма ввода имени
│   ├── models.py                     # Модель UserName
│   ├── urls.py                       # URL маршруты приложения
│   └── views.py                      # Представления (view)
├── greeting_project/                 # Корневой проект Django
│   ├── __init__.py
│   ├── asgi.py                       # ASGI конфигурация
│   ├── settings.py                   # Настройки проекта
│   ├── urls.py                       # Главные URL маршруты
│   └── wsgi.py                       # WSGI конфигурация
├── db.sqlite3                        # База данных SQLite
├── manage.py                         # Django CLI утилита
└── README.md                         # Этот файл
```

---

## 🚀 Установка и запуск

### Требования:
- Python 3.8+
- Django 4.2+

### Шаг 1: Клонирование проекта

```bash
git clone <repository-url>
cd greeting_3
```

### Шаг 2: Создание виртуального окружения

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Шаг 3: Установка зависимостей

```bash
pip install django
```

Или через requirements.txt:

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
Django==4.2.30
```

### Шаг 4: Применение миграций

```bash
python manage.py migrate
```

### Шаг 5: Создание суперпользователя (опционально)

```bash
python manage.py createsuperuser
```

### Шаг 6: Запуск сервера разработки

```bash
python manage.py runserver
```

### Шаг 7: Открытие в браузере

Откройте: **http://127.0.0.1:8000/**

---

## 💡 Использование

### Сценарий 1: Первое посещение

1. Откройте главную страницу
2. Увидите форму с полем "Введите ваше имя"
3. Введите имя, например "Иван"
4. Нажмите кнопку **Submit**
5. Появится приветствие: **"Привет, Иван! 👋"**

### Сценарий 2: Попытка отправить пустую форму

1. Оставьте поле пустым
2. Нажмите **Submit**
3. Появится ошибка: **"Имя не может быть пустым"**

### Сценарий 3: Просмотр сохранённых имён

1. Перейдите в админ-панель: http://127.0.0.1:8000/admin/
2. Войдите с учётными данными суперпользователя
3. Выберите раздел **User names**
4. Увидите список всех введённых имён

---

## 🛠️ Технические детали

### Модель данных (models.py)

```python
class UserName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

**Поля:**
- `id` — автоинкрементный первичный ключ (создаётся автоматически)
- `name` — текстовое поле для хранения имени (максимум 100 символов)

### Форма (forms.py)

```python
class NameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваше имя'
            })
        }
        labels = {
            'name': ''  # Скрыть label
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not name.strip():
            raise forms.ValidationError('Имя не может быть пустым')
        return name.strip()
```

**Особенности:**
- Используется `ModelForm` для связи с моделью
- Кастомная валидация через `clean_name()`
- Удаление пробелов в начале и конце (`strip()`)
- Проверка на пустое значение

### Представление (views.py)

```python
def index(request):
    greeting_name = None

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user = form.save()           # Сохранение в БД
            greeting_name = user.name    # Получение имени
            form = NameForm()            # Очистка формы
    else:
        form = NameForm()

    return render(request, 'greeting/index.html', {
        'form': form,
        'greeting_name': greeting_name,
    })
```

**Логика работы:**
1. При **GET** запросе — отображается пустая форма
2. При **POST** запросе:
   - Валидация формы
   - Сохранение в базу данных
   - Отображение приветствия
   - Очистка формы для нового ввода

### Шаблон (index.html)

```html
{% if greeting_name %}
    <p class="greeting-text">Привет, {{ greeting_name }}! 👋</p>
{% endif %}

<form method="post">
    {% csrf_token %}

    {% if form.name.errors %}
        <div class="error-text">
            {{ form.name.errors.0 }}
        </div>
    {% endif %}

    {{ form.name }}
    <button type="submit" class="btn-submit">Submit</button>
</form>
```

**Компоненты:**
- `{% csrf_token %}` — защита от CSRF атак
- `{{ form.name }}` — рендер поля формы
- `{{ form.name.errors }}` — вывод ошибок валидации
- `{{ greeting_name }}` — условное отображение приветствия

---

## 🎨 Стилизация

### CSS-дизайн:

- **Фон:** Градиент от `#667eea` к `#764ba2` (фиолетово-синий)
- **Контейнер:** Белая карточка с тенью и скруглением 12px
- **Поля ввода:** 
  - Граница 2px, скругление 8px
  - Фокус: фиолетовая граница `#764ba2`
- **Кнопка:** 
  - Фон: `#764ba2`
  - Hover: `#5e3a85` (темнее)
  - Скругление 8px
- **Центрирование:** Flexbox для вертикального и горизонтального выравнивания

---

## Выполнение требований ТЗ

| Требование | Статус |
|------------|--------|
| Форма ввода имени с кнопкой Submit | Реализовано |
| Модель Django с полем "name" | Реализовано |
| Сохранение имени в БД | Реализовано |
| Персонализированное приветствие | Реализовано |
| Обработка ошибок (пустое поле) | Реализовано |
| CSS стилизация | Реализовано |
| Защита от CSRF атак | Реализовано |

---

## 🔒 Безопасность

### Реализованные меры:

1. **CSRF Protection** — включён `CsrfViewMiddleware` в настройках
   ```python
   MIDDLEWARE = [
       # ...
       'django.middleware.csrf.CsrfViewMiddleware',
       # ...
   ]
   ```

2. **XSS Protection** — Django автоматически экранирует вывод в шаблонах
   ```html
   {{ greeting_name }}  <!-- Безопасный вывод -->
   ```

3. **SQL Injection Protection** — использование ORM вместо сырых SQL запросов
   ```python
   form.save()  # Безопасное сохранение через ORM
   ```

4. **Валидация на уровне формы** — проверка и очистка данных
   ```python
   def clean_name(self):
       name = self.cleaned_data.get('name')
       return name.strip()  # Удаление лишних пробелов
   ```

5. **Clickjacking Protection** — включён `XFrameOptionsMiddleware`

---

## 🎯 Возможные улучшения

### Функциональные:
- [ ] Добавить список последних приветствий на странице
- [ ] Реализовать пагинацию для истории имён
- [ ] Добавить поиск по сохранённым именам в админ-панели
- [ ] Счётчик количества использований каждого имени
- [ ] Экспорт данных в CSV/JSON

### UI/UX:
- [ ] Анимация появления приветствия
- [ ] Toast-уведомления вместо встроенных ошибок
- [ ] Адаптивный дизайн для мобильных устройств
- [ ] Тёмная тема
- [ ] Поддержка разных языков (i18n)

### Технические:
- [ ] Миграция на PostgreSQL для продакшена
- [ ] Добавить Docker контейнеризацию
- [ ] Настроить CI/CD (GitHub Actions)
- [ ] Написать unit-тесты (Django TestCase)
- [ ] Добавить логирование
- [ ] Настроить статику через WhiteNoise
- [ ] Реализовать кеширование (Redis)

### Безопасность:
- [ ] Настроить HTTPS в продакшене
- [ ] Включить rate limiting для защиты от спама
- [ ] Добавить CAPTCHA
- [ ] Использовать переменные окружения для SECRET_KEY
- [ ] Настроить ALLOWED_HOSTS для продакшена

---

## 📊 База данных

### Таблица UserName

| Поле | Тип | Описание |
|------|-----|----------|
| id | BigAutoField | Первичный ключ (автоинкремент) |
| name | CharField(100) | Имя пользователя |

**SQL эквивалент:**
```sql
CREATE TABLE greeting_username (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);
```

### Примеры записей:

| id | name |
|----|------|
| 1 | Иван |
| 2 | Мария |
| 3 | Алексей |

---

## 📝 Команды управления

```bash
# Создание приложения
python manage.py startapp greeting

# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Запуск сервера
python manage.py runserver

# Создание суперпользователя
python manage.py createsuperuser

# Запуск shell
python manage.py shell

# Запуск тестов
python manage.py test

# Сбор статики
python manage.py collectstatic
```

---

**Автор:** Лёнин Никита Юрьевич
