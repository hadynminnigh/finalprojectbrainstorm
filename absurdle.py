answers = {1 : "will", 2 : "fore", 3 : "caps"}
finalAnswerGuessed = False

# ----------------------------------------------------------------------------- EXAMPLES --------------------------------------------------------------------------------
'''
✓ > will -> X X X X, wilt -> X X X _, wink -> X X _ _, w--- -> X _ _ _, till -> _ X X X, 
X > call -> (blank)*, like -> (blank)*,

* this is because the guessed letters exist in the correct spots in 1 & 3, the game doesn't know how to choose one over the other yet
  this should happen for each guess like this
'''
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Guess a four letter word")  # prompts user to start

while finalAnswerGuessed is False:

    # allow user to make a guess until the final answer is guessed
    guess = str(input(""))

# -------------------------------------------------------------------------------- NONE ---------------------------------------------------------------------------------
# ------ NONE : none correct ------
# --------- wrong spaces ----------
    if guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        answer = ("_ _ _ _")
            # checking for matches in wrong spots for 1st letter
        if guess[0:1] == str(answers[1])[1:2] or guess[0:1] == str(answers[1])[2:3] or guess[0:1] == str(answers[1])[3:] or guess[0:1] == str(answers[2])[1:2] or guess[0:1] == str(answers[2])[2:3] or guess[0:1] == str(answers[2])[3:] or guess[0:1] == str(answers[3])[1:2] or guess[0:1] == str(answers[3])[2:3] or guess[0:1] == str(answers[3])[3:]:
            answer = ("O _ _ _")
            if guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
                answer = ("O O _ _")
                if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                    answer = ("O O O _")
                    if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                        answer = ("O O O O")
                    else:
                        pass
                elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                        answer = ("O O _ O")
                else:
                    pass
            elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("O _ O _")
            elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("O _ _ O")
    
            else:
                pass

            # checking for matches in wrong spots for 2nd letter
        elif guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
            if guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
                answer = ("_ O _ _")
                if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                    answer = ("_ O O _")
                    if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                        answer = ("_ O O O")
                    else:
                        pass
                else:
                    pass
            elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                    answer = ("_ O _ O")
            else:
                pass

            # checking for matches in wrong spots for 3rd letter
        elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
            if guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
                answer = ("_ _ O _")
                if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                    answer = ("_ _ O O")
                else:
                    pass
            else:
                pass

            # checking for matches in wrong spots for 3rd letter
        elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
            if guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
                answer = ("_ _ _ O")
            else:
                pass

        print(answer)
    
# ------------------------------------------------------------------------------ SINGLES --------------------------------------------------------------------------------
# ------ ANSWER ONE : 1 correct, no matches for others ------
    elif guess[0:1] == str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
            # checks if 1st matches
        answer = ("X _ _ _")

        if guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
            answer = ("X O _ _")
            if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("X O O _")
                if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                        answer = ("X O O O")
                else:
                    pass
            elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                        answer = ("X O _ O")
            else:
                pass
        elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
            answer = ("X _ O _")
            if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("X _ O O")
        elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
            answer = ("X _ _ O")

        print(answer)

    elif guess[0:1] != str(answers[1])[0:1] and guess[1:2] == str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
            # checks if 2nd matches
        answer = ("_ X _ _")

        if guess[0:1] == str(answers[1])[1:2] or guess[0:1] == str(answers[1])[2:3] or guess[0:1] == str(answers[1])[3:] or guess[0:1] == str(answers[2])[1:2] or guess[0:1] == str(answers[2])[2:3] or guess[0:1] == str(answers[2])[3:] or guess[0:1] == str(answers[3])[1:2] or guess[0:1] == str(answers[3])[2:3] or guess[0:1] == str(answers[3])[3:]:
            answer = ("O X _ _")
            if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("O X O _")
                if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                    answer = ("O X O O")
                else:
                    pass
            else:
                pass
        elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
            answer = ("_ X O _")
            if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("_ X O O")
            else:
                pass
        elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
            answer = ("_ X _ O")
        else: 
            pass

        print(answer)

    elif guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] == str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if 3rd matches
        answer = ("_ _ X _")
        
        if guess[0:1] == str(answers[1])[1:2] or guess[0:1] == str(answers[1])[2:3] or guess[0:1] == str(answers[1])[3:] or guess[0:1] == str(answers[2])[1:2] or guess[0:1] == str(answers[2])[2:3] or guess[0:1] == str(answers[2])[3:] or guess[0:1] == str(answers[3])[1:2] or guess[0:1] == str(answers[3])[2:3] or guess[0:1] == str(answers[3])[3:]:
            answer = ("O _ X _")
            if guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
                answer = ("O O X _")
                if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                    answer = ("O O X O")
                else:
                    pass
            elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("O _ X O")
            else:
                pass
        elif guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
            answer = ("_ O X _")
            if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("_ O X O")
            else:
                pass
        elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
            answer = ("_ _ X O")
        else:
            pass

        print(answer)

    elif guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] == str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
            # checks if 4th matches
        answer = ("_ _ _ X")

        if guess[0:1] == str(answers[1])[1:2] or guess[0:1] == str(answers[1])[2:3] or guess[0:1] == str(answers[1])[3:] or guess[0:1] == str(answers[2])[1:2] or guess[0:1] == str(answers[2])[2:3] or guess[0:1] == str(answers[2])[3:] or guess[0:1] == str(answers[3])[1:2] or guess[0:1] == str(answers[3])[2:3] or guess[0:1] == str(answers[3])[3:]:
            answer = ("O _ _ X")
            if guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
                answer = ("O O _ X")
                if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                    answer = ("O O O X")
                else:
                    pass
            elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("O _ O X")
            else:
                pass
        elif guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
            answer = ("_ O _ X")
            if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("_ O O X")
        elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
            answer = ("_ _ O X")
        else:
            pass

        print(answer)


