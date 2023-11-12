from player import Player
import requests

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()  # tämä tekee http pyynnön ja metodi json kutsu muuttaa tiedoston python rakenteeksi
    # responseen on  tallennettu lista dictionaryjä

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            players.append(player)

    # pelaajien järjestäminen pisteiden mukaan
    sorted_players = sorted(players, key=lambda player: player.points, reverse=True)

    print("Players from FIN:")

    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    main()
