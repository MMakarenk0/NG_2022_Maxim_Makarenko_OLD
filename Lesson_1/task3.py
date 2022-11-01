
numSec=int(input("Enter the number of seconds: ")) #Input the number of seconds.

numDays=int(numSec/86400)   #Calculation of the number of days.
numSec%=86400 

numHours=int(numSec/3600)    #Calculation of the number of hours.
numSec%=3600

numMinutes=int(numSec/60)   #Calculation of the number of minutes.
numSec%=60

print(f"Number of days: {numDays}, hours: {numHours}, minutes: {numMinutes}, seconds: {numSec}") #Output the result to the console.