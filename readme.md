## Simple flask template

__1. Create blog.py file:__

blog/blog.py
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Holla Planet!"
```

__2. Run a flask app (inside the blog dir)__ 

Unix Bash (Linux & MacOS):
```
$ export FLASK_APP=blog.py
$ export FLASK_ENV=development
$ flask run
```
Windows CMD:
```
> set FLASK_APP=blog.py
> set FLASK_ENV=development
> flask run
```
Windows PowerShell:
```
> $env:FLASK_APP = "blog.py"
> $env:FLASK_ENV = "development"
> flask run
```

In browser: 127.0.0.1:5000

![alt=text](pics/pic01.png)

__3. Sending some HTML__

blog/blog.py
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Super Blog</h1>"
```

__4.__

blog/blog.py
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> SUPER BLOG </h1>"\

@app.route("/kontakt/")
def contact():
    return "Tu sa vypise kontakt."
```

![alt=text](pics/pic02.png)


__5. Templates(šablóny)__

Create `templates` folder with `home.html` file

```
blog
├── blog.py
└── templates
    └── home.html
```

blog/templates/home.html
```html
<!doctype html>
<html lang="sk">
  <head>
    <title>Názov stránky</title>
  </head>
  <body>
    <h1>Super Blog</h1>
    <p>Obsah stránky</p>
  </body>
</html>
```

blog/blog.py
```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/kontakt/")
def contact():
    return "Tu sa vypíše kontakt"

```

![alt=text](pics/pic03.png)

__6. HTML template for /kontakt/__

blog/templates/contact.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Kontakt na mna</h1>
    <p>Meno: Juraj Klucka</p>
    <p>Mail: juraj.klucka@pycon.sk</p>
    <p>Telefon: 0903 000 000</p>
</body>
</html>
```

blog/blog.py
```python
@app.route("/kontakt/")
def contact():
    return render_template('contact.html')
```

__7. Links (odkazy)__

```html
<a href="https://pycon.sk">PyCon SK</a>
```

blog/templases/home.html
```html
  <body>
    <a href="https://pycon.sk">PyCon SK</a>
    <h1>Super Blog</h1>
    <p>Obsah stránky</p>
  </body>
```

__7. Links inside Flask__

Here we create link for contact.html
`
<a href="{{ url_for('contact') }}">Zobraziť kontakt</a>
`

blog/templates/home.html
```html
  <body>
    <a href="https://pycon.sk">PyCon SK</a>
    <a href="{{ url_for('contact') }}">Zobraziť kontakt</a>
    <h1>Super Blog</h1>
    <p>Obsah stránky</p>
  </body>
``` 

Link for home.html inside home.html

blog/templates/home.html
```html
  <body>
    <a href="https://pycon.sk">PyCon SK</a>
    <a href="{{ url_for('contact') }}">Zobraziť kontakt</a>
    <a href="{{ url_for('home') }}">Uvodna stranka</a>
    <h1>Super Blog</h1>
    <p>Obsah stránky</p>
  </body>
```
Create the same links for contact page.

blog/templates/contact.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <a href="https://pycon.sk">PyCon SK</a>
    <a href="{{ url_for('contact') }}">Zobraziť kontakt</a>
    <a href="{{ url_for('home') }}">Uvodna stranka</a>
    <h1>Kontakt na mna</h1>
    <p>Meno: Juraj Klucka</p>
    <p>Mail: juraj.klucka@pycon.sk</p>
    <p>Telefon: 0903 000 000</p>
</body>
</html>
```
Too much code duplication.

![alt=text](pics/pic04.png)


__8. Template inheritance (Base skeleton)__

blog/templates/base.html
```html
<!doctype html>
<html lang="sk">
  <head>
    <title>Názov stránky</title>
  </head>
  <body>
    <a href="https://pycon.sk">PyCon SK</a>
    <a href="{{ url_for('contact') }}">Zobraziť kontakt</a>
    <a href="{{ url_for('home') }}">Úvod</a>
    {% block content %}{% endblock %}
  </body>
</html>
```

blog/templates/home.html
```html
{% extends "base.html" %}

{% block content %}
  <h1>Super Blog</h1>
  <p>Obsah stránky</p>
{% endblock %}
```

blog/templates/contact.html
```html
{% extends "base.html" %}
    {% block content %}
    <h1>Kontakt na mna</h1>
    <p>Meno: Juraj Klucka</p>
    <p>Mail: juraj.klucka@pycon.sk</p>
    <p>Telefon: 0903 000 000</p>
{% endblock %}
```
__9. CSS styling__

blog/templates/base.html
```html
<!doctype html>
<html lang="sk">
  <head>
    <title>Názov stránky</title>
  </head>
  <body>
    <div style="background-color: yellow; margin-bottom: 100px;">
      <a href="https://pycon.sk">PyCon SK</a>
      <a href="{{ url_for('contact') }}">Zobraziť kontakt</a>
      <a href="{{ url_for('home') }}">Úvod</a>
    </div>
    {% block content %}{% endblock %}
  </body>
</html>
```
We create folder `static` with `style.css` file

```
blog
├── blog.py
├── static
│   └── style.css
└── templates
    └── index.html
```
blog/static/style.css
```css
.my-menu {
  background-color: lightblue;
  margin-bottom: 100px;
}
```

Add link to css file in `base.html` inside head tag

```
<link rel="stylesheet" type="text/css"
      href="{{ url_for('static', filename='style.css') }}">
```
and add my-menu class inside div with links.

blog/templates/base.html
```html
<!doctype html>
<html lang="sk">
  <head>
    <title>Názov stránky</title>
    <link rel="stylesheet" type="text/css"
          href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
    <div class="my-menu">
      <a href="https://pycon.sk">PyCon SK</a>
      <a href="{{ url_for('contact') }}">Zobraziť kontakt</a>
      <a href="{{ url_for('home') }}">Úvod</a>
    </div>
    {% block content %}{% endblock %}
  </body>
</html>
```

__9. Bootstrap__