# ------ ANSWER TWO : 1 correct, no matches for others ------
    elif guess[0:1] == str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if 1st matches
        answer = ("X _ _ _")

        if guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
            answer = ("X O _ _")
            if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("X O O _")
                if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                        answer = ("X O O O")
                else:
                    pass
            elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                        answer = ("X O _ O")
            else:
                pass
        elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
            answer = ("X _ O _")
            if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("X _ O O")
        elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
            answer = ("X _ _ O")

        print(answer)

    elif guess[0:1] != str(answers[2])[0:1] and guess[1:2] == str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if 2nd matches
        answer = ("_ X _ _")

        if guess[0:1] == str(answers[1])[1:2] or guess[0:1] == str(answers[1])[2:3] or guess[0:1] == str(answers[1])[3:] or guess[0:1] == str(answers[2])[1:2] or guess[0:1] == str(answers[2])[2:3] or guess[0:1] == str(answers[2])[3:] or guess[0:1] == str(answers[3])[1:2] or guess[0:1] == str(answers[3])[2:3] or guess[0:1] == str(answers[3])[3:]:
            answer = ("O X _ _")
            if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("O X O _")
                if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                    answer = ("O X O O")
                else:
                    pass
            else:
                pass
        elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
            answer = ("_ X O _")
            if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("_ X O O")
            else:
                pass
        elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
            answer = ("_ X _ O")
        else: 
            pass

        print(answer)

    elif guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] == str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if 3rd matches
        answer = ("_ _ X _")

        if guess[0:1] == str(answers[1])[1:2] or guess[0:1] == str(answers[1])[2:3] or guess[0:1] == str(answers[1])[3:] or guess[0:1] == str(answers[2])[1:2] or guess[0:1] == str(answers[2])[2:3] or guess[0:1] == str(answers[2])[3:] or guess[0:1] == str(answers[3])[1:2] or guess[0:1] == str(answers[3])[2:3] or guess[0:1] == str(answers[3])[3:]:
            answer = ("O _ X _")
            if guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
                answer = ("O O X _")
                if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                    answer = ("O O X O")
                else:
                    pass
            elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("O _ X O")
            else:
                pass
        elif guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
            answer = ("_ O X _")
            if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("_ O X O")
            else:
                pass
        elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
            answer = ("_ _ X O")
        else:
            pass

        print(answer)

    elif guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] == str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if 4th matches
        answer = ("_ _ _ X")

        if guess[0:1] == str(answers[1])[1:2] or guess[0:1] == str(answers[1])[2:3] or guess[0:1] == str(answers[1])[3:] or guess[0:1] == str(answers[2])[1:2] or guess[0:1] == str(answers[2])[2:3] or guess[0:1] == str(answers[2])[3:] or guess[0:1] == str(answers[3])[1:2] or guess[0:1] == str(answers[3])[2:3] or guess[0:1] == str(answers[3])[3:]:
            answer = ("O _ _ X")
            if guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
                answer = ("O O _ X")
                if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                    answer = ("O O O X")
                else:
                    pass
            elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("O _ O X")
            else:
                pass
        elif guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
            answer = ("_ O _ X")
            if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("_ O O X")
        elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
            answer = ("_ _ O X")
        else:
            pass
        
        print(answer)

