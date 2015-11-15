import csv
from random import choice
with open('attendees.csv') as a:
    d = list(csv.DictReader(a))[1:]
    attendees = {x["Email Address"].lower(): x["First Name"]+" "+x["Last Name"] for x in d}
    
with open('raffle.csv') as f:
    d = list(csv.reader(f))
    prizes = {prize: [] for prize in d[0][2:]} 
    prize_list = d[0][2:]
    #print prizes
    for row in d[1:]:
        #total_tickets = sum(int(x) for x in row[2:])
        #if total_tickets<=10:
        total_tickets = 10
        prize_labels = zip(prize_list, [int(x) for x in row[2:]])
        for label, prize_number in prize_labels:
            for i in range(prize_number):
                if total_tickets >0: 
                    prizes[label].append(row[1].lower())
                    total_tickets = total_tickets-1
        
    #print prizes
    for prize in prize_list:
        print prize
        print "number of tickets", len(prizes[prize])
        print "number of people entered", len(set(prizes[prize]))
        times = int(raw_input("How many of this prize are being given out: "))
        if times<len(set(prizes[prize])): 
            print "too many times"
            times = len(set(prizes[prize]))
        print ""
        stop = True
        for time in range(times):
            winner = choice(prizes[prize])
            if winner in attendees:
                print attendees[winner]
            else:
                print winner
            if stop:
                wait = str(raw_input(""))
                if wait=="c": 
                    stop = False
            while winner in prizes[prize]:
                prizes[prize].remove(winner)
        print ""
                
        
        
                