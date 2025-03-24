def highest_bidder(bid_dictionary):
    highest_bidder_name=""
    highest_bid=0
    for bidder in bid_dictionary:
        bid_amount=bid_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            highest_bidder_name=bidder
    print(f"Highest bid is {bid_amount} from {highest_bidder_name}")

auction={}
continue_bid="True"
while continue_bid=="True":
    person=input("Enter name: ")
    bid=int(input("Enter bid: $"))
    auction[person]=bid
    another=input('Put another bid? Type "yes" for yes and "no" for no:' ).lower()
    if another=="yes":
        continue
    if another=="no":
        continue_bid="False"

highest_bidder(auction)
