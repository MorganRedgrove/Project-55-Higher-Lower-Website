from flask import Flask
from random import randint

app = Flask(__name__)

def number_gen():
    return randint(0, 9)

random_number = number_gen()

@app.route("/")
def welcome():
    return "<h1>Guess a number between 0 and 9" \
           "<br>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<string:var1>")
def number_check(var1):
    global random_number
    guess = int(var1)
    if guess == random_number:
        return success()
    elif guess <= random_number:
        return low()
    elif guess >= random_number:
        return high()

def success():
    return "<h1 style='color:purple'>You guessed correctly! &#127881;</h1>"

def high():
    return "<h1 style='color:green'>You guessed too high</h1>"

def low():
    return "<h1 style='color:red'>You guessed too low</h1>"


if __name__ == "__main__":
    app.run(debug=True)