# python-crypter
FUD python crypter For anti virus evasion

This is a Python script that obfuscates Python code for protection. The script utilizes various obfuscation techniques to make the code more challenging to understand and analyze.

## Obfuscation Techniques Used

- **Base64 Encoding:** The code is first encoded using Base64 to obfuscate the original content.

- **Marshaling:** The obfuscated code is then marshaled, converting it into a binary format.

- **Module Parsing:** The script parses the input Python file to extract the module imports. The imported modules are included in the obfuscated code.

- **Random Junk Code Injection:** Random junk code is generated and injected into the obfuscated code. This includes creating random variables with random values, adding extra code to confuse readers.

## Each Crypting Algorithms
> Base64 Encoding: Base64 encoding is used to obfuscate the original code by converting it into a text format that consists of ASCII characters.

Zlib Compression: The zlib library is used to compress the obfuscated code, reducing its size and making it harder to analyze.

Marshal: The marshal module is used to serialize the obfuscated code into a binary format, making it more challenging to read and understand.

Fernet Encryption: The Fernet encryption algorithm, provided by the cryptography library, is used to encrypt the obfuscated code. Fernet uses symmetric key cryptography with AES-128 in CBC mode and HMAC using SHA256 for authentication.

## Usage

> python main.py


## Example
Let's say we have a Python file named example.py with the following content:

python
```
Copy code
import math

def square(x):
    return x ** 2

num = int(input("Enter a number: "))
result = square(num)
print("Square:", result)
Running the obfuscation script and providing example.py as input will generate the obfuscated code:
```
python
Copy code
```
import ast
import base64
import zlib
import marshal
from cryptography.fernet import Fernet
import random
from string import ascii_letters, digits
aPglzwU3ZY = 45
W5sU2AdB2y = 90
key = b'CXG5p8tBc7iDgVKl3b61eYiI5eOvSh_ZAeD1qMf35EA='
encrypted_data = b'eJzTNnEMBAEIRXLmf8sAEEfzR8gFlRDHCFwAAJUEVF0='
decryption_key = base64.b64decode(key)
cipher_suite = Fernet(decryption_key)
decrypted_data = cipher_suite.decrypt(encrypted_data)
decompressed_data = zlib.decompress(decrypted_data).decode()
exec(decompressed_data)
```
The obfuscated code includes random junk code, the imported module math, and the original code. The obfuscated code is saved as obfuscated_example.py.





Please note that while this script provides a level of obfuscation, it is not foolproof and may be possible to reverse engineer or understand the code with enough effort and analysis. its only for testing and education purpose. hope u be a nice security guy.


