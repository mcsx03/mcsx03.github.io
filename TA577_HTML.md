

<style>
img{
	border: 4px solid black;
}
</style>


TA577 has recently been switching between xls, xlsx, and html attachments. I decided to take a quick look at the html files.  
<img src="Screenshots/Pasted image 20240328134148.png">

I noticed they are using base64 encoding and then reversing the string to create the callout. 
<img src="Screenshots/Pasted image 20240328134027.png">

Using CyberChef I decode the string by reversing the string and using from base64. 
<img src="Screenshots/Pasted image 20240328134232.png">

To further investigate, I utilized the two strings as search parameters on VirusTotal (*return s.split("").reverse().join("")* and *alert("Something went wrong!")*). 
<img src="Screenshots/Pasted image 20240328134648.png">


To make this search useful, I create a Python script to extract all callouts from the identified samples. 
<img src="Screenshots/Pasted image 20240328134817.png">

This gave me two additional IPs to search for activity to.
<img src="Screenshots/Pasted image 20240328135243.png">

To wrap it up, I created a Yara rule based on my VT search. This will allows me to hunt/detect these files going forward.
<img src="Screenshots/Pasted image 20240328135705.png">


<a href="Scripts/TA577_HTML_VT">Link to Python script</a>
<br>
<a href="https://github.com/mcsx03/mcsx03.github.io/blob/main/Yara/TA577_HTML.yara">Link to Yara rule</a>
<br>
<a href="IOCs/2024_2_28_TA577_DarkGate">Link to IOCs</a>
<br>
