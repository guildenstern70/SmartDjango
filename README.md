# SmartDjango

![SmartDjango CI](https://github.com/guildenstern70/SmartDjango/workflows/SmartDjango%20CI/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/56d6e895837d4fcc93387e33eb774adc)](https://www.codacy.com/gh/guildenstern70/SmartDjango/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=guildenstern70/SmartDjango&amp;utm_campaign=Badge_Grade)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0.6-green?logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white)

## Description

SmartDjango is a modern Django 6 starter template featuring:

| | |
|---|---|
| **Backend** | Python 3.13 · Django 6.0.6 |
| **Frontend** | Bootstrap 5.3.6 (dark mode) · Bootstrap Icons 1.11.3 · Inter font |
| **Forms** | django-crispy-forms · crispy-bootstrap5 |
| **Database** | SQLite (default) · PostgreSQL via Supabase |
| **Server** | Gunicorn · WhiteNoise · Docker-ready |

The UI uses a dark-mode-first design system with glassmorphism cards, an indigo accent palette, animated hero, and a single custom CSS file — no extra frameworks.

---

## Setup

### Requirements

- Python **3.12 or newer** (3.13 recommended — required by Django 6.0)
- pip

### Virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Database setup

By default the app uses SQLite. Run these commands once after cloning:

```bash
python manage.py makemigrations SmartDjango
python manage.py migrate
python manage.py loaddata SmartDjango/fixtures/initial_data.yaml
```

### PostgreSQL (Supabase)

1. Set your Supabase credentials in `SmartDjango/settings.py` (the `supabase` database block).
2. Prefix every manage command with `DJANGO_DATABASE='supabase'`:

```bash
DJANGO_DATABASE='supabase' python manage.py migrate
DJANGO_DATABASE='supabase' python manage.py createsuperuser
DJANGO_DATABASE='supabase' python manage.py runserver
```

---

## Local run

The quickest way to start everything (migrate, seed, collect static, launch Gunicorn):

```bash
./run.sh
```

For the Django development server only:

```bash
python manage.py runserver
```

The app will be available at **http://localhost:8000** (dev server) or **http://localhost:8080** (Gunicorn via `run.sh`).

Default credentials: `admin / admin` or `guest / guest`.

---

## Admin

Create a superuser manually if needed:

```bash
python manage.py createsuperuser
```

Then visit `/admin/`.

---

## Docker

```bash
docker build --platform linux/amd64 -t smart-django:latest .
docker run -p 8080:8080 smart-django:latest
```

The Docker image is based on `python:3.13-slim-bookworm`.

---

## Reset database

```bash
# SQLite
python manage.py flush

# PostgreSQL
python manage.py flush --database=supabase
```

To drop all PostgreSQL tables and start fresh:

```sql
do $$ declare
    r record;
begin
    for r in (select tablename from pg_tables where schemaname = 'public') loop
        execute 'drop table if exists ' || quote_ident(r.tablename) || ' cascade';
    end loop;
end $$;
```

---

## Project structure

```
SmartDjango/
├── SmartDjango/          # Django project package
│   ├── settings.py       # Config (pathlib BASE_DIR, DEFAULT_AUTO_FIELD, etc.)
│   ├── urls.py           # URL routing
│   ├── views.py          # Page & auth views
│   ├── forms.py          # Crispy forms
│   ├── models.py         # Brand, Car models
│   ├── db_utils.py       # Seed helpers
│   ├── static/
│   │   └── SmartDjango/
│   │       ├── css/main.css   # Full design system (single file)
│   │       ├── js/            # main.js, cars.js
│   │       └── img/           # Brand logos, favicons
│   └── fixtures/
│       └── initial_data.yaml
├── templates/
│   ├── skeleton.html     # Base HTML (Bootstrap 5.3, dark mode, Inter)
│   ├── base-nav.html     # Layout with glass navbar + footer
│   ├── header.html       # Glassmorphism navbar
│   ├── footer.html       # Dark three-column footer
│   ├── index.html        # Hero landing page
│   ├── homepage.html     # Dashboard with feature cards
│   ├── cars.html         # Car management table + modals
│   ├── anotherpage.html  # Generic placeholder page
│   └── account/
│       ├── login.html
│       ├── profile.html
│       ├── registration.html
│       └── registration_ok.html
├── manage.py
├── run.sh
├── Dockerfile            # python:3.13-slim-bookworm
└── requirements.txt
```

---

## Dependencies

Key packages (see `requirements.txt` for pinned versions):

- [`Django`](https://www.djangoproject.com/) 6.0.6
- [`django-crispy-forms`](https://django-crispy-forms.readthedocs.io/) + `crispy-bootstrap5` 2026.3
- [`whitenoise`](https://whitenoise.readthedocs.io/) — static file serving
- [`gunicorn`](https://gunicorn.org/) — production WSGI server
- [`psycopg`](https://www.psycopg.org/) — PostgreSQL adapter
- [`django-feather`](https://pypi.org/project/django-feather/) — Feather icon template tags

---

## Changelog

### 2026-06
- Upgraded Django 5.2.9 → **6.0.6**
- Upgraded crispy-bootstrap5 2025.6 → **2026.3** (Django 6 support)
- Docker base image updated `python:3.11-slim-buster` → **python:3.13-slim-bookworm**
- `settings.py`: migrated `BASE_DIR` to `pathlib.Path`, removed `USE_L10N`, added `DEFAULT_AUTO_FIELD`
- Full UI overhaul: dark-mode design system, glassmorphism navbar/cards, Bootstrap 5.3.6, Inter font, Bootstrap Icons 1.11.3, animated hero, feature-card dashboard, redesigned all 9 templates

---

## License

[MIT](LICENSE) © 2026 Alessio Saltarin
