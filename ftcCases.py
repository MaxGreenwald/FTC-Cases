from flask import Flask, send_from_directory, render_template, request
#from flask.ext.pymongo import PyMongo
import pymongo

MONGODB_URI = 'mongodb://maxgreenwald:oliver11@ds061621.mongolab.com:61621/ftc-cases' 

# Database(MongoClient('mongodb://maxgreenwald:oliver11@ds061621.mongolab.com:61621/ftc-cases', 27017), u'test_database')
app = Flask(__name__)
# mongo = PyMongo(app)

# app.config['MONGO3_HOST'] = 'ds061621.mongolab.com:61621/ftc-cases'
#app.config['MONGO3_PORT'] = 27017
#app.config['MONGO3_DBNAME'] = 'ftc-cases'
#mongo3 = PyMongo(app, config_prefix='MONGO3')
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()
cases = db['cases']

@app.route('/')
def homepage():
	return send_from_directory('templates', 'realIndex.html')
@app.route('/newHomepage')
def home2():
	return send_from_directory('templates', 'index.html')

@app.route('/add', methods=['GET', 'POST'])
def addCase():
	if request.method == 'POST':
		print "hello"
		print request.form['case']
		newCase1 = [
	    {
	        'case': request.form['case'],
	        'date': request.form['date'],
	        'company name': request.form['companyName'],
	        'act violated': request.form['actViolated'],
	        'categoryPC': request.form['categoryPC'],
	        'summaryPC': request.form['summaryPC'],
	        'redressObtained': request.form['redressObtained'],
	        'financial': request.form['financial'],
	        'audit': request.form['audit'],
	        'prohibitions': request.form['prohibitions'],
	        'pressCoverage': request.form['pressCoverage']
	    }
		]
		cases.insert(newCase1)
	
	
		#print projectpath
	

	return send_from_directory('templates', 'add.html')
@app.route('/view')
def viewTable():

	caseFinder = cases.find()
	tableData = []
	for x in caseFinder:
		newCase = [x['case'], x['date'], x['company name'], x['act violated'], x['categoryPC'], x['summaryPC'], x['redressObtained'], x['financial'], x['audit'], x['prohibitions'], x['pressCoverage']]
		tableData.append(newCase)
	return render_template('view.html', tableData = tableData)


if __name__ == '__main__':
    app.run(debug = True)