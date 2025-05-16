print('''    A        U        C        T        I        O        N

            / \      |    |      _____      _____    _ _ _    _   _
           / _ \     |    |     / ____|       |      / __ \  | \ | |
          / ___ \    |    |    | |            |     | |  | | |  \| |
         /_/   \_\   |____|    | |____        |     | |__| | | |\  |
                                \_____|       |      \____/  |_| \_|
''')

print("welcome to auction challenge")

def find_highest_bidder(bidding_dictionary):
  highest_bid=0
  winner=""
  #winner = max(bidding_dictionary, key=bidding_dictionary.get)
  #highest_bid = bidding_dictionary[winner]
  for bidder in bidding_dictionary:
    bid_amount=bidding_dictionary[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder

  print(f"the winner is {winner} with a bid of ${highest_bid}")

bids={}

continue_bidding=True
while continue_bidding:
  name=input("wHAT IS YOUR NAME?")
  bid=int(input("whats your bid?:$"))
  bids[name]=bid
  should_continue=input("is there another user who want to bid:type yes or no?").lower()
  if should_continue=="no":
    continue_bidding=False
    find_highest_bidder(bids)
  elif should_continue=="yes":
    print("\n"*20)




#also use max function max(fruits,key=fruits.get)ie  max(stats,key=stats.get)

