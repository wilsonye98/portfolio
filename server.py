from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def home():
	return render_template(f'index.html')

@app.route('/thankyou.html')
def thankyou():
	return render_template(f'thankyou.html')

@app.route('/<string:file_name>')
def get_file(file_name):
	return render_template(f'{file_name}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		# return redirect('/thankyou.html')
		return redirect('./thankyou.html')
	else:
		return 'Something went wrong'

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
	with open('database.csv', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])