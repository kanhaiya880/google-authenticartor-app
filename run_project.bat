@echo off

echo ==============================
echo Activating virtual environment
echo ==============================

REM Change this if your venv folder name is different
call venv\Scripts\activate

echo ==============================
echo Installing requirements
echo ==============================

pip install -r requirements.txt

echo ==============================
echo Running migrations
echo ==============================

python manage.py makemigrations
python manage.py migrate

echo ==============================
echo Starting Django server
echo ==============================

python manage.py runserver 0.0.0.0:5500

pause