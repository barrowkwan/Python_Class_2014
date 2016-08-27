# Krystal Kwan
# 7/16/2016
# ATM Machine

import time
import sys



def withdraw(m):
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
            return m
    except ValueError:
        print("Invalid Input.")
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit(0)

def balance(m):
    print("Your current balance: $%.2f." % m)
    return m

def deposit(m):
    try:
        print("Deposit amount:")
        w = float(input("> "))
        if w <= 0:
            print("Invalid Input.")
        else:
            print("Depositing $%.2f..." % w)
            m = m + w
            time.sleep(2)
            print("Done.")
            return m
    except ValueError:
        print("Invalid Input.")
    except KeyboardInterrupt:
        print("Quitting...")
        sys.exit(0)

def decide(a, m):
    if a == 1:
        return balance(m)
    elif a == 2:
        return deposit(m)
    elif a == 3:
        return withdraw(m)
    else:
        print("Invalid Input.")

m = 0.0

while True:
    try:
        print("Your Name:")
        n = input("> ")
        print("Your current balance:")
        m = float(input("> "))
        break
    except ValueError:
        print("Input Invalid.")
    except KeyboardInterrupt:
        sys.exit(0)
    except NameError:
        print("Input Invalid.")
        continue

while True:
    try:
        print("%s, what do you want to do today? (type in 1, 2, or 3)" % n)
        print("\t1) Print Balance")
        print("\t2) Deposit")
        print("\t3) Withdraw")
        a = float(input("> "))
        m = decide(a, m)
    except ValueError:
        print("Input Invalid.")
    except KeyboardInterrupt:
        print("Quitting...")
        break
