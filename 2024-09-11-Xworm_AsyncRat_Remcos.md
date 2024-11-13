We're seeing more campaigns delivering a combination of XWorm, AsyncRat, and now Remcos. The delivery methods remain mostly the same as before (link: 2024-07-03-Xworm-AsyncRat), but with a few notable changes. First, they've stopped using the PDF they had been reusing, which made it easier to track site creations, and instead, the new tactic is to open any PDF in the downloads folder. Additionally, they've started deploying RemcosRat as part of the mix. Here are some of the steps I took in analyzing a recent campaign.

Starting point, email containing link to kannadibank[.]com/Paymenteceipt[.]html which downloads a lnk file from trackingshipmentt[.]xyz@9394\DavWWWRoot\1B0S_YS63093BVSA_URDSGA.


Link file runs file new.bat.


Looking at trackingshipmentt[.]xyz@9394\DavWWWRoot, it's the same structure they've been using for a while now. 

I pulled the new.bat file, and luckily, the obfuscation hasn't changed. I used the script I wrote a while back to deobfuscate the file, and here's what we can see:

    Searches for and opens a PDF file in the downloads folder.
    Downloads DXJS.zip and FTSP.zip.
    Extracts the ZIP files to the downloads folder using PowerShell’s Expand-Archive command.
    Deletes the ZIP files.
    Navigates to and runs the extracted Python scripts located in Downloads\python\python312.
    Searches for another PDF file to open.
    Downloads a second batch file (startupppp.bat).
    Extracts FTSP.zip again and deletes the ZIP file.
    Changes the files to hidden and then removes the new.bat file.



I run the same script against startupppp.bat which shows it runs python scripts 1 - 7 located in downloads\print\python321 which were extracted above. It then does a little clean up.