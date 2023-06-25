import os
import random
import base64
import marshal
import zlib
from flask import Flask, render_template, request, send_file
from cryptography.fernet import Fernet
from colorama import Fore, init

init()
app = Flask(__name__)

def text():
    print(f"program started")

def genjunk():
    r1 = random.randint(0, 999)
    r2 = random.randint(0, 999)
    var_name = ''.join(random.choices(ascii_letters + digits, k=10))
    return f'{var_name} = {r1} * {r2}\n'

def junkgenerator(num):
    code = ''
    for _ in range(num):
        code += genjunk()
    return code

def fernet_encrypt(key, data):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data)
    return cipher_text

def encode_b64(data):
    return base64.b64encode(data.encode()).decode()

def decode_b64(data):
    return base64.b64decode(data.encode()).decode()

def compress(data):
    return zlib.compress(data.encode())

def decompress(data):
    return zlib.decompress(data)

def obfuscate_code(file_name, inject_junk):
    with open(file_name, 'r') as f:
        data = f.read()
    encoded_data = encode_b64(data)
    compressed_data = compress(encoded_data)
    encryption_key = Fernet.generate_key()
    encrypted_data = fernet_encrypt(encryption_key, compressed_data)
    r1 = random.randint(1, 999)
    r2 = random.randint(1, 999)
    r3 = random.randint(1, 999)

    if inject_junk.lower() == 'y':
        junk_code = junkgenerator(random.randint(10, 30))
        encrypted_data = f'{junk_code}{encrypted_data}'
    encrypted_data = base64.b64encode(encrypted_data)
    encrypted_data = marshal.dumps(encrypted_data)
    encrypted_data = zlib.compress(encrypted_data)

    stub_code = f'''
import base64
import zlib
import marshal
from cryptography.fernet import Fernet

key = "{encode_b64(encryption_key.decode())}"
encrypted_data = {compressed_data}

# Additional obfuscation
encrypted_data = zlib.decompress(encrypted_data)
encrypted_data = marshal.loads(encrypted_data)
encrypted_data = base64.b64decode(encrypted_data)

decryption_key = base64.b64decode(key)
cipher_suite = Fernet(decryption_key)
decrypted_data = cipher_suite.decrypt(encrypted_data)

decompressed_data = zlib.decompress(decrypted_data).decode()
exec(decompressed_data)
    '''
    with open('obfuscated_' + file_name, 'w') as f:
        f.write(stub_code)
    return 'obfuscated_' + file_name

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        inject_junk = request.form['inject_junk']
        file = request.files['file']
        file_name = file.filename
        file_path = os.path.join(app.root_path, file_name)
        file.save(file_path)
        obfuscated_file = obfuscate_code(file_path, inject_junk)
        return send_file(obfuscated_file, as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
