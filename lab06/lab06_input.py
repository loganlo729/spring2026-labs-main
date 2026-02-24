import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from lab06 import generate_character
from lab06 import generate_monster
from lab06 import generate_encounter

description = input("Enter a description for your D&D character: ")
character = generate_character(description)
print(character.model_dump_json(indent=2))

description = input("Enter a concept for your D&D monster: ")
monster = generate_monster(description)
print(monster.model_dump_json(indent=2))

description = input("Enter a theme for your D&D encounter: ")
encounter = generate_encounter(party_level=5, num_monsters=3, theme=description)
print(encounter.model_dump_json(indent=2))