import random


players = ["Kamari","Max","Braylen","Jeffery","Xavier"
           ,"Avery","Carl","Nahom","Ja'Den","Joaquin",
           "EJ","Marshawn","Isaiah","Kenlon","Kriss","Joseph",
           "Semaj","darren","Nishad","Kauri","Tay","Taqari","Jarmauri"]
 
def PickTeams(Players):
    random.shuffle(players)
    Team1 = players[:len(players) // 2]
    teamCaptain1 = Team1[random.randrange(0,13)]

    print("Team 1:")
    print("Team 1 Captain" + teamCaptain1)
    for player in Team1:
        print(player)
    
    team2 = players[len(players) // 2:]
    team2Captain = team2[random.randrange(0,13)]

    print("Team 2:")
    print("Team 2 Captain" + team2Captain)
    for player in team2:
        print(player)


PickTeams(players)


