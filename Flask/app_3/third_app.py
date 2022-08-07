from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def fun_1():
    if request.method == 'POST':
        email = request.form['input_email']
        return "Welcome {}".format(email)
    
    return render_template("form.html")

@app.route('/search', methods=['GET'])
def search_function():
    query = request.args['q']
    return "Search query entered = {}".format(query)
    

if __name__ == '__main__':

    app.run(debug=True)