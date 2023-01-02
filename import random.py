import random
suit_tuple=("spades","hearts","clubs","diamonds")
rank_tuple=("Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King")
ncards=8
def getcard(decklistin):
    thiscard=decklistin.pop()
    return thiscard
def shuffle(decklistin):
    decklistout=decklistin.copy()
    random.shuffle(decklistout)
    return decklistout
print("Welcome to Higher or Lower")
print("You have to chose whether the next card to be shown will be higher or lower than the current card")
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

startdecklist=[]
for suit in suit_tuple:
    for thisval,rank in enumerate(rank_tuple):
        carddict={'rank':rank,'suit':suit,'value':thisval+1}
        startdecklist.append(carddict)
score=50
# print(startdecklist)
while(True):
    print()
    gamedecklist=shuffle(startdecklist)
    currentcarddict=getcard(gamedecklist)
    currentcardrank=currentcarddict['rank']
    currentcardvalue=currentcarddict['value']
    currentcardsuit=currentcarddict['suit']
    print('Starting card is:', currentcardrank + ' of ' + currentcardsuit)
    print()
    
    for cardno in range(0,ncards):
        answer=input('Will the next card be higher or lower than the ' + 
                               currentcardrank + ' of ' + 
                               currentcardsuit + '?  (enter h or l): ')
        # answer=answer.casefold()
        nextcarddict=getcard(gamedecklist)
        nextcardrank=nextcarddict['rank']
        nextcardsuit=nextcarddict['suit']
        nextcardvalue=nextcarddict['value']
        print("Next card is:",nextcardrank+' of '+nextcardsuit)
        
        if answer == 'h':
            if nextcardvalue > currentcardvalue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15 
        
        elif answer == 'l':
            if nextcardvalue < currentcardvalue:
                score = score + 20
                print('You got it right, it was lower')

            else:
                score = score - 15
                print('Sorry, it was not lower') 
        print('Your score is:', score)
        print()
        currentcardrank = nextcardrank
        currentcardvalue = nextcardvalue
        currentcardsuit = nextcardsuit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')
        
        