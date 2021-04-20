# PyShorten
A URL shortener made with Flask

# Usage
Change the secret key in `__init__.py`

```
app.config["SECRET_KEY"] = "<Secret Key>"
```

Then run `main.py`

#How it works
* When you create a shortened URL a database object is created to store the URL and shortened URL.
* The shortend URL is created by base 62 encoding the primary key.
