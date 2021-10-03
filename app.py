from flask import Flask
import time
import rest

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    result = ""

    animals = ["Hippo", "Rhino", "Lion", "Leopard", "Black Mamba", "Puff Adder", "Cape Cobra"]

    start = time.time()

    for animal1 in animals:
        for animal2 in animals:
            result += str(rest.findDegrees(animal1, animal2))
            result += "\n"

    end = time.time()
    result += "Took " + str(end - start) + " seconds"

    return 'Hello World! ' + result


if __name__ == '__main__':
    app.run()
