from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/')
def home():
    regex = str(request.args.get('input_regex'))
    test_string = str(request.args.get('input_string'))
    count = 0
    matches_location = []
    print("count is this" , regex , test_string)
    if (regex and test_string) != "None":
        for match in re.finditer(regex, test_string):
            count += 1
            location = match.group(), "start index", match.start(), "End index", match.end()
            matches_location.append(location)
    return render_template('home.html', n=count, m = matches_location)


if __name__ == '__main__':
    app.run(debug=True)
