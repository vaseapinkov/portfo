import csv

from flask import *

app = Flask(__name__)
print(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name + '.html')


def write_to_file(datas):
    with open('database.text', mode='a') as database:
        email = datas['email']
        subject = datas['subject']
        message = datas['message']
        file = database.write(f'Email:{email}\nSubject:{subject}\nMessage:{message}\n\n')


def write_to_csv(datas):
    with open('database.csv', mode='a') as database2:
        email = datas['email']
        subject = datas['subject']
        message = datas['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou')
        except:
            return 'not saved'
    else:
        return 'Error'
