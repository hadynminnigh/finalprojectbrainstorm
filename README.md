# Absurdle

Absurdle is variation of the game Wordle, coined by [qntm](https://qntm.org/absurdle).
I decided to create a version of Absurdle with 4-word guesses and answers.

Within this version:
**Correct** guesses in the **correct** spots are represented through "X" (usually they are represented by a green box)
**Correct** guesses in the **wrong** spots are represented through "O" (usually they are represented by a yellow box)
**Wrong** guesses are represented through "_" (usually they are represented by a grey box)
There is a limited set of answers: **will**, **fore**, and **caps**

## Video demonstrating my project:

[Click here](https://youtu.be/tgmudbpgq-E)

## Some issues I ran into:

> FIXED - for_ is not working (note: numbers in wrong spots)
> FIXED - matches in wrong spots not working, only showing correct guesses in correct spots (note: needs to be in ("_ _ _ _") check, otherwise it will just print as that)
> FIXED - O O O _ AND O O O O are broken (note: wrong postitions)

If a single letter in the wrong spot is used throughout the whole word, it will be detected for each when it shouldn't be
    *Ex: input "iiii" -> output "O X O O"*
         Note: this isn't an actual word, there isn't much I can do about this right now but there will be cases where a guess is displayed wrong because of this
    *Ex: input "bees" -> output "_ O O X"*
         Note: this is because of the "E" in "fore" and "S" in "caps"

## What I enjoyed:

I really enjoyed working through any issues I ran into, big or small. While my project hasn't made it to the best outcome, as outlined in my proposal, I have gotten farther than I expected. It isn't fully fleshed out yet, but I was happy I was easily able to figure out the portion represented by "O"s. The time that I've spent with this project makes me want to keep up with it, even after I have submitted it for this class, so I honestly will probably try to finish it over our winter break as a way to keep myself working with python.
