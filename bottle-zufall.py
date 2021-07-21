from bottle import run, request, get
from random import randint

@get("/roll")
def roll():
    lower = int(request.query.lowerBound)
    upper = int(request.query.upperBound)

    if lower >= upper:
        return "Falsche Eingabe"

    title = request.query.title

    number = randint(lower, upper - 1)
    if not title:
        return str(number)

    return f"<b>{title}:</b> {number}"

run(debug=True, reloader=True)
