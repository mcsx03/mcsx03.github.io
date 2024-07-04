{% include sidebar.html %}
Recently, I've noticed emails containing links, attachments, or both, leading to a combination of XWorm, AsyncRat, and Remcos. These threats use multiple layers of obfuscation, involving data mapping and the Early Bird technique. Below are some screenshots of my analysis process, a link to IOCs, and a script I created to decode some of the layers.


The starting point is an email containing a PDF attachment, alongside links to ZIP files.
<br>
<a href="Screenshots/XA1.png"> 
<img src="Screenshots/XA1.png">
</a>
<br>
PDF which contained the link.
<br>
<a href="Screenshots/XA2.png"> 
<img src="Screenshots/XA2.png">
</a>
<br>

Link Downlods ZIP file.
<br>
<a href="Screenshots/XA2_1.png"> 
<img src="Screenshots/XA2_1.png">
</a>
<br>

ZIP file contains URL file
<br>
<a href="Screenshots/XA4.png"> 
<img src="Screenshots/XA4.png">
</a>
<br>

Which then goes to a LNK file
<br>
<a href="Screenshots/XA5.png"> 
<img src="Screenshots/XA5.png">
</a>
<br>

Upon examining the site, several files stand out. Interestingly, multiple sites share identical file names and structures. This could lead to an fun hunt in the future.
<br>
<a href="Screenshots/XA6.png"> 
<img src="Screenshots/XA6.png">
</a>
<br>

LNK file pulls down new.bat.
<br>
<a href="Screenshots/XA6_.png"> 
<img src="Screenshots/XA6_.png">
</a>
<br>
Obfuscated batch file. 
<br>
<a href="Screenshots/XA7.png"> 
<img src="Screenshots/XA7.png">
</a>
<br>

I've encountered several instances of these threats, all following the same format, so I decided to create a Python script to handle them (link below). They use data mapping by setting a key string and then creating another string based on character positions within that key string.<br>
    - Download a PDF from their site (which does nothing significant).<br>
    - Download two ZIP files, extract their contents, and delete the ZIP files.<br>
    - Download startupppp.bat and place it in the startup menu.<br>
Each ZIP file contains a Python executable along with six Python scripts. The script runs the first six scripts: money.py, moment.py, update.py, upload.py, time.py, and kam.py.
<br>
<a href="Screenshots/XA8.png"> 
<img src="Screenshots/XA8.png">
</a>
<br>
Examining startuppppp.bat file, it has the same obfuscation as new.bat. Using the script again, we can see that startuppppp.bat is mostly just cleaning up and running the other six Python scripts: 1.py, 2.py, 3.py, 4.py, 5.py, and 6.py.
<br>
<a href="Screenshots/XA9.png"> 
<img src="Screenshots/XA9.png">
</a>
<br>
After inspecting the Python scripts, they are all nearly identical. Each script contains a Base64 string, a key, and a decryption function.
I modifed their code slighty to write the output to a file.
<br>
<a href="Screenshots/XA10_.png"> 
<img src="Screenshots/XA10_.png">
</a>
<br>

<a href="Screenshots/XA11.png"> 
<img src="Screenshots/XA11.png">
</a>
<br>
Looking at the output of several of these scripts, they all appear to be shellcode. After uploading them to VirusTotal, they all were flagged as Donut shellcode.
<br>
<a href="Screenshots/XA12.png"> 
<img src="Screenshots/XA12.png">
</a>
<br>
Once running, the threat actors did not try to hide much. They used the Early Bird APC technique to inject the shellcode into Notepad.exe.
<br>
<a href="Screenshots/XA10.png"> 
<img src="Screenshots/XA10.png">
</a>
<br>
<a href="Screenshots/XA13.png"> 
<img src="Screenshots/XA13.png">
</a>
<br>
Finally analyzing the injection of notepad.exe, it appeared to be XWorm and AsyncRat. This was later confirmed by Triage. <a href="https://tria.ge/240703-tlv6nsyele/behavioral2"> Hatching Triage Report </a>

<br>
<br>
<a href="https://github.com/mcsx03/mcsx03.github.io/blob/main/IOCs/2024_07_03_Xworm_AsyncRat">Link to IOCs.</a>
<br>
<a href="https://github.com/mcsx03/mcsx03.github.io/blob/main/Scripts/BatchDecode.py">Link to script.</a>
<br>
