from flask import Flask, render_template
from god_parser import get_god



app = Flask(__name__)


@app.route("/")
def main():
	return render_template("index.html")

@app.route("/facts")
def secondary():
	god, desc = get_god()
	return render_template("facts.html", god = god, desc = desc)


if __name__ == "__main__":
	app.run()
