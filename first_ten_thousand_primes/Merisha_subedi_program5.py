data = [] #empty list to store all the numbers after preprocessing the data

with open('first_ten_thousand_primes.txt') as file: # read the file
    lines = file.readlines()

    for i in lines:
        i = i.split()
        
        for x in i:
            data.append(x) # append all the splitted contents in data

data= data[15:len(data)-1] # remove the first few lines before the actual prime numbers and the end value

#initialize the counts of each range to 0
dict_primes = {'0 - 9999': 0 , '10000 - 19999': 0, '20000 - 29999':0, '30000 - 39999': 0, '40000 - 49999': 0, '50000 - 59999': 0, '60000 - 69999': 0, '70000 - 79999': 0, '80000 - 89999':0, '90000 - 99999': 0, '100000 - 109999': 0, 'others': 0}

# go over each item in data and check to see if they are in the ranges below
for item in data: 
    item = int(item)
    
    if item > 0 and item <=9999: 
        dict_primes['0 - 9999']+=1

    elif item >9999 and item <=19999: 
        dict_primes['10000 - 19999']+=1

    elif item >19999 and item <=29999: 
        dict_primes['20000 - 29999']+=1

    elif item >29999 and item <=39999: 
        dict_primes['30000 - 39999']+=1

    elif item >39999 and item <=49999: 
        dict_primes['40000 - 49999']+=1

    elif item >49999 and item <=59999: 
        dict_primes['50000 - 59999']+=1

    elif item >59999 and item <=69999: 
        dict_primes['60000 - 69999']+=1

    elif item >69999 and item <=79999: 
        dict_primes['70000 - 79999']+=1

    elif item >79999 and item <=89999: 
        dict_primes['80000 - 89999']+=1

    elif item >89999 and item <=99999: 
        dict_primes['90000 - 99999']+=1

    elif item >99999 and item <=109999: 
        dict_primes['100000 - 109999']+=1

    else: 
        dict_primes['others']+=1


import operator
#print the output in console
print('The range with maximum prime numbers is : ' + str(max(dict_primes.items(), key=operator.itemgetter(1))[0]))

print('\n\n Distribution of primes: \n ===========================')

print('\nRange' + ' '* 17 + 'numbers')
print('\n====='+ ' '*17 + '=====')

for keys in dict_primes:
    print('\n'+ keys +' ' * (22-len(keys))+  str(dict_primes[keys]))


#write the output to the file
with open ('Merisha_subedi_program5.txt', 'w') as output:
    output.write('The range with maximum prime numbers is : ' + str(max(dict_primes.items(), key=operator.itemgetter(1))[0]))

    output.write('\n\n Distribution of primes: \n ===========================')

    output.write('\nRange\t\t\t\tnumbers')
    output.write('\n=====\t\t\t\t =====')

    for keys in dict_primes:
        output.write('\n'+ keys + ' ' * (22-len(keys))+  str(dict_primes[keys]))

      
    
        
        
        
        
        
        
        
        
        

        

    