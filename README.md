# 💱 Django Currency Converter (No API)

A simple web-based currency converter built with Django that performs real-time currency conversion **without using any third-party APIs**. Instead, it uses a predefined set of exchange rates stored locally.

---

## 🚀 Features

- Convert between popular currencies (e.g., USD, EUR, INR, GBP, JPY, etc.)
- No need for internet access to fetch conversion rates
- User-friendly interface with clean styling
- Lightweight and fast – perfect for learning Django basics

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Django 4+
- **Frontend**: HTML, CSS (optional: Bootstrap for styling)
- **Database**: SQLite (default Django DB)

---

## 📁 Project Structure

```
currency_converter/
├── converter/        
│   ├── migrations/
│   ├── static/        
│   ├── templates/
│   │   └── converter/
│   │       └── base.html
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py       
│   ├── urls.py
│   └── views.py
├── currency_converter/  
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-currency-converter.git
cd django-currency-converter
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn’t exist, simply install Django:
```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Then open your browser and go to:  
**`http://127.0.0.1:8000/`**

---

## 🔄 How It Works

- A fixed dictionary of currency rates (relative to a base currency like USD) is stored in `views.py` or optionally in a model.
- The user selects the source and target currencies, enters the amount, and the view calculates the converted value using simple math.
- No external API is used, so it's ideal for offline use or educational purposes.

Example:
```python
exchange_rates = {
    'USD': 1.0,
    'INR': 83.0,
    'EUR': 0.91,
    'GBP': 0.78,
    'JPY': 151.3,
}
```

Formula:
```
converted_amount = (amount / source_rate) * target_rate
```

---

## 📸 Screenshots

> Add screenshots of your website here for visual reference (if available)

---

## ✨ Future Improvements

- Admin interface to update rates dynamically
- Add historical conversion tracking
- Add unit tests
- Dark mode toggle

---

## 🤝 Contributing

Feel free to fork the repo and submit a pull request. Contributions are always welcome!

---

## 📄 License

This project is open-source and available.

---

## 🙋‍♂️ Questions?

If you have any questions, feel free to reach out via [GitHub Issues](https://github.com/Pxdarkshadow/django-currency-converter/issues) or open a discussion!

---
```
