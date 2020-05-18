# ~~~ Entry Point ~~~

def main():
  print("Initialize App!")

if __name__ == '__main__':
  main()
 
import calendar  ## Importing Module
y = int(input("Input the year : "))  ## Input for the Year
m = int(input("Input the month : ")) ## Input for the month
print(calendar.month(y, m)) ## Displaying the calender. Also, month() is a built-in function taking arguments as year and month
