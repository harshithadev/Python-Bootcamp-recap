# Project 28 : Blind Auction 

auction = {}
more = "y"
while(True):
    auction.update({input("What is your name : "):int(input("What is your bid : "))})
    more = input("Any more bidders ? (y/n) ")
    if more != 'y':
        break 
print(f'Congradulations {list(auction.keys())[list(auction.values()).index(max(auction.values()))][0]} you won the auction with a bid of ${max(auction.values())}!')
    