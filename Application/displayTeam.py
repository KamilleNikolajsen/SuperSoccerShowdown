def display_team(team):
    print(f"Team name: {team.name}")
    print(f"Team players:")

    for player in team.players:
        if player.position == 'Goalie':
            print(f"Goalie: \nName: {player.name}, Height: {player.height}cm, Weight: {player.weight}kg")
        elif player.position == 'Defence':
            print(f"Defence: \nName: {player.name}, Height: {player.height}cm, Weight: {player.weight}kg")
        elif player.position == 'Offence':
            print(f"Offence: \nName: {player.name}, Height: {player.height}cm, Weight: {player.weight}kg")
        else:
            print(f"Name: {player.name}, Height: {player.height}cm, Weight: {player.weight}kg, "
                  f"Position: {player.position}")

    print("\n")
