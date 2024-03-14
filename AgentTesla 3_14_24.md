An email is sent containing an attachment named "PO1876.xls".:
    ![[Pasted image 20240314122108.png]]

Opening the XLS file triggers a callout to download "everylovecantchangebecauseitsatrueloverwhichmakingeverythingmoregreatunder____newlovetointroducewithmyselfkiss.doc".:
    ![[Pasted image 20240314122211.png]]
    ![[Pasted image 20240314122300.png]]
The DOC file exploits CVE-2017-11882, utilizing eqnedt32.exe to download a JPEG file, which is actually a VBS script.:
    ![[Pasted image 20240314122342.png]]

After de-obfuscating a few layers we can see the VBS script uses PowerShell to download JPG files from uploaddeimagens[.]com. It then looks for the embedded base64'd executable between the <<BASE64_START>> and <<BASE65_END>>:
![[Pasted image 20240314122555.png]]
![[Pasted image 20240314123507.png]]
    ![[Pasted image 20240314122745.png]]
    
Looking at the has for both images, we can see they are the same file:
-![[Pasted image 20240314123058.png]]

 Using CyberChef to convert the exe from base64:
![[Pasted image 20240314123620.png]]

These files are not packed, simplifying the extraction of the command-and-control (C2) information.
![[Pasted image 20240314123836.png]]