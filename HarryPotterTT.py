import random
import requests
import pyfiglet


def print_ascii_title(title):
    # Used pyfiglet to create ASCII art for the title
    ascii_title = pyfiglet.figlet_format(title, font="doom")
    print(ascii_title)


def print_character_card(character):
    # Function to display the character's information as a "card"
    card = f"""
    +-----------------------------+
    | Name: {character['name']:>21} |
    |-----------------------------|
    | Species: {character['species']:>18} |
    | Gender:  {character['gender']:>18} |
    | House:   {character['house']:>18} |
    | Ancestry:{character['ancestry']:>18} |
    |-----------------------------|
    | Power: {character['power']:>20} |
    | Intelligence: {character['intelligence']:>13} |
    | Loyalty: {character['loyalty']:>18} |
    +-----------------------------+
    """
    print(card)


def random_harry_potter_character():
    character_number = random.randint(0, 199)  # Limit to the first 200 characters
    url = 'https://hp-api.herokuapp.com/api/characters'
    response = requests.get(url)
    characters = response.json()
    character = characters[character_number]

    # Custom numerical stats
    power = random.randint(1, 100)
    intelligence = random.randint(1, 100)
    loyalty = random.randint(1, 100)

    return {
        'name': character.get('name', 'Unknown'),
        'species': character.get('species', 'Unknown'),
        'gender': character.get('gender', 'Unknown'),
        'house': character.get('house', 'Unknown'),
        'ancestry': character.get('ancestry', 'Unknown'),
        'power': power,  # Custom power stat
        'intelligence': intelligence,  # Custom intelligence stat
        'loyalty': loyalty  # Custom loyalty stat
    }


def get_valid_stat_choice():
    # Function to get a valid stat choice from the player
    valid_stats = ['power', 'intelligence', 'loyalty']
    while True:
        stat_choice = input('Which stat do you want to use? (power, intelligence, loyalty) ').lower()
        if stat_choice in valid_stats:
            return stat_choice
        else:
            print("Invalid choice. Please choose from 'power', 'intelligence', or 'loyalty'.")


def play_round():
    # Generate and display the player's character
    my_character = random_harry_potter_character()
    print("Your Character Card:")
    print_character_card(my_character)

    stat_choice = get_valid_stat_choice()

    # Generate and display the opponent's character
    opponent_character = random_harry_potter_character()
    print("Opponent's Character Card:")
    print_character_card(opponent_character)

    # Retrieve the selected stats
    my_stat = my_character[stat_choice]
    opponent_stat = opponent_character[stat_choice]

    # Compare the stats and personalize the responses
    if my_stat > opponent_stat:
        print(f"You Win! Your {stat_choice} of {my_stat} outmatched your opponent's {stat_choice} of {opponent_stat}!")
    elif my_stat < opponent_stat:
        print(
            f"You Lose! Your opponent's {stat_choice} of {opponent_stat} was too strong for your {stat_choice} of {my_stat}.")
    else:
        print(f"It's a Draw! Both you and your opponent have a {stat_choice} of {my_stat}.")


def ask_to_continue():
    # Function to ask the player if they want to continue playing
    while True:
        continue_game = input("Do you want to play another round? (yes/no) ").lower()
        if continue_game in ['yes', 'no']:
            return continue_game == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def run():
    print_ascii_title("Harry Potter" f"\n" "Top Trumps")  # Print game title in ASCII art

    while True:
        play_round()

        if not ask_to_continue():
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    run()