# ------ ANSWER THREE : 1 correct, no matches for others ------
    elif guess[0:1] == str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks if 1st matches
        answer = ("X _ _ _")

        if guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
            answer = ("X O _ _")
            if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("X O O _")
                if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                        answer = ("X O O O")
                else:
                    pass
            elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                        answer = ("X O _ O")
            else:
                pass
        elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
            answer = ("X _ O _")
            if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("X _ O O")
        elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
            answer = ("X _ _ O")

        print(answer)

    elif guess[0:1] != str(answers[3])[0:1] and guess[1:2] == str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks if 2nd matches
        answer = ("_ X _ _")

        if guess[0:1] == str(answers[1])[1:2] or guess[0:1] == str(answers[1])[2:3] or guess[0:1] == str(answers[1])[3:] or guess[0:1] == str(answers[2])[1:2] or guess[0:1] == str(answers[2])[2:3] or guess[0:1] == str(answers[2])[3:] or guess[0:1] == str(answers[3])[1:2] or guess[0:1] == str(answers[3])[2:3] or guess[0:1] == str(answers[3])[3:]:
            answer = ("O X _ _")
            if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("O X O _")
                if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                    answer = ("O X O O")
                else:
                    pass
            else:
                pass
        elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
            answer = ("_ X O _")
            if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("_ X O O")
            else:
                pass
        elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
            answer = ("_ X _ O")
        else: 
            pass

        print(answer)

    elif guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] == str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks if 3rd matches
        answer = ("_ _ X _")

        if guess[0:1] == str(answers[1])[1:2] or guess[0:1] == str(answers[1])[2:3] or guess[0:1] == str(answers[1])[3:] or guess[0:1] == str(answers[2])[1:2] or guess[0:1] == str(answers[2])[2:3] or guess[0:1] == str(answers[2])[3:] or guess[0:1] == str(answers[3])[1:2] or guess[0:1] == str(answers[3])[2:3] or guess[0:1] == str(answers[3])[3:]:
            answer = ("O _ X _")
            if guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
                answer = ("O O X _")
                if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                    answer = ("O O X O")
                else:
                    pass
            elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("O _ X O")
            else:
                pass
        elif guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
            answer = ("_ O X _")
            if guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
                answer = ("_ O X O")
            else:
                pass
        elif guess[3:] == str(answers[1])[0:1] or guess[3:] == str(answers[1])[1:2] or guess[3:] == str(answers[1])[2:3] or guess[3:] == str(answers[2])[0:1] or guess[3:] == str(answers[2])[1:2] or guess[3:] == str(answers[2])[2:3] or guess[3:] == str(answers[3])[0:1] or guess[3:] == str(answers[3])[1:2] or guess[3:] == str(answers[3])[2:3]:
            answer = ("_ _ X O")
        else:
            pass

        print(answer)

    elif guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] == str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks if 4th matches
        answer = ("_ _ _ X")

        if guess[0:1] == str(answers[1])[1:2] or guess[0:1] == str(answers[1])[2:3] or guess[0:1] == str(answers[1])[3:] or guess[0:1] == str(answers[2])[1:2] or guess[0:1] == str(answers[2])[2:3] or guess[0:1] == str(answers[2])[3:] or guess[0:1] == str(answers[3])[1:2] or guess[0:1] == str(answers[3])[2:3] or guess[0:1] == str(answers[3])[3:]:
            answer = ("O _ _ X")
            if guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
                answer = ("O O _ X")
                if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                    answer = ("O O O X")
                else:
                    pass
            elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("O _ O X")
            else:
                pass
        elif guess[1:2] == str(answers[1])[0:1] or guess[1:2] == str(answers[1])[2:3] or guess[1:2] == str(answers[1])[3:] or guess[1:2] == str(answers[2])[0:1] or guess[1:2] == str(answers[2])[2:3] or guess[1:2] == str(answers[2])[3:] or guess[1:2] == str(answers[3])[0:1] or guess[1:2] == str(answers[3])[2:3] or guess[1:2] == str(answers[3])[3:]:
            answer = ("_ O _ X")
            if guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
                answer = ("_ O O X")
        elif guess[2:3] == str(answers[1])[0:1] or guess[2:3] == str(answers[1])[1:2] or guess[2:3] == str(answers[1])[3:] or guess[2:3] == str(answers[2])[0:1] or guess[2:3] == str(answers[2])[1:2] or guess[2:3] == str(answers[2])[3:] or guess[2:3] == str(answers[3])[0:1] or guess[2:3] == str(answers[3])[1:2] or guess[2:3] == str(answers[3])[3:]:
            answer = ("_ _ O X")
        else:
            pass

        print(answer)

