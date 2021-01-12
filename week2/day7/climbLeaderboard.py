def climbingLeaderboard(ranked, player):
    current_rank = 0
    players_rank = []
    previous_val = 2147483647
    notInserted = True
    
    for i in range(len(player)):
        current_rank = 0
        for j in range(len(ranked)):
            if(previous_val > ranked[j]):
                current_rank += 1   
            print(" "+ str(player[i])+ " with"+ str(ranked[j])+" r :" +str(current_rank))
            if player[i] > ranked[j]:
                ranked.insert(j,player[i])
                players_rank.append(current_rank+1)
                previous_val = ranked[j]
                notInserted = False
                break
            elif player[i] == ranked[j]:
                ranked.insert(j+1,player[i])
                players_rank.append(current_rank+1)
                previous_val = ranked[j]
                notInserted = False
                break        
        
            previous_val = ranked[j]

        if notInserted:
            ranked.insert(len(ranked),player[i])
            players_rank.append(current_rank+1)
        print(ranked)
            
    return players_rank
        
        

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10],[5, 25, 50, 120]))