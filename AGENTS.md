# AGENTS.md

## Project overview
SmartDjango is a Django 6.x demo app using Bootstrap 5.3, SQLite by default, and optional PostgreSQL via the `supabase` database config. The UI uses a dark-mode design system with Inter font, glassmorphism cards, and a custom CSS design token layer on top of Bootstrap 5.3's native dark-mode support.

## Tech stack
| Layer | Technology |
|---|---|
| Backend | Python 3.13, Django 6.0.6 |
| Frontend | Bootstrap 5.3.6, Bootstrap Icons 1.11.3, Inter (Google Fonts) |
| Forms | django-crispy-forms 2.4, crispy-bootstrap5 2026.3 |
| Database | SQLite (default) / PostgreSQL via Supabase |
| Server | Gunicorn 23.x, WhiteNoise 6.9 |
| Container | Docker (python:3.13-slim-bookworm) |

## Key files
- `manage.py` — Django entry point.
- `run.sh` — local/container startup script: migrate, create superuser, makemigrations, collectstatic, load fixtures, then start Gunicorn on port `8080`.
- `SmartDjango/settings.py` — project settings; uses `pathlib.Path` for `BASE_DIR`; database selected via `DJANGO_DATABASE` env var; `DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'`.
- `SmartDjango/urls.py` — route map.
- `SmartDjango/views.py` — page logic and auth/car flows; `get_db_name()` casts `NAME` to `str` to handle both `Path` and string values.
- `SmartDjango/forms.py` — custom forms and Crispy Forms setup.
- `SmartDjango/models.py` — data models (`Brand`, `Car`).
- `SmartDjango/static/SmartDjango/css/main.css` — single CSS file containing the full design system (tokens, glassmorphism, table, auth, profile, hero, feature cards, Bootstrap overrides).
- `SmartDjango/static/SmartDjango/js/main.js` — active nav-link logic.
- `SmartDjango/static/SmartDjango/js/cars.js` — modal open/close and delete-link wiring.
- `templates/skeleton.html` — base HTML shell (Bootstrap 5.3 CDN, `data-bs-theme="dark"`, Inter).
- `templates/base-nav.html` — layout with navbar + footer wrappers.
- `templates/header.html` — glass navbar with Bootstrap Icons and avatar dropdown.
- `templates/footer.html` — dark three-column footer with DB badge.
- `templates/` — all page templates.

## Working conventions
- Keep changes small and aligned with the existing Django structure.
- Preserve the current app flow unless a task explicitly changes behaviour.
- Reuse the existing template and form patterns instead of introducing new frameworks.
- Follow the current naming and formatting style in the repo.
- All styling goes into `main.css`; do **not** add per-page CSS files.
- Use CSS custom properties (`--accent`, `--surface`, etc.) for any new colours or spacing values.
- `data-bs-theme="dark"` is set on `<html>` — Bootstrap's dark-mode variables are active globally.

## Common commands
- Local run: `./run.sh`
- Dev server: `python manage.py runserver`
- Install deps: `pip install -r requirements.txt`
- Django manage commands: `python manage.py <command>`
- PostgreSQL target: `DJANGO_DATABASE='supabase' python manage.py <command>`
- Run tests with deprecation warnings: `python -Wd manage.py test SmartDjango`
- Collect static: `python manage.py collectstatic --noinput`

## Notes
- The app uses Crispy Forms with the Bootstrap 5 template pack.
- `run.sh` assumes a default admin user if env vars are not set.
- Use the existing fixtures/migrations workflow when changing models.
- Django 6.0 requires Python 3.12+; the project currently targets Python 3.13.
- `DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'` is set explicitly in `settings.py` to preserve the existing `Car` model schema (32-bit integer PK).
- `USE_L10N` has been removed (it was dropped in Django 5.0).
