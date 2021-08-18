# character

wizard = "Wizard"
elf = "Elf"
human = "Human"

# hitPower
wizard_hp = 70
elf_hp = 100
human_hp = 150

# damage
wizard_damage = 150
elf_damage = 100
human_damage = 20

# dragon
dragon_hp = 300
dragon_damage = 5

while True:
    print("1) wizard")
    print("2) elf")
    print("3) human")

    character = input("Choose your Character:")

    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    print("Unknown Character")
print("You chose", character, "with a hit power of",
      my_hp, "and damage power of", my_damage)

while True:
    dragon_damage = dragon_hp - my_damage
    print("The", character, "damaged the Dragon", dragon_damage, "points")
    if dragon_damage <= 0:
        print("The dragon lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print(character, "Has been eliminated be Dragon")
    if my_hp <= 0:
        print("YOu been killed")
        break