# ------------------------------------------------------- ^ NEED TO CHECK FOR ONES WITH MULTIPLE SINGLE MATCHES ^ -------------------------------------------------------

# ------------------------------------------------------------------------------ DOUBLES --------------------------------------------------------------------------------
# ------ ANSWER ONE : 2 correct, no matches for others ------
    elif guess[0:1] == str(answers[1])[0:1] and guess[1:2] == str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if first 2 match and not last 2
        answer = ("X X _ _")
        print(answer)

    elif guess[0:1] == str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] == str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks 1st and 3rd letter for match
        answer = ("X _ X _")
        print(answer)

    elif guess[0:1] == str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] == str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks first and last for match
        answer = ("X _ _ X")
        print(answer)

    elif guess[0:1] != str(answers[1])[0:1] and guess[1:2] == str(answers[1])[1:2] and guess[2:3] == str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks middle two for match
        answer = ("_ X X _")
        print(answer)

    elif guess[0:1] != str(answers[1])[0:1] and guess[1:2] == str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] == str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks 2nd and 4th for match
        answer = ("_ X _ X")
        print(answer)

    elif guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] == str(answers[1])[2:3] and guess[3:] == str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if last 2 match and not first 2
        answer = ("_ _ X X")
        print(answer)

# ------ ANSWER TWO : 2 correct, no matches for others ------
    elif guess[0:1] == str(answers[2])[0:1] and guess[1:2] == str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if first 2 match and not last 2
        answer = ("X X _ _")
        print(answer)

    elif guess[0:1] == str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] == str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks 1st and 3rd letter for match
        answer = ("X _ X _")
        print(answer)

    elif guess[0:1] == str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] == str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks first and last for match
        answer = ("X _ _ X")
        print(answer)

    elif guess[0:1] != str(answers[2])[0:1] and guess[1:2] == str(answers[2])[1:2] and guess[2:3] == str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks middle two for match
        answer = ("_ X X _")
        print(answer)

    elif guess[0:1] != str(answers[2])[0:1] and guess[1:2] == str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] == str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks 2nd and 4th for match
        answer = ("_ X _ X")
        print(answer)

    elif guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] == str(answers[2])[2:3] and guess[3:] == str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if last 2 match and not first 2
        answer = ("_ _ X X")
        print(answer)

# ------ ANSWER THREE : 2 correct, no matches for others ------
    elif guess[0:1] == str(answers[3])[0:1] and guess[1:2] == str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks if first 2 match and not last 2
        answer = ("X X _ _")
        print(answer)

    elif guess[0:1] == str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] == str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks 1st and 3rd letter for match
        answer = ("X _ X _")
        print(answer)

    elif guess[0:1] == str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] == str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks first and last for match
        answer = ("X _ _ X")
        print(answer)

    elif guess[0:1] != str(answers[3])[0:1] and guess[1:2] == str(answers[3])[1:2] and guess[2:3] == str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks middle two for match
        answer = ("_ X X _")
        print(answer)

    elif guess[0:1] != str(answers[3])[0:1] and guess[1:2] == str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] == str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks 2nd and 4th for match
        answer = ("_ X _ X")
        print(answer)

    elif guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] == str(answers[3])[2:3] and guess[3:] == str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks if last 2 match and not first 2
        answer = ("_ _ X X")
        print(answer)

# ------------------------------------------------------- ^ NEED TO CHECK FOR ONES WITH MULTIPLE DOUBLE MATCHES ^ -------------------------------------------------------

