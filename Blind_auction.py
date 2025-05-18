import art

print(art.logo1)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of the bid is {winner}, with a bid of ${highest_bid}.")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is the price? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
        print(bids)
    else:
        print("\n" * 20)
