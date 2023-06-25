from flask import Flask, render_template, request, send_file
import os
from cryptography.fernet import Fernet
import base64
import random
import base64
import marshal
import zlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        junksor = request.form.get('junksor')

        data = file.read().decode("utf-8")
        original_code = data

        obfuscated = base64.b64encode(base64.b32encode(zlib.compress(marshal.dumps(original_code.encode()))))[::-1]

        gotobase64 = base64.b64encode(obfuscated)
        gotobase64x2 = base64.b64encode(gotobase64)
        gotobase32 = base64.b32encode(gotobase64x2)
        gotobase64x3 = base64.b64encode(gotobase32)

        randomnum = random.randint(10, 500)
        randomnum2 = random.randint(10, 500)
        randomnum3 = random.randint(10, 500)
        randomnum4 = random.randint(10, 500)
        randomnum5 = random.randint(10, 500)

        def genjunk():
            return f"""
def saint{random.randint(99999, 9999999)}():
    if {random.randint(99999, 9999999)} == {random.randint(99999, 9999999)}:
        print({random.randint(99999, 9999999)})
        aaa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        print({random.randint(99999, 9999999)})
        bbb{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        aa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        z{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        zz{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        c{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        cc{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
    elif {random.randint(99999, 9999999)} == {random.randint(99999, 9999999)}:
        print({random.randint(99999, 9999999)})
        aaa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        print({random.randint(99999, 9999999)})
        bbb{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        aa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        x{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        xx{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        y{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        yy{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
    else:
        print({random.randint(99999, 9999999)})
        aaa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        print({random.randint(99999, 9999999)})
        bbb{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        aa{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        w{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        ww{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        r{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}
        rr{random.randint(99999, 9999999)} = {random.randint(99999, 9999999)}

saint{randomnum}()
saint{randomnum2}()
saint{randomnum3}()
saint{randomnum4}()
saint{randomnum5}()
        """

        if junksor == "Yes":
            obfuscated = genjunk() + obfuscated.decode("utf-8")

        filename = f"obfuscated_code_{random.randint(1000, 9999)}.py"
        with open(filename, 'w') as file:
            file.write(obfuscated)

        return render_template('index.html', obfuscated_code=obfuscated.decode("utf-8"), filename=filename)
    return render_template('index.html')

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