# ------------------------------------------------------------------------------ TRIPLES --------------------------------------------------------------------------------
# ------ ANSWER ONE : 3 correct, no matches for others ------
    elif guess[0:1] == str(answers[1])[0:1] and guess[1:2] == str(answers[1])[1:2] and guess[2:3] == str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if first 3 match and not last one
        answer = ("X X X _")
        print(answer)

    elif guess[0:1] == str(answers[1])[0:1] and guess[1:2] == str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] == str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if first 2 and last letter match, letter 3 does not match
        answer = ("X X _ X")
        print(answer)

    elif guess[0:1] == str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] == str(answers[1])[2:3] and guess[3:] == str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # first and last two match, second letter does not
        answer = ("X _ X X")
        print(answer)

    elif guess[0:1] != str(answers[1])[0:1] and guess[1:2] == str(answers[1])[1:2] and guess[2:3] == str(answers[1])[2:3] and guess[3:] == str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # last 3 match, first does not
        answer = ("_ X X X")
        print(answer)

# ------ ANSWER TWO : 3 correct, no matches for others ------
    elif guess[0:1] == str(answers[2])[0:1] and guess[1:2] == str(answers[2])[1:2] and guess[2:3] == str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if first 3 match and not last one
        answer = ("X X X _")
        print(answer)

    elif guess[0:1] == str(answers[2])[0:1] and guess[1:2] == str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] == str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # checks if first 2 and last letter match, letter 3 does not match
        answer = ("X X _ X")
        print(answer)

    elif guess[0:1] == str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] == str(answers[2])[2:3] and guess[3:] == str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # first and last two match, second letter does not
        answer = ("X _ X X")
        print(answer)

    elif guess[0:1] != str(answers[2])[0:1] and guess[1:2] == str(answers[2])[1:2] and guess[2:3] == str(answers[2])[2:3] and guess[3:] == str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        # last 3 match, first does not
        answer = ("_ X X X")
        print(answer)

# ------ ANSWER THREE : 3 correct, no matches for others ------
    elif guess[0:1] == str(answers[3])[0:1] and guess[1:2] == str(answers[3])[1:2] and guess[2:3] == str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks if first 3 match and not last one
        answer = ("X X X _")
        print(answer)

    elif guess[0:1] == str(answers[3])[0:1] and guess[1:2] == str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] == str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # checks if first 2 and last letter match, letter 3 does not match
        answer = ("X X _ X")
        print(answer)

    elif guess[0:1] == str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] == str(answers[3])[2:3] and guess[3:] == str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # first and last two match, second letter does not
        answer = ("X _ X X")
        print(answer)

    elif guess[0:1] != str(answers[3])[0:1] and guess[1:2] == str(answers[3])[1:2] and guess[2:3] == str(answers[3])[2:3] and guess[3:] == str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        # last 3 match, first does not
        answer = ("_ X X X")
        print(answer)

# ------------------------------------------------------- ^ NEED TO CHECK FOR ONES WITH MULTIPLE TRIPLE MATCHES ^ -------------------------------------------------------

# -------------------------------------------------------------------------------- ALL ----------------------------------------------------------------------------------
# ------ ANSWER ONE : all correct, no matches for others ------
    elif guess[0:1] == str(answers[1])[0:1] and guess[1:2] == str(answers[1])[1:2] and guess[2:3] == str(answers[1])[2:3] and guess[3:] == str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        answer = ("X X X X")
        print(answer)
        finalAnswerGuessed is True

# ------ ANSWER TWO : all correct, no matches for others ------
    elif guess[0:1] == str(answers[2])[0:1] and guess[1:2] == str(answers[2])[1:2] and guess[2:3] == str(answers[2])[2:3] and guess[3:] == str(answers[2])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[3])[0:1] and guess[1:2] != str(answers[3])[1:2] and guess[2:3] != str(answers[3])[2:3] and guess[3:] != str(answers[3])[3:]:
        answer = ("X X X X")
        print(answer)
        finalAnswerGuessed is True

# ------ ANSWER THREE : all correct, no matches for others ------
    elif guess[0:1] == str(answers[3])[0:1] and guess[1:2] == str(answers[3])[1:2] and guess[2:3] == str(answers[3])[2:3] and guess[3:] == str(answers[3])[3:] and guess[0:1] != str(answers[1])[0:1] and guess[1:2] != str(answers[1])[1:2] and guess[2:3] != str(answers[1])[2:3] and guess[3:] != str(answers[1])[3:] and guess[0:1] != str(answers[2])[0:1] and guess[1:2] != str(answers[2])[1:2] and guess[2:3] != str(answers[2])[2:3] and guess[3:] != str(answers[2])[3:]:
        answer = ("X X X X")
        print(answer)
        finalAnswerGuessed == True
        break

    else:
        break