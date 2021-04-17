from website import create_app, db
from flask import render_template, request, redirect, url_for, flash
from website.models import Url
from utils import encode, decode

app = create_app()


@app.route("/")
def home():
	return render_template("home.html")


@app.route("/create",  methods=["GET", "POST"])
def create_url():
	if request.method == "POST":
		url = request.form.get('url')
		if url:
			new_url = Url(url=url, shortened_url="")
			db.session.add(new_url)
			db.session.commit()
			update_obj = Url.query.get(new_url.id)
			update_obj.shortened_url = encode(new_url.id)
			db.session.commit()
			flash("URL created!", category="success")
			return render_template("create_url.html", shortened_url = request.host_url + update_obj.shortened_url)
		else:
			flash("URL cannot be blank.", category="error")

	return render_template("create_url.html")


@app.route("/<path>")
def redirected(path):
	urlid = decode(path)
	url = Url.query.filter_by(id=urlid).first()
	return redirect(str(url.url))


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
