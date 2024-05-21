from super import Superhero

spider = Superhero("Spiderman", "Peter Parker", "Spider sense", "Green Goblin")

print(f"A wonderful and well-liked", spider.name,"," f"his secret identity is", spider.identity, f"his super power",spider.power,  f"Spider man Arch enemy is", spider.enemy)


superman = Superhero("Superman", "Clark Kent", "Heat vison", "Lex Lutor, and cryptonite ofc")
print(f"Our heros name is",superman.name, f"his secret identity is", superman.identity, f"one of his super power is",superman.power, f"Superman arch enemy is",superman.enemy)

flash = Superhero("Flash", "Barry Allen", "the speed of force", "reverse flash")
print(f"He is the fastest man alive",flash.name,"," f"Hes secret identity", flash.identity,"," f"the superpower of hes", flash.power, "," f"Flash arch enemy is", flash.enemy, "Eobard Thawne")

batman = Superhero("Batman", "Bruce Wayne" ,"intellect, fighting skills, and wealth.", "Joker")
print(f"",batman.name,"," f"Batman secret indentity",batman.identity, f"he is power is in his", batman.power, f"Batman arch enemy is ",batman.enemy)

# spider.transform()
# superman.transform()
# flash.transform()
# batman.transform()

spider.secret("Spider cave")
superman.secret("Crystal citadel")
flash.secret("idk")
batman.secret("Batcave")

