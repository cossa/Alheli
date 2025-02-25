import csv 

def read_accidents(filename):
    accidents = {}
    with open(filename, mode = 'r', newline= '') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            
            year = row[0]
            fatalities = row[1]
            injuries = row[2]
            crashes = row[3]
            fatal_crashes = row[4]
            dafcf = row [5]
            fcicpu = row [6]
            fcies = row [7]
            fcwduti = row[8]
            fcifi = row[9]
            accidents[year] = [fatalities, injuries, crashes, fatal_crashes, dafcf, fcicpu, fcies, fcwduti, fcifi]
    return accidents

def display_info(year_info ):
    if year_info:
        print("Menu: ")
        print("1.year")
        print("2.fatalities") 
        print("3.injuries") 
        print("4.crashes")
        print("5.fatal_crashes") 
        print("6.dafcf")
        print("7.fcicpu") 
        print("8.fcies") 
        print("9.fcwdut") 
        print("10.fcifi") 
        
        choice = input("Enter your  choice: ")
        
        if choice =="1":
            print(f'year: {year_info[0]}')
        elif choice == "2":
            print(f"fatalities: {year_info[1]}")
        elif choice == "3":
            print(f"Injuries: {year_info[2]}")
        elif choice == "4":
            print(f"Crashes: {year_info[3]}")
        elif choice == "5":
            print(f"Fatal Crashes: {year_info[4]}")
        elif choice == "6":
            print(f"Distraction Affected Fatal Crashes: {year_info[5]}")
        elif choice == "7":
            print(f"Fatal Crashes involving Cell Phone Use: {year_info[6]}")
        elif choice == "8":
            print(f"Fatal Crashes involving Excessive Speed: {year_info[7]}")
        elif choice == "9":
            print(f"Fatal Crashes while Driving under the Influence: {year_info[8]}")
        elif choice == "10":
            print(f"Fatal Crashes involving Fatigue or Illness: {year_info[9]}")
        
        else: 
            print("invalid choice")
    else: 
        print("year not found")
def main():
    file_name = 'accident.csv'
    
    crashes = read_accidents(file_name) 
    year = input('Write the year: ')
    year_info = crashes.get(year)
    
    display_info(year_info)
        
main()