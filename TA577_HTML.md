{% include sidebar.html %}


TA577 has recently been switching between xls, xlsx, and html attachments. I decided to take a quick look at the html files.
<a href="Screenshots/Pasted image 20240328134148.png"> 
<img src="Screenshots/Pasted image 20240328134148.png">
</a>

I noticed they are using base64 encoding and then reversing the string to create the callout. 
<a href="Screenshots/Pasted image 20240328134027.png"> 
<img src="Screenshots/Pasted image 20240328134027.png">
</a>

Using CyberChef I decode the string by reversing the string and using from base64.
<a href="Screenshots/Pasted image 20240328134232.png">  
<img src="Screenshots/Pasted image 20240328134232.png">
</a>

To further investigate, I utilized the two strings as search parameters on VirusTotal (*return s.split("").reverse().join("")* and *alert("Something went wrong!")*).
<a href="Screenshots/Pasted image 20240328134648.png">  
<img src="Screenshots/Pasted image 20240328134648.png">
</a>

To make this search useful, I create a Python script to extract all callouts from the identified samples.
<a href="Screenshots/Pasted image 20240328134817.png"> 
<img src="Screenshots/Pasted image 20240328134817.png">
</a>

This gave me two additional IPs to search for activity to.
<a href="Screenshots/Pasted image 20240328135243.png">
<img src="Screenshots/Pasted image 20240328135243.png">
</a>

To wrap it up, I created a Yara rule based on my VT search. This will allows me to hunt/detect these files going forward.
<a href="Screenshots/Pasted image 20240328135705.png">
<img src="Screenshots/Pasted image 20240328135705.png">
</a>

<a href="https://github.com/mcsx03/mcsx03.github.io/blob/main/Scripts/TA577_HTML_VT.py">Link to Python script</a>
<br>
<a href="https://github.com/mcsx03/mcsx03.github.io/blob/main/Yara/TA577_HTML.yara">Link to Yara rule</a>
<br>
<a href="https://github.com/mcsx03/mcsx03.github.io/blob/main/IOCs/2024_3_28_TA577_DarkGate">Link to IOCs</a>
<br>
