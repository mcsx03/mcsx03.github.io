<style>
img{
	border: 4px solid black;
}
</style>
I'm providing an update to my previous Latrodectus post. Here are additional pivot points I utilized and some searches that might be worth watching.

In my previous post, I mentioned pivoting on "-private-files/shared". However, after monitoring for more sites created with the same body hash, I observed a change from "files" to "fls":
<br>
<a href="Screenshots/LatVT1"> 
<img src="Screenshots/LatVT1.png">
</a>
<br>
When visiting some of these sites, I found another change in the security check site. Previously, they were using arrivingback[.]org/security_check/, a domain registered on 4/24/2024. They switched to using dimozti1[.]org/security_check, another domain also created on 4/24/2024:
<br>
<a href="Screenshots/LatVT2"> 
<img src="Screenshots/LatVT2.png">
</a>
<br>
<a href="Screenshots/LatVT2_1"> 
<img src="Screenshots/LatVT2_1.png">
</a>
<br>
<a href="Screenshots/LatVT2_2"> 
<img src="Screenshots/LatVT2_2.png">
</a>
<br>
<br>
I then noticed that both of these domains have been resolving to the same IP, 193[.]106[.]174[.]210. When examining this IP in VirusTotal, it appears to have a history of malicious activity:
<br>
<a href="Screenshots/LatVT3"> 
<img src="Screenshots/LatVT3.png">
</a>
<br>
While the previous findings were intriguing, I reached a point where progress seemed halted. Rather than broadening my search, it seemed that I narrowed it to one IP. I decided to look at both arrivingback[.]org/security_check/ and dimozti1[.]org/security_check using urlscan, hoping to uncover new leads. I found that both sites were redirecting to a PDF hosted on harvardlawreview[.]org:
<br>
<a href="Screenshots/LatVT4"> 
<img src="Screenshots/LatVT4.png">
</a>
<br>
<a href="Screenshots/LatVT4_1"> 
<img src="Screenshots/LatVT4_1.png">
</a>
<br>
<a href="Screenshots/LatVT4_2"> 
<img src="Screenshots/LatVT4_2.png">
</a>
<br>
<a href="Screenshots/LatVT4_3"> 
<img src="Screenshots/LatVT4_3.png">
</a>
<br>
Returning to VirusTotal, I conducted a search for URLs that redirected to the PDF hosted on harvardlawreview. The results returned some interesting URLs:
<br>
<a href="Screenshots/LatVT5"> 
<img src="Screenshots/LatVT5.png">
</a>
<br>
This seemed like the ending point, but out of curiosity, I decided to search for URLs redirecting to the PDF containing "/security_check/"-the pattern observed in the two previous URLs:
<br>
<a href="Screenshots/LatVT6"> 
<img src="Screenshots/LatVT6.png">
</a>
<br>
The search didn't yield an ton of results, but it did uncover one additional domain. Looking at the comments of the additional domain, it seems I'm on the right trail:
<br>
<a href="Screenshots/LatVT7"> 
<img src="Screenshots/LatVT7.png">
</a>
<br>



<U>Some VT searches that I'll continue to monitor</u>

<b>Relations to body hash, this will help monitor for changes to URLs:</b>
<br>
96296d63308cf90f44477f24d92a5b34bc6953d4710c66679e1255f2a8b4fcfc
<br><br>
<b>URLs that contain the same redirect and uri:</b>
<br>
entity:url redirects_to:"https://harvardlawreview.org/wp-content/uploads/2016/06/2289-2296-Online.pdf" url:/security_check/
<br><br>
<b>Samples using entry point "homq" which has been used on the previous samples:</b>
<br>
behaviour_processes: *dll, homq