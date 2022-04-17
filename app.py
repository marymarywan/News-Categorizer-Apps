from flask import Flask, request, render_template, redirect, url_for
import pickle

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    if request.method == 'POST':
        user = request.form["nm"]
        return redirect(url_for("model", article=user))
    else:
        return render_template('main.html')

@app.route("/<article>")
def model(article):
    model = pickle.load(open('model.pkl', 'rb'))
    cv = pickle.load(open('cv.pkl', 'rb'))
    text = [article]
    cv_text = cv.transform(text)
    yy = model.predict(cv_text)
    result = ""
    if yy == [0]:
        result = "opinion"
    elif yy == [1]:
        result = "world"
    elif yy == [2]:
        result = "Politics News"
    elif yy == [3]:
        result = "arts"
    elif yy == [4]:
        result = "business"
    elif yy == [5]:
        result = "sports"
    return render_template('main.html', output=result)

@app.route('/statistic')
def hello():
    return render_template('statics.html')

if __name__ == '__main__':
    app.run(debug=True)
