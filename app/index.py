from flask import Flask, render_template
import dao

app = Flask("__name__")


cates = dao.ger_categories()


@app.route("/")
def index():
    return render_template('index.html', categories=cates)


if __name__ == "__main__":
    app.run(debug=True)