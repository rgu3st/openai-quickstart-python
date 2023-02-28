import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_jedi_prompt(animal),
            temperature=0.6,
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


def generate_jedi_prompt(name_in):
    return f"""
    Suggest three options for changing the provided name that is similar to but the actual name of a jedi.
    Name: Ben Kendrick
    Jedi Name: Obi-wan Kendrobi
    Name: Ben Smith
    Jedi Name: Kylo Rien
    Name: Amelia Porter
    Jedi Name: Darth Potter
    Name: Mark Williams
    Jedi Name: Mace Windu
    Name:{name_in}
    Jedi Name:
    """