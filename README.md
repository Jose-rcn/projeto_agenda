Iniciar o projeto django
```
python - m venv venv
. venv/bin/activate
pip install -r requirements.txt
django-admin startproject project .
python manage.py startapp contact
```

Configurar o Git
```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
```

Migrando a base de dados do django
```
python manage.py makemigrations
python manage.py migrate
```
Criando um superusuario
```
python manage.py createsuperuser
```