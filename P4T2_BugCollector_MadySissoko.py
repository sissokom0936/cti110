# A brief description of the project
# April 1, 2020
# CTI-110 P4T2 - Bug Collector
# Mady Sissoko
#
#Initialiaze the accumlator.
total = 0

#Get the bugs collected for each day.
for day in range(1, 6):
    print("Enter the bugs collected on day", day)
    bugs = int(input())
    total += bugs

#Display the total bugs.
print("You collected a total of", total, "bugs.")
    
