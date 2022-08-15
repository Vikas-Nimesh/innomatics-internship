import os
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pyshorteners as ps

app = Flask(__name__)


################# SQLAlchemy Configuration #################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

############################################################

####################### MODEL CLASS ########################

class URLS(db.Model):

    __tablename__ = 'urls'
    
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.Text)

    def __init__(self,url):
        self.url = url

    def __repr__(self):
        return "{}".format(self.url)

############################################################


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/url_shortner',methods = ['GET','POST'])
def url_shortner():
    if request.method == 'POST':
        url = request.form.get('box_input')

        url = ps.Shortener().tinyurl.short(url)

        new_url = URLS(url)
        db.session.add(new_url)
        db.session.commit()


    return render_template('url_shortner.html')


@app.route('/history')
def history():

    urls = URLS.query.all()
    return render_template('history.html',urls = urls)


if __name__ == '__main__':
    app.run(debug=True)