rule Stego: RandomStealers
{

    meta:
        author = "Josh_S"
        description = "<<BASE64_START>> and <<BASE64_END>> seen in recent campaigns leading to xworm, agenttesla, remcos and xloader"
        creation_date  = "2024-04-10"
        samples        = "028BC57D1F0094FF86B87F63BF6CC11F,e490b60c48a258ff91ced1d104cf748b"

    strings:
        $png = {89 50 4E 47 0D 0A 1A 0A}    //Header PNG
        $jpeg = {FF D8 FF E0 00 10 4A 46 49 46} //Header JFIF
        $StartBase = {3c 3c 42 41 53 45 36 34 5f 53 54 41 52 54 3e 3e 54 56 71} //<<BASE64_START>>TVq

    condition:
        ($png or $jpeg at 0 and $StartBase)
}
