# 1 2 5 10 20 50 100 200 500
# 1250
# Farzana Shaikh
# 11:28 AM
# { 500: 2 , 200:1 , 50 :1}


def atm():
    notes = [1,2,5,10,20,50,100,200,500]
    amount = int(input("Enter the amount:"))
    withdraw = {}
    notes.sort(reverse=True)
    for note in notes:
            res = amount//note
            new_amount = amount - (res*note)
            print(res)
            if res!= 0:
                withdraw[note]=res
            amount =  new_amount
    print(withdraw)

if __name__ == "__main__":
    atm()