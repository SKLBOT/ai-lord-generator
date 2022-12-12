import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("SECRET_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        input = request.form["input"]

        
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_teammate_prompt(input),
            temperature=0.4,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )


def generate_teammate_prompt(person):
    return """Suggest a funny name for a person as if they were a noble person from the middle ages.
person: Sean
name: Sir Sean the Wanker
person: James
name: Lord James the Disappointment
person: Thomas
name: Viceroy Thomas the Lame
person: Ricky
name: King Ricky the Icky
person: {}
name:""".format(
        person.capitalize()
    )