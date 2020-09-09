# Encrypt Text :
<hr = "75%" >
<ul>
  <h2><a href = "https://github.com/Gowthaman1401/Python/blob/master/Encrypt/Encrypt.py">To Base64 :</a></h2>
<ul>
<li>To get help : <br>
<pre><code>python Encrypt.py --help
</code></pre>
<strong>Output</strong>:
<pre><code>

Usage:  [-c choice] [-t message] [-h help]

Options:
  -h,          --help              show this help message and exit
  -t MESSAGE,  --message=MESSAGE   Enter the message
  -c CHOICE,   --choice=CHOICE     Enter the choice(Encode/Decode)
</code></pre>
</li>
<li>To encode text <code>"Hello World"</code> to the base64:
<pre><code>python Encrypt.py -t "Hello World" -c e -p ...path...
</code></pre>
This will encode the text into base64 and save it as <code>Base64en.txt</code><br>
<strong>Output:</strong>
<pre><code>
[+] Message encoded
[+] Encoded/Decoded message saved in ...path.../Base64en.txt
</code></pre>

</li>
<li>To decode text <code>"Hello World"</code> from the base64:
<pre><code>python Encrypt.py -t "SGVsbG8gV29ybGQ=" -c d -p ...path...
</code></pre>
This will decode the base64 into text and save it as <code>Base64de.txt</code><br>
<strong>Output:</strong>
<pre><code>
[+] Message decoded
[+] Encoded/Decoded message saved in ...path.../Base64de.txt
</code></pre>
</ul></ul>
