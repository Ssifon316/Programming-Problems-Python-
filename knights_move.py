"""Problem #1: Knights Move on Keypad
   Given a numeric keypad, chooing successive digits as a knight moves in chess, determine how many
   different paths can be formed of lenght n."""

knight ={0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[3,9,0],5:[], 6:[1,7,0], 7:[2,6], 8:[1,3], 9:[2,4]}

def knights_move(n):
    current = [1]*len(knight)
    final_count =[0]*len(knight)
    for i in range(n-1):
        for key, val in knight.items():
            final_count[key] = sum(current[j] for j in val )
        current = list(final_count)
    return final_count
