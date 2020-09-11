# <a href = "https://github.com/Gowthaman1401/Python/blob/master/Youtube-Loader/YoutubeLoader.py">YoutubeLoader :</a>
<hr = "75%" >
<ul>
<li>To get help :<br><pre><code>python YoutubeLoader.py --help
</code></pre>
<strong>Output</strong>:
<pre><code>
Usage:  [-u url] [-c choice] [-h help]

Options:
  -h,        --help           show this help message and exit
  -m MENU,   --menu=MENU      Do you want to return to the Mainmenu(Y/N)?
  -u URL,    --url=URL        Url to youtube video (url should be in 'https://www.youtube.com/...' format)
  -c CHOICE, --choice=CHOICE  Enter your choice (1.DownloadVideo / 2.DownloadSubtitle(if available) / 3.WatchWithoutAds / 4.WatchAgeRestricted                
</code></pre>
</li>
<li>To get/watch Youtube video <code>"https://www.youtube.com/..."</code>:
<pre><code>python YoutubeLoader.py -u "https://www.youtube.com/..." -c 1
</code></pre>
<strong>Output:</strong>
<pre><code>
[-] You have to do it manually!
[+] Redirecting to default browser...
</code></pre>
</ul>
