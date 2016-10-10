"""CONTROL FLOW"""
#While loops are useful when the number of iterations is not well-defined
import random
hp = 10
lv = 1
xp = 0
atk = 3
df = 1
defeated = 0
print("You awaken trapped in the Dungeons of Farrell with no means of escape.")
print("Suddenly, ghastly monsters approach you from every angle.\nDefend yourself!\n\n")
while hp > 0 and lv < 5:
    #Get a monster
    mhp, matk, mdf = round(5+2*(.5+random.random())*defeated*.9), round(2+1*(.5+random.random())*defeated*.8), round((.5+random.random())*defeated*.4)
    #Start a fight, continue until one dies
    while hp > 0 and mhp > 0:
        print("Player  -- LV:{} XP:{}/{} HP:{} ATK:{} DEF:{}".format(lv,xp,5*lv,hp,atk,df))
        print("Monster -- HP:{} ATK:{} DEF:{}".format(mhp,matk,mdf))
        #Player hits monster
        dmg = round((atk-mdf)*(.5+random.random()))
        mhp -= dmg
        print("You strike the foul beast for {} damage!".format(dmg))
        #If monster still alive, it hits back
        if mhp > 0:
            dmg = round((matk-df)*(.5+random.random()))
            hp -= dmg
            print("The knave responds with brutish force, dealing {} damage!".format(dmg))
    #If player still alive, they won
    if hp > 0:
        defeated += 1
        xp += 1 + defeated
        print("You defeated the enemy!  Another step closer to salvation...")
        #Has player leveled up?
        if xp >= lv * 5:
            lv += 1
            atk += round(3 * (.5 + random.random()))
            df += round(1.5 * (.5 + random.random()))
            hp = 10 + (lv-1) * 5
            xp = 0
            print("LEVEL UP!!!")
    #Either start another fight, or end the game
    input("\n\nPress Enter to continue...\n\n")
        
#If we get here, the game is over.  Did the player win or lose?
if lv == 5:
    print("YOU HAVE ESCAPED THE FARRELL DUNGEONS.\nYour legend will be told for centuries to come.\n\nC O N G R A T U L A T I O N S!!!")
else:
    print("The Farrell Dungeons have claimed another victim. . . :(")
    
#%%
"""EXERCISES
Play the game a couple times.

After you understand what it's doing, try fiddling with the values above to 
make the game either easier or harder to win.  To make the games faster, you can
comment out the input() function on line 42 so you no longer have to press enter.

For a real challenge, try making the game more interactive.
For example, you could use input statements to accept input from the user
to choose between a couple different types of attacks.  Maybe one attack does more
consistent, but lower damage, while another has higher variability but also higher
damage potential
"""

#%%
#User input example:
done = False
while not done:
    userinput = input("Enter 1 for Diet Coke, 2 for Cherry Coke, or q to quit > ")
    if userinput == "1":
        print("One Diet Coke, coming right up!")
    elif userinput == "2":
        print("Cherry Coke it is, my good sir.")
    elif userinput == "q":
        print("Quitting...")
        done = True
    else:
        print("Invalid entry.  Please try again...")