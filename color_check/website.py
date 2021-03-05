from flask import Flask
from flask import render_template
from flask import request
import logging
from color_check.controllers.get_color_code import get_color_code
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title="Color Check")


@app.route('/color', methods=['POST'])
def show_color():
    # When the user submits the form at /, the contents of the form
    # will be send to this route, and whatever code you write here will
    # be run by your server. In order to render a new page for your user,
    # you will need to do a few things:
    # - extract the data submitted by the user
    # - check if the color exists in our list, return the hex code if it does
    # - render a new page which shows a square of that color and its name
    # - if the color doesn't exist, give the user a useful error message.
    # - create a log.txt file which records (logs) the user requests.
    color_name = request.form['color']
    color_hex_code = get_color_code(color_name)
    if color_hex_code == "error":
        error_message = "Sorry {} isn't a color in CSS."\
            .format(color_name)
        return render_template('color.html', page_title="Error",
                               your_color=error_message)
    else:
        your_color = "Your color {} is {} in hex code"\
            .format(color_name, color_hex_code)
        return render_template('color.html', page_title="Your Color",
                               your_color=your_color,
                               color_hex_code=color_hex_code)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
