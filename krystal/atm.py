# Krystal Kwan
# 7/16/2016
# ATM Machine

import time
import sys

m = 0

def withdraw():
    global m
    try:
        print("Withdraw amount:")
        w = float(input("> "))
        if w > m:
          print("Not enough!")
        else:
          print("Withdrawing $%.2f..." % w)
          m -= w
          time.sleep(2)
          print("Done.")
    except ValueError:
        print("Invalid Input.")
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit(0)

def balance():
    global m
    print("Your current balance: $%.2f." % m)

def deposit():
        global m
        try:
            print("Deposit amount:")
            w = float(input("> "))
            if w <= 0:
              print("Invalid Input.")
            else:
              print("Depositing $%.2f..." % w)
              m += w
              time.sleep(2)
              print("Done.")
        except ValueError:
            print("Invalid Input.")
        except KeyboardInterrupt:
            print("Quitting...")
            sys.exit(0)

def decide(a):
    if a == 1:
        balance()
    elif a == 2:
        deposit()
    elif a == 3:
        withdraw()
    else:
        print("Invalid Input.")
try:
    print("Your Name:")
    n = input("> ")
    print("Your current balance:")
    b = float(input("> "))
    m = b
except ValueError:
    print("Input Invalid.")
except KeyboardInterrupt:
    print("Quitting...")



while True:
    try:
        print("%s, what do you want to do today? (type in 1, 2, or 3)" % n)
        print("\t1) Print Balance")
        print("\t2) Deposit")
        print("\t3) Withdraw")
        a = float(input("> "))
        decide(a)
    except ValueError:
        print("Input Invalid.")
    except KeyboardInterrupt:
        print("Quitting...")
        break
