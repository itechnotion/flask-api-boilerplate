# flask-api-boilerplate

This boilerplate will help you to quick start API development using flask

```
mkdir flask-api-boilerplate
cd flask-api-boilerplate
python3 -m venv venv

pip install Flask
pip install flask-restplus
pip install flask_script

python app.py runserver
```

Config : https://pythonise.com/feed/flask/flask-configuration-files#config-basics

# Run app
```
export FLASK_APP=run.py
export FLASK_ENV=development

python3 manager.py run
```

#Folder Structure

manager.py - it manages app run and other commands
app.py= Load config based on ENV