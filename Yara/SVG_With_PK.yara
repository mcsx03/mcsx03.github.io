rule SVG_With_PK : RandomStealers
{

    meta:
        author = "Josh_S"
        description = "Detects base64'd for cab and zip file stored in svg files. This has been seen in email campaigns that have lead to Xworm and AgentTesla"
        creation_date  = "2024-03-07"
        samples        = "36a1ff08399ab52ecfcdf97c71a79a39 6b1572df46317b5ad159919242622052 75723051d38fd752f7b91c711162fe84 60723202dd540ad1255c9ad30fdd17b7 668ede7476144949ef4a1c2b36865dbd a0f0fe6606b632257aa4376a55c3bada"

    strings:
        $header = {3c73766720}    //<svg
        $PK = {5545734442} //Base64 for PK  Zip Header
        $Cab = {54564e445267} //Base64 for MSCF Cab Header
        $String1 = "window.URL.revokeObjectURL(url)"

    condition:
        ($header at 0
        and $String1
        and $PK
        or $Cab)
}
