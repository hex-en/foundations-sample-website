import logging
from flask import Flask
from flask import render_template
from flask import request
from color_check.controllers.get_color_code import get_color_code
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title="Color Check")


@app.route('/color', methods=['POST'])
def show_color():

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

    logging.basicConfig(filename='tmp/log.txt', filemode='w',
                        level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
    logging.debug(f'User request: {color_name}')


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
