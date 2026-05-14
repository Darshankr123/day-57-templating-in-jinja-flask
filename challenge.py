import requests
from flask import Flask, render_template
# from urllib3.contrib.emscripten import response
import random
from datetime import datetime as dt

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    year = dt.now().year
    return render_template("index.html",num=random_number,year=year)

@app.route("/guess/<string:name>")
def guess(name):
    genderRes = requests.get(f"https://api.genderize.io/?name={name}")
    gender = genderRes.json()["gender"]
    ageRes = requests.get(f"https://api.agify.io/?name={name}")
    age = ageRes.json()["age"]
    # print(f"age : {age}, gender : {gender}")
    print(gender)
    print(age)

    return render_template("index.html",name=name.title(),gender=gender,age=age)

@app.route("/blog/<int:num>")
def blog_posts(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog_post.html",posts=all_posts,num=num)


if __name__ == "__main__":
    app.run(debug=True,port=5001)