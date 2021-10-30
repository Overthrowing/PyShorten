from flask import render_template, request, redirect, flash

from utils import encode, decode
from website import create_app, db
from website.models import Url

app = create_app()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/create", methods=["GET", "POST"])
def create_url():
    if request.method == "POST":
        url = request.form.get('url')
        if url:
            new_url = Url(url=url, shortened_url="", times_visited=0)
            db.session.add(new_url)
            db.session.commit()
            update_obj = Url.query.get(new_url.id)
            update_obj.shortened_url = encode(new_url.id)
            db.session.commit()
            flash("URL created!", category="success")
            return render_template("create_url.html", shortened_url=request.host_url + update_obj.shortened_url)
        else:
            flash("URL cannot be blank.", category="error")

    return render_template("create_url.html")


@app.route("/<path>")
def redirected(path):
    if path != "favicon.ico":
        urlid = decode(path)
        url = Url.query.get(urlid)
        url.times_visited += 1
        db.session.commit()

        return redirect(str(url.url))
    else:
        return render_template("home.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
