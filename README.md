# pyGuessTheNumber

<h2>a guess-the-number game.</h2>
finished on the 16th Nov 2020<br>
made with Python3 <br>
executable made with <a href="http://www.pyinstaller.org/">pyinstaller</a>
<h1>Menu</h1>
<h3>type: </h3>
<ul>
<li><b>p:</b> [p]lay the game.</li>
<li><b>r:</b> read the game's [r]ule/help.</li>
<li><b>a:</b> read [a]bout page.</li>
<li><b>q:</b> to [q]uit.</li>
</ul>

<h1>Rules</h1>
<h3>to win: you have to correctly guess a randomly generated number.</h3>
<h3>different difficulty level gives you different ranges of numbers and tries:</h3>
<ol>
<li><b>easy:</b> number ranges from 1 to 10. you have 5 chances to guess the number.</li>
<li><b>medium:</b> number ranges from 1 to 100. you have 7 chances to guess the number.</li>
<li><b>hard:</b> number ranges from -500 to 500. you have 10 chances to guess the number.</li>
</ol>

<h3>Binary Search Algorithm</h3>
if you understand the concept of binary search algorithm, you can win this easy.<br>
the explanation that stuck with me was the one from of the "<a href="https://youtu.be/Tpl7k8IOT6E?t=3364">finding David</a>" part of
CS50 2020 Lecture 0.</br>
the basic idea is to target the number in the middle of the range.<br>
ie: if it's from 1-10, you should start with 5. see if it's a higher or lower number than the correct number, then you repeat the process until you win.

<h1>Screenshots</h1>
<h6>pyGuessTheNumber main screen</h6>
<img src="https://github.com/CaptKraken/pyGuessTheNumber/blob/master/img/pyGtN%20Main%20Screen.jpg?raw=true" width="75%"></img>
<h6>pyGuessTheNumber Play</h6>
<img src="https://github.com/CaptKraken/pyGuessTheNumber/blob/master/img/pyGtN%20play.jpg?raw=true" width="75%"></img>
<h6>pyGuessTheNumber Rules</h6>
<img src="https://github.com/CaptKraken/pyGuessTheNumber/blob/master/img/pyGtN%20Rules.jpg?raw=true" width="75%"></img>
