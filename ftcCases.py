from flask import Flask, send_from_directory, render_template, request
# -*- coding: utf-8 -*-
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home2():


	if request.method == 'POST':
		newCase1 = [
	    {
	        'company name': request.form['companyName'],
	        'date': request.form['date'],
	        'act violated': request.form['actViolated'],
	        'categoryPC': request.form['categoryPC'],
	        'summaryPC': request.form['summaryPC'],
	        'redressObtained': request.form['redressObtained'],
	        'audit': request.form['audit'],
	        'prohibitions': request.form['prohibitions'],
	        'pressCoverage': request.form['pressCoverage']

	    }
		]
		# cases.insert(newCase1)
	return send_from_directory('templates', 'index.html')

@app.route('/view')
def viewTable():

	caseFinder = json.load(open('static/json/ftc5-14.json'))
	tableData = []
	for x in caseFinder:
		newCase = [x['FIELD1'], x['FIELD2'],x['FIELD3'],x['FIELD4'],x['FIELD5'],x['FIELD6'],x['FIELD7'],x['FIELD8'],x['FIELD9'],x['FIELD10'],x['FIELD11'],x['FIELD12'],x['FIELD13'],x['FIELD14'],x['FIELD15'],x['FIELD16'],x['FIELD17'],x['FIELD18'],x['FIELD19'],x['FIELD20'],x['FIELD21'],x['FIELD22'],x['FIELD23'],x['FIELD24'],x['FIELD25'],x['FIELD26'],x['FIELD27'],x['FIELD28'],x['FIELD29']]
		tableData.append(newCase)
	return render_template('view.html', tableData = tableData)


if __name__ == '__main__':
    app.run(debug = True)