from flask import Flask,render_template,request,redirect    
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/<string:x>")
def page(x):
    return render_template(x)

def save_file(data_set):
    with open('database.txt',"a") as my_file:
        email= data_set["email"]
        sub= data_set["subject"]
        msg= data_set["msg"]
        my_file.write(f"{email} {sub} {msg}")
        my_file.write("\n")

def save_csv(data_set):
    with open('database.csv',"a") as my_file2:
        email= data_set["email"]
        sub= data_set["subject"]
        msg= data_set["msg"]
        csv_write = csv.writer(my_file2,delimiter=',',newline='', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,sub,msg])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        save_csv(data)
        return redirect("/thankyou.html")
    else:
        return ("something went wrong")

    # return render_template(data=data)

app.run(debug=True)