#!/usr/bin/env python

def main():
  try:
      f=open('testfile', 'w')
      f.write("Write a test line")
  except TypeError:
      print("There was a type error!")
  except OSError:
      print ("Hey you have an OS Error")
  finally:
      print("I always run")
          
  
if __name__== "__main__":
  main()
