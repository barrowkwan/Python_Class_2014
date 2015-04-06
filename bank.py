#
#  Bank Program
#
def withdraw():
    w_money = int(raw_input("How much money do you want to withdraw?"))
    global balance
    if balance < 0:
        print "that balance is not valid"
    elif balance > 0:
        my_book = open(bank_book,'w')
        my_book.write (str(balance - w_money))
        my_book.close()
        balance = balance - w_money

def deposit():
    print "This old machine is now depositing your money$$........"

def print_balance():
    print "Your current balance is : %d" % balance
