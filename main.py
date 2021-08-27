from flask import*
app=Flask(__name__)
@app.route("/add",methods=['POST','GET'])
def Add():
    if request.method=='POST':
        num1=int(request.form.get('nm'))
        num2=int(request.form.get('nt'))
        sum1=num1+num2
        return render_template("add.html",sum=sum1)
    else:
        return render_template('add.html')
if __name__=='__main__':
    app.run(debug=True)