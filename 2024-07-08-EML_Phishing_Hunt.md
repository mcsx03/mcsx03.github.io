{% include sidebar.html %}
A few days ago, we received several phishing emails with EML attachments that contained HTML files. This method isn't new to us, but needing a break from AgentTesla samples, I decided to investigate further. The HTML files utilized a straightforward Replace.Call command to decode the URL embedded within. Upon searching common strings on VirusTotal, it appears these files have been circulating since May 22, 2024. Below is a concise overview of my investigative process, along with a CyberChef recipe and a Python script used to extract the URL.

Initial Email with EML Attachment (companyname.eml)
<br>
<a href="Screenshots/PH1.png"> 
<img src="Screenshots/PH1.png">
</a>
<br>

EML Attachment with HTML File (companyname.html>)
<br>
<a href="Screenshots/PH2.png"> 
<img src="Screenshots/PH2.png">
</a>
<br>

Here is the snippet where it constructs the URL by replacing strings in "a43f4e7". For privacy reasons, I've replaced the email address with email@domain.com.
<br>
<a href="Screenshots/PH3.png"> 
<img src="Screenshots/PH3.png">
</a>
<br>

Since I enjoy using CyberChef, I found it fairly straightforward to recreate this process. The code involves finding and replacing two strings stored between "/" and "/", separated by "|", as shown in this example: "/(e386ac|f5014622)/". In CyberChef, I utilize the Register and a Regex operation to identify these two strings.
<br>
<a href="Screenshots/PH4.png"> 
<img src="Screenshots/PH4.png">
</a>
<br>

Next, I simply take the two variables and perform the find and replace operation.
<br>
<a href="Screenshots/PH5.png"> 
<img src="Screenshots/PH5.png">
</a>
<br>

Then it's just a straightforward extraction of the URL.
<br>
<a href="Screenshots/PH6.png"> 
<img src="Screenshots/PH6.png">
</a>
<br>

While that was fun, I decided to do some hunting on VirusTotal. Starting with the replace.call string, I ran a search and surprisingly found solid results when paired with the HTML tags provided. It's worth noting the extremely low VirusTotal scores for these findings.
<br>
<a href="Screenshots/PH7.png"> 
<img src="Screenshots/PH7.png">
</a>
<br>

I ran a few of these through the CyberChef recipe from earlier, which worked great. But there were still 85 samples on VirusTotal. I wanted to create a way to extract all the URLs, so I decided to mimic the CyberChef recipe with a Python script.
<br>
<a href="Screenshots/PH8.png"> 
<img src="Screenshots/PH8.png">
</a>
<br>

After removing duplicates, this returned 17 unique domains to block/detect.
<br>
<a href="Screenshots/PH9.png"> 
<img src="Screenshots/PH9.png">
</a>
<br>

<br>
<br>
<a href="https://github.com/mcsx03/mcsx03.github.io/blob/main/IOCs/2024_07_08_EML_Phihsing_Hunt">Link to IOCs.</a>
<br>
<a href="https://github.com/mcsx03/mcsx03.github.io/blob/main/Scripts/PhihsingDecode.py">Link to script.</a>
<br>



CyberChef Recipe:<br>
[
  { "op": "Register",
    "args": ["((?<=/\\()[^|]+(?=\\|))", false, false, false] },
  { "op": "Register",
    "args": ["(/\\([^|]+\\|)", true, false, false] },
  { "op": "Find / Replace",
    "args": [{ "option": "Regex", "string": "$R1" }, "", true, false, true, false] },
  { "op": "Find / Replace",
    "args": [{ "option": "Regex", "string": "$R3" }, "", true, false, true, false] },
  { "op": "Extract URLs",
    "args": [false, false, false] }
]