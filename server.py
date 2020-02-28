from flask import Flask,render_template,url_for,request, redirect
import csv
app = Flask(__name__)
#print(__name__)

#@app.route('/')
#def hello_world():
 #   #return 'Hello, Peter and yosief!'
  #  return render_template('index.html')

#@app.route('/<username>/<int:post_id>')
#def hello_world(username=None,post_id =None):
    #return 'Hello, Peter and yosief!'
  #  return render_template('index.html',name = username, post_id = post_id)

#@app.route('/blog')
#def blog():
 #   return 'This is realy cool to create blogs'

#@app.route('/blog/2020/cats')
#def blog2():
 #   return 'This is my cat'


@app.route('/')
def my_home():
    return render_template('index.html')

#@app.route('/about.html')
#def about():
   # #return 'Hello, Peter and yosief!'
   # return render_template('about.html')

#@app.route('/works.html')
#def work():
   # #return 'Hello, Peter and yosief!'
   # return render_template('works.html')

@app.route('/<string:page_name>')
def about(page_name):
    #return 'Hello, Peter and yosief!'
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode ='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n {email}, {subject}, {message} ')

def write_to_csv(data):
	with open('database.csv', newline='', mode ='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2,delimiter=',',quotechar='/', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
          data = request.form.to_dict()
          write_to_csv(data) # this tels in which function we will write
          return redirect('thankyou.html')
       except:
    	  return 'did not save to database'
    else:
       return 'somthing is wrong, try again'

