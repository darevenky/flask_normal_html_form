from flask import Flask,render_template,request

FI=Flask(__name__)

@FI.route('/form',methods=['POST','GET'])
def form():
    if request.method=='POST':
        form_data=request.form
        print(form_data)
        return form_data
    return render_template('form.html')



if __name__=='__main__':
    FI.run(debug=True)