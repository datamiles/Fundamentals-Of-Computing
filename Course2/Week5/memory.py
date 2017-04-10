#for card_index in range(len(cards)):
#    card_pos = 50 * card_index
#    canvas.draw_text(str(cards[card_index]), card_pos, ....)
    

# implementation of card game - Memory

import simplegui
import random


#cardIndex = range(16)
#print cardIndex
#exposed = [False] * 16
#print exposed
#cards = []
indexClick = []
turns = 0
#exposed = [False] * 16
#cardIndex = range(16)
#print len(cards)
#print len(cardIndex)
#print len(exposed)
#print cards
#state = 0
# helper function to initialize globals

def new_game():
    global cards, state, exposed, indexClick, turns
    exposed = [False] * 16
    cards = range(8)
    list2 = range(8)
    cards.extend(list2)
    random.shuffle(cards)
    print cards
    indexClick = []
    turns = 0
    label.set_text('Turns = ' + str(turns))
        
    state = 0

def mouseclick(pos):
    #print 'click loc:' + str(pos)
    indexClicked = pos[0]//50
    print 'indexClicked : ' + str(indexClicked)

    global state, indexClick, turns
    
    if exposed[indexClicked] != True:
        if state == 0:
            state = 1
            print 'In state 1 card at index ' + str(indexClicked) + ' was clicked'
            exposed[indexClicked] = True
            indexClick.append(indexClicked)
        elif state == 1:
            state = 2
            print 'In state 2 card at index ' + str(indexClicked) + ' was clicked'
            exposed[indexClicked] = True
            indexClick.append(indexClicked)
            turns += 1
            label.set_text('Turns = ' + str(turns))
        else:
            print 'exposed ' + str(exposed)
            print 'indexClicked list in state 2 :' + str(indexClick)

            idx1 = indexClick[0]
            idx2 = indexClick[1]

            if cards[idx1] == cards[idx2]:
                print 'match found'
                indexClick = []
            elif cards[idx1] != cards[idx2]:
                print 'match not found'
                exposed[idx1] = False
                exposed[idx2] = False
                indexClick = []

            exposed[indexClicked] = True
            indexClick.append(indexClicked)

            state = 1
            print 'state of indexClick list is :' + str(indexClick)
    
    print 'state is ' +str(state)

    
def draw(canvas):
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        canvas.draw_line((card_pos+50, 0), (card_pos+50, 100), 1, 'White')
    
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        if exposed[card_index] == True:
            canvas.draw_text(str(cards[card_index]), (card_pos+10, 50), 50, 'Red')
            
            
        
        
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric    