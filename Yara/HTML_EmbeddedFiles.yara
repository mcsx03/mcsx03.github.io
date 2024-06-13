rule HTML_EmbeddedFiles: RandomStealers
{

    meta:
        author = "Josh_S"
        description = "Detects base64'd for MZ, PK, and LNK file stored in html files. This has been seen in email campaigns that have lead to AgentTesla, Lokibot, AsyncRat"
        creation_date  = "2024-06-12"
        samples        = "4AD876A177069C91AB6A33914527F09C, F997B38674254C2520D0ABC6B062BBD0, 3E045F1FA7E08692418B1A21673ED3EC, 4EE1052019ADEE452408411F6D816622, A8A92D4B136AE58B2D39213EFCDCDBF1"
    strings:
        $html = "<html>"
        $Filetype_PK = {22 55 45 73 44 42} //Base64 for PK  Zip header with added "
        $Filetype_VBS = {22 4a 79 42 45 5a} //Base64 ' D seen in VBS 
        $Filetype_MZ = {22 54 56 71} //Base64 for MZ header with added "
        $Filetype_LNK = {22 54 41 41 41 41 41}  //Base64 for LNK header
        $URLBlob = {77 69 6e 64 6f 77 2e 55 52 4c 2e 63 72 65 61 74 65 4f 62 6a 65 63 74 55 52 4c 28 62 6c 6f 62 29} //Base64 for window.URL.createObjectURL(blob)

    condition:
       $html and $URLBlob and any of ($Filetype_PK, $Filetype_VBS, $Filetype_MZ, $Filetype_LNK)
}
