import random


def battle():
  grass = "Bulbasaur"
  fire = "Charmander"
  water = "Squirtle"

  player_pokemon = ""
  cpu_pokemon = ""

  player_hp = 20.0
  player_attack = 0
  player_speed = 0

  cpu_hp = 20.0
  cpu_attack = 0
  cpu_speed = 0

  is_battle_over = False
  # Initialize variables for player's choice(input) and computer's choice
  player_starter = int(input("What do you choose? Type 1 for Bulbasaur, 2 for Charmander, or 3 for Squirtle.\n"))
  if player_starter == 1:
      player_pokemon = grass
      player_attack += 6.5
      player_speed += 4.5
      print(f"You chose {grass}!")
  elif player_starter == 2:
      player_pokemon = fire
      player_attack += 6.0
      player_speed += 6.5
      print(f"You chose {fire}!")
  elif player_starter == 3:
      player_pokemon = water
      player_attack += 5.0
      player_speed += 4.3
      print(f"You chose {water}!")
  else:
      print("Invalid option")

  cpu_starter = random.randint(1, 3)
  if cpu_starter == 1:
      cpu_pokemon = grass
      cpu_attack += 6.5
      cpu_speed += 4.5
      print(f"Your opponent chose {grass}!")
  elif cpu_starter == 2:
      cpu_pokemon = fire
      cpu_attack += 6.0
      cpu_speed += 6.5
      print(f"Your opponent sent out {fire}!")
  elif cpu_starter == 3:
      cpu_pokemon = water
      cpu_attack += 5.0
      cpu_speed += 4.3
      print(f"Your opponent sent out {water}!")

  # Ask player to attack or surrender
  # Calculate player and cpu health
  # If player starter speed is higher than CPU starter speed
  while not is_battle_over:
      battle_options = input("Do you want to attack or surrender? Press 'a' for attack or 's' for surrender.\n").lower()
      # Switched player_starter for player_pokemon
      if battle_options == "a" and (player_speed >= cpu_speed) and player_pokemon == "Bulbasaur":
          if cpu_pokemon == "Bulbasaur":
             cpu_hp -= (player_attack * 1)
             player_hp -= (cpu_attack * 1)
          elif cpu_pokemon == "Charmander":
              cpu_hp -= (player_attack * .5)
              player_hp -= (cpu_attack * 2)
          elif cpu_pokemon == "Squirtle":
              cpu_hp -= (player_attack * 2)
              player_hp -= (cpu_attack * .5)
      elif battle_options == "a" and (player_speed >= cpu_speed) and player_pokemon == "Charmander":
          if cpu_pokemon == "Bulbasaur":
              cpu_hp -= (player_attack * 2)
              player_hp -= (cpu_attack * .5)
          elif cpu_pokemon == "Charmander":
              cpu_hp -= (player_attack * 1)
              player_hp -= (cpu_attack * 1)
          elif cpu_pokemon == "Squirtle":
              cpu_hp -= (player_attack * .5)
              player_hp -= (cpu_attack * 2)
      elif battle_options == "a" and (player_speed >= cpu_speed) and player_pokemon == "Squirtle":
          if cpu_pokemon == "Bulbasaur":
              cpu_hp -= (player_attack * .5)
              player_hp -= (cpu_attack * 2)
          elif cpu_pokemon == "Charmander":
              cpu_hp -= (player_attack * 2)
              player_hp -= (cpu_attack * .5)
          elif cpu_pokemon == "Squirtle":
              cpu_hp -= (player_attack * 1)
              player_hp -= (cpu_attack * 1)
      # If CPU starter speed is higher than player starter speed
      elif battle_options == "a" and (cpu_speed > player_speed) and cpu_pokemon == "Bulbasaur":
          if player_pokemon == "Bulbasaur":
              player_hp -= (cpu_attack * 1)
              cpu_hp -= (player_attack * 1)
          elif player_pokemon == "Charmander":
              player_hp -= (cpu_attack * .5)
              cpu_hp -= (player_attack * 2)
          elif player_pokemon == "Squirtle":
              player_hp -= (cpu_attack * 2)
              cpu_hp -= (player_attack * .5)
      elif battle_options == "a" and (cpu_speed > player_speed) and cpu_pokemon == "Charmander":
          if player_pokemon == "Bulbasaur":
              player_hp -= (cpu_attack * 2)
              cpu_hp -= (player_attack * .5)
          elif player_pokemon == "Charmander":
              player_hp -= (cpu_attack * 1)
              cpu_hp -= (player_attack * 1)
          elif player_pokemon == "Squirtle":
              player_hp -= (cpu_attack * .5)
              cpu_hp -= (player_attack * 2)
      elif battle_options == "a" and (player_speed > cpu_speed) and cpu_pokemon == "Squirtle":
          if player_pokemon == "Bulbasaur":
              player_hp -= (cpu_attack * .5)
              cpu_hp -= (player_attack * 2)
          elif player_pokemon == "Charmander":
              player_hp -= (cpu_attack * 2)
              cpu_hp -= (player_attack * .5)
          elif player_pokemon == "Squirtle":
              player_hp -= (cpu_attack * 1)
              cpu_hp -= (player_attack * 1)
      elif battle_options == "s":
          is_battle_over = True
          print("CPU wins!")

      else:
          print("Not a valid input.")

      print(f"Your {player_pokemon}'s HP is {round(player_hp)}")
      print(f"CPU {cpu_pokemon}'s HP is {round(cpu_hp)}")

      if player_hp <= 0:
          is_battle_over = True
          print("CPU wins!")
      elif cpu_hp <= 0:
          is_battle_over = True
          print("You win!")

battle()