from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)

@app.route('/sudh', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_sudh():
    if (request.method=='POST'):
        num0=request.json['num0']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = num0*num1*num2
        return jsonify(result)

@app.route('/sudh1', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_sudh1():
    if (request.method=='POST'):
        name=request.json['name']

        return jsonify(name + "ffsdfsfsf")

@app.route('/sudh2', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_sudh2():
    if (request.method=='POST'):
        name = request.json['name']
        eamil= request.json['mail']
        phonenumber = request.json['phone_number']

        return jsonify(name + eamil + str(phonenumber))


if __name__ == '__main__':
    app.run()
