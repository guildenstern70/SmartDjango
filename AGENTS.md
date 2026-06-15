# AGENTS.md

## Project overview
SmartDjango is a Django 5.x demo app using Bootstrap 5, SQLite by default, and optional PostgreSQL via the `supabase` database config.

## Key files
- `manage.py` Django entry point.
- `run.sh` local/container startup script: migrate, create superuser, makemigrations, collectstatic, load fixtures, then start Gunicorn on port `8080`.
- `SmartDjango/settings.py` project settings and database selection via `DJANGO_DATABASE`.
- `SmartDjango/urls.py` route map.
- `SmartDjango/views.py` page logic and auth/car flows.
- `SmartDjango/forms.py` custom forms and Crispy Forms setup.
- `SmartDjango/models.py` data models (`Brand`, `Car`).
- `templates/` HTML templates.

## Working conventions
- Keep changes small and aligned with the existing Django structure.
- Preserve the current app flow unless a task explicitly changes behavior.
- Reuse the existing template and form patterns instead of introducing new frameworks.
- Follow the current naming and formatting style in the repo.

## Common commands
- Local run: `./run.sh`
- Install deps: `pip install -r requirements.txt`
- Django shell/manage commands: `python manage.py <command>`
- SQLite default; PostgreSQL target: `DJANGO_DATABASE='supabase' python manage.py <command>`

## Notes
- The app uses Crispy Forms with the Bootstrap 5 template pack.
- `run.sh` assumes a default admin user if env vars are not set.
- Use the existing fixtures/migrations workflow when changing models.
