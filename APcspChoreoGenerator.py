import random

PINK = '\033[95m'
GRAY = '\033[90m'
RESET = '\033[0m'
#(ANSI color code written by David Y. (2023) sentry.io)

print(GRAY + "Ballet Combo Choreographer" + RESET)
print(PINK + "⋆ ˚｡⋆୨♡୧⋆ ˚｡ \n"+ RESET)

moves = {
    'petit allegro': 
        [('Glissade',2),('Jeté',1),('Temps de cuisse',3),('Royale',1),('Souté',1),
         ('Changement',1),('Entrechecat',1),('Sous-su',1),('Ballotté',2),('Assemblé',1)],
    'adagio': 
        [('Developpé',4),('Enveloppé',4),('Fondu',2),('Pas de bourrée',3),('Promenade',8),
         ('Attitude',2),('Penché',4),('Rond de Jambe en l\'air',4),('Coupé',2),('Tendu',2)],
    'grand allegro': 
        [('Tombé, pas de bourrée',3),('Glissade',2),('Grande jeté',2),('Contretemp',1),('Assemblé',2),
         ('Pas de chat',2),('Saut de chat',2),('Tour jeté',2),('Chassé',3),('Itallian pas de chat',2)]
}


def choreograph(style, counts_per_measure, num_measures):
    combo = []
    
    for measure in range (1, num_measures+1): 
        combo.append(RESET + f"Measure {measure} ({counts_per_measure} counts):") 
        
        total_counts = 0
        while total_counts < counts_per_measure:
            valid_moves = []
            for i in moves[style]:
                if total_counts + i[1] <= counts_per_measure:
                    valid_moves.append(i)

                    
            if not valid_moves:
                if (counts_per_measure - total_counts == 1):
                    combo.append(GRAY + "  - Plié " + PINK + "(1 count)" + RESET) 
                break 
            
            move, move_counts = random.choice(valid_moves)
            if move_counts > 1:
                combo.append(GRAY + f"  - {move} " + PINK + f"({move_counts} counts)" + RESET)
            else:
                combo.append(GRAY + f"  - {move} " + PINK + f"({move_counts} count)" + RESET)
                
            total_counts += move_counts
            
    return "\n".join(combo)
    
    
def music(style):
    if style == "adagio":
        print ("Your choreography will be to " + PINK + "City of Stars " + 
                GRAY + "from the musical movie " + PINK + "La La Land!")
    elif style == "petit allegro":
        print ("Your choreography will be to " + PINK + "River Flows in You" + GRAY + " by" + PINK + " Yiruma!")
    else:
        print ("Your choreography will be to " + PINK + "Für Elise" + GRAY + " by " + PINK + "Beethoven!")
    
    
while True: 
    u_style = input(RESET + "Enter style (adagio, petit allegro, grand allegro): "+ PINK).strip().lower()
    if u_style in moves:
        break
    else:
        print(PINK + "invalid style" + RESET)
while True:
    try:
        u_counts_per_measure = int(input(RESET + "Enter a count structure (3 or 8): " + PINK).strip())
        if u_counts_per_measure in [3,8]:
            break
        else:
            print(PINK + "invalid structure" + RESET) 
    except ValueError:
        print(PINK + "please input numerical values" + RESET)
        continue
while True:
    try:
        u_num_measures = int(input(RESET + "Enter number of measures you would like: " + PINK).strip())
        break
    except ValueError:
        print(PINK + "please input numerical values" + RESET)
        continue

print(PINK + "\n━◦○◦━◦○◦━\n" + RESET)

print(choreograph(u_style, u_counts_per_measure, u_num_measures))
print(" ")

music(u_style)
