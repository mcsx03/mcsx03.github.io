rule TA577_HTML : Pikabot_DarkGate
{

    meta:
        author = "Josh_S"
        description = "Detects strings in html attachments used in recent Darkgate campaigns"
        creation_date  = "2024-03-28"
        samples        = "474bbc288e0a4c3de64865bf0055e80269b9c7861c1a22e3f81dfa512161657a, 6e72e76d60990669b323f976897820f4341d0bf8fe7744f69f71ca11a0b2226b, 97e67047e2dce5dfa176de708e4b345453ab734dd29ea7ad88799389e32bada2"

    strings:
        $header = {3c21444f43545950452068746d6c3e}  //<!DOCTYPE html>
        $String1 = {72657475726e20732e73706c6974282222292e7265766572736528292e6a6f696e282222293b} //return s.split("").reverse().join("");
        $String2 = {616c6572742822536f6d657468696e672077656e742077726f6e672122293b} //alert("Something went wrong!");

    condition:
        $header at 0 and $String1 and $String2
}