{% include sidebar.html %}
Started seeing AgentTesla emails with HTML attachments. The HTML contains Base64-encoded VBE, which prompts a download when opened. The VBE has a Base64-encoded executable that delivers AgentTesla. These are interesting as they do not require a connection between the email and infection. The initial HTML file seems to be a template for delivering LNK files. Below are screenshots of the sample I analyzed.


Email
<br>
<a href="Screenshots/AT1.png"> 
<img src="Screenshots/AT1.png">
</a>
<br>
HTML File
<br>
<a href="Screenshots/AT2.png"> 
<img src="Screenshots/AT2.png">
</a>
<br>
Prompts to download VBE
<br>
<a href="Screenshots/AT3.png"> 
<img src="Screenshots/AT3.png">
</a>
<br>
VBE contains an obfuscated executable.
<br>
<a href="Screenshots/AT4.png"> 
<img src="Screenshots/AT4.png">
</a>
<br>
Obfuscation is a simple replacement of characters.
<br>
<a href="Screenshots/AT5.png"> 
<img src="Screenshots/AT5.png">
</a>
<br>
After doing the find/replace, we can see the TVq, which is the base64 for the MZ header.
<br>
<a href="Screenshots/AT6.png"> 
<img src="Screenshots/AT6.png">
</a>
<br><br>
<a href="Screenshots/AT7.png"> 
<img src="Screenshots/AT7.png">
</a>
<br>
After unpacking the EXE, we can see the config as well as the C2.
<br>
<a href="Screenshots/AT8.png"> 
<img src="Screenshots/AT8.png">
</a>
<br>
<a href="https://github.com/mcsx03/mcsx03.github.io/blob/main/IOCs/2024_06_12_AgentTesla_VBE">Link to IOCs</a>
<br>