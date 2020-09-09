# <a href = "https://github.com/Gowthaman1401/Python/blob/master/PhoneInfo/PhoneInfo.py">Phonenumber Info :</a>
<hr = "75%" >
<ul>
<li>To run this :<br><code>pip3 install -r requirements.txt</code></li>
<li>To get help :<br><pre><code>python PhoneInfo.py --help
</code></pre>
<strong>Output</strong>:
<pre><code>

Usage:  [-p phonenumber] [-h help]

Options:
  -h,             --help             show this help message and exit
  -p PHONENUMBER, --phn=PHONENUMBER  Enter phonenumber with county code                     
</code></pre>
</li>
<li>To get info about phonenumber <code>"+40721234567"</code>:
<pre><code>python PhoneInfo.py -p "+40721234567"
</code></pre>
<strong>Output:</strong>
<pre><code>
['Vodafone', ('Europe/Bucharest',), 'Romania']
</code></pre>
</ul>
