
class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError()
    for player in players:
        if player[1] != 'R' and player[1] != 'S' and player[1] != 'P':
            raise NoSuchStrategyError()
    if (players[0][1] == 'R' and players[1][1] == 'S') or (players[0][1] == 'S' and players[1][1] == 'P') or (players[0][1] == 'P' and players[1][1] == 'R'):
        return players[0]
    elif players[0][1] == players[1][1]:
        return players[0]
    else:
        return players[1]

#print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
#print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
print(rps_game_winner([['player1', 'S'], ['player2', 'R']]) )
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))