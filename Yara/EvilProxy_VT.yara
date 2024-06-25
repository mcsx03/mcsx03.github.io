import "vt"

rule EvilProxy_Hunting {
meta:
  description = "EvilProxy_Hunting"
  author = "Stockton_J"
  target_entity = "domain"
condition:
  for any key, value in vt.net.domain.whois : (
    value == "f8d7755b176f3422s@ecs4kids.org" or value == "f9d15ebd4b78bd9bs@shelbyvilletn.org"
  )
}
