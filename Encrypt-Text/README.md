# Encrypt Text :
<hr = "75%" >
<ul>
  <h2><a href = "https://github.com/Gowthaman1401/Python/blob/master/Encrypt-Text/Base64.py">To Base64 :</a></h2>
<ul>
<li>To get help : <br>
<pre><code>python Base64.py --help
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
<pre><code>python Base64.py -t "Hello World" -c e -p ...path...
</code></pre>
This will encode the text into base64 and save it as <code>Base64_encoded.txt</code><br>
<strong>Output:</strong>
<pre><code>
[+] Message encoded
[+] Encoded/Decoded message saved in ...path.../Base64_encoded.txt
</code></pre>

</li>
<li>To decode text <code>"Hello World"</code> from the base64:
<pre><code>python Base64.py -t "SGVsbG8gV29ybGQ=" -c d -p ...path...
</code></pre>
This will decode the base64 into text and save it as <code>Base64_decoded.txt</code><br>
<strong>Output:</strong>
<pre><code>
[+] Message decoded
[+] Encoded/Decoded message saved in ...path.../Base64_decoded.txt
</code></pre>
</ul>

  <h2><a href = "https://github.com/Gowthaman1401/Python/blob/master/Encrypt-Text/Morse.py">To Morsecode :</a></h2>
<ul>
<li>To get help : <br>
<pre><code>python Morse.py --help
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
<li>To encode text <code>"HELLO WORLD"</code> to the morse code:
<pre><code>python Morse.py -m "HELLO WORLD" -c e -p ...path...
</code></pre>
This will encode the text into morse and save it as <code>Morse_encoded.txt</code><br>
<strong>Output:</strong>
<pre><code>
[+] Message encoded
[+] Encoded/Decoded message saved in ...path.../Morse_encoded.txt
</code></pre>

</li>
<li>To decode text <code>"HELLO WORLD"</code> from the morse code:
<pre><code>python Morse.py -m ".... . .-.. .-.. ---  .-- --- .-. .-.. -.." -c d -p ...path...
</code></pre>
This will decode the base64 into text and save it as <code>Morse_decoded.txt</code><br>
<strong>Output:</strong>
<pre><code>
[+] Message decoded
[+] Encoded/Decoded message saved in ...path.../Morse_decoded.txt
</code></pre>
</ul>

</ul>
