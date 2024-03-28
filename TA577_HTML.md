

<style>
img{
	border: 4px solid black;
}
</style>



TA577 has recently been switching between xls, xlsx, and html attachments. For this short write-up, I’m going to focus on the html attachments. 
<img src="Screenshots/Pasted image 20240328134148.png">

Upon a quick glance, it appears they are using base64 encoding and then reversing the string. 
<img>
![[Screenshots/Pasted image 20240328134027.png]]

Using CyberChef we can easily decode this by reversing the string and use from base64. 
<img>
![[Screenshots/Pasted image 20240328134232.png]]

To further investigate, I utilized the two strings as search parameters on VirusTotal (*return s.split("").reverse().join("")* and *alert("Something went wrong!")*). 
<img>
![[Screenshots/Pasted image 20240328134648.png]]


Subsequently, I developed a Python script to extract all callouts from the identified samples. 

<img>![[Screenshots/Pasted image 20240328134817.png]]
This gave us two additional IPs to search for activity to.
<img>
![[Screenshots/Pasted image 20240328135243.png]]
From this information I created a Yara rule to detect/hunt for these html files.
<img>
![[Screenshots/Pasted image 20240328135705.png]]
