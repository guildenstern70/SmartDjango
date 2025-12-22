if [ -z "${DJANGO_SUPERUSER_USERNAME}" ]; then
    export DJANGO_SUPERUSER_USERNAME='admin'
    export DJANGO_SUPERUSER_PASSWORD='admin'
    export DJANGO_SUPERUSER_EMAIL="admin@smartdjango.net"
fi
echo "resetting db..."
echo "using settings: $DJANGO_SETTINGS_MODULE"
rm db.sqlite3
rm -rf SmartDjango/migrations
rm -rf SmartDjango/__pycache__
python manage.py migrate
python manage.py createsuperuser --noinput
echo "make app migrations..."
python manage.py makemigrations SmartDjango
echo "migrate app..."
python manage.py migrate SmartDjango
python manage.py loaddata initial_data.yaml
python manage.py collectstatic --noinput