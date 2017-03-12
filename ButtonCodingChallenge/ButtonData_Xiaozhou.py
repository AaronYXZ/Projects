## The Challenge

'''
The solution is pretty intuitive. The probability of getting x black cards from n draws equals to the probability of getting x red cards from n draws, and one's return is the inverse of the other's. So these combinations cancel out each other and the expected value will always be zero. 

To prove this, I enumerate all the possible combinations of black and red cards from n draw, calculate each one's returns and possibility, the expected winnings would be the sum of every combination's return multiplied by its possibility. 

I used the comb function from scipy to help me calculate nCr(number of combinations choosing r out of n). I could write a function myself, the simplest way (not necessarily the most efficient) would be to define a recursive function, say fac(n) that computes the factorial of n, then nCr is given by fac(n)/(fac(n-r)*fac(r)).  
'''

from scipy.misc import comb

def CardGame(draws, total_black = 26, total_red = 26):
    total = total_black + total_red
    winnings = 0
    if draws > total:
        print('Invalid Input!\nDraws must be less or equal than 52.')
        return
    
    total_comb = comb(total, draws)    
    if draws > total_black:
        black = draws - total_black
        for b in range(black, total_black + 1):
            r = draws - b
            winnings += comb(total_black,b)*comb(total_red,r)*(b-r)
        winnings = winnings / total_comb
        return winnings
    else:
        for b in range(draws + 1):
            r = draws - b
            winnings += comb(total_black, b)*comb(total_red,r)*(b-r)
        winnings = winnings / total_comb
        return winnings


## Optional Portion

'''
Given X and Y, the current expected value of the game is the number of black cards (Y) minus the number of red cards (X-Y), i.e., 2Y - X. Whether to continue drawing cards depends on the number of black and red cards drawn. Intuitively, if we've drawn more black cards, then the possibility of getting a black card in the next draw is smaller than getting a red card. So if the current expected value is larger than zero, we shouldn't continue drawing, because the expected value won't get any larger. 

To prove this, my function will calculate the expected value of every draw we could make after we've drawn X cards and Y black cards. Then it chooses the maximum expected value and compares with the current expected value. If the former is larger than the latter, it would suggest continuing drawing and tell you how many draws you need to make to get the maximum expected value.
'''

def CardGame2(X, Y):
    if X > 52 or Y > 26 or Y > X:
        print("Invalid Input!")
        return 
    else:
        expected_value = Y - (X-Y)
        remaining = 52 - X
        remaining_black = 26 - Y
        remaining_red = 26 - (X-Y)
        dic = {}
        for i in range(1, remaining + 1):
            dic[i] = CardGame(i, remaining_black, remaining_red)
        max_draws = sorted(dic, key = lambda x:dic[x], reverse = True)[0]
        max_expected_value = dic[max_draws]
        return expected_value, max_draws, max_expected_value



## How to run this code:

'''
Please download the code and put it under the working directory. Open the command line and type "python ButtonData_Xiaozhou.py". 
Then, follow the instructions on the screen. First, enter an integer as draws, it will return the expected value for challenge 1. Then, for the optional portion, enter integers for X and Y, it will return the current expected value and whether or not you would continue drawing.

You may need Python 3.x. to run this code successfully.
'''


if __name__ == '__main__':
    try:    
        draws = int(input("Please enter an integer for draws: "))        
        expected_value = CardGame(draws)
        print("The expected_value is {} ".format(expected_value))
    except ValueError:
        print('Invalid Input!\nDraws must be an integer.')

    try:    
        X = int(input("Please enter an integer for X: ")) 
        Y = int(input("Please enter an integer for Y: "))         
        expected_value, max_draws, max_expected_value = CardGame2(X,Y)
        print("The expected_value is {} ".format(expected_value))
        if max_expected_value > expected_value:
            print("Continue drawing cards, max exptected value will be {}, obtained at the {}th draw".format(max_expected_value, max_draws))
        else:
            print("Don't continue drawing cards, max expected value already obtained.")
    except TypeError:
        pass
    except ValueError:     
        print('Invalid Input!\nX and Y must be integers.')

