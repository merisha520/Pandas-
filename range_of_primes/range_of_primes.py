#reading the primenumbers.txt file (Problem 2 : Part 1)
with open('primenumbers.txt') as file:
    #creating a list of numbers in the file (Problem 2 : Part 1 )
    primes = file.read().split()

    #creating a dictioanry of ranges and initializing the count to 0 (Problem 2: part 2)
    dict_nums = {'<=300': 0,'<=600': 0, '<1000':0}

    #comparing each number to the enbounds of the range and adding them to one of the ranges : 
    for nums in primes:
        if int(nums)<= 300:
            dict_nums['<=300']+=1

        elif int(nums) <=600 and int(nums) > 300:
            dict_nums['<=600']+=1

        else:
            dict_nums['<1000']+=1

    
    #creating a dictionary to store the sums of the numbers in each range (Problem 2: part 3)
    dict_sums= {'<=300':0, '<=600':0, '<1000':0}

    #creating count dictionary to store the number of primes in each range
    count = {'<=300':0, '<=600':0, '<1000':0}

    #creating average dictionary to store the averages in each range
    average = {'<=300':0, '<=600':0, '<1000':0}

#getting count and sums of each range to find the average
    for nums in primes:
        nums = int(nums)
        if nums<=300 :
            count['<=300']+=1
            dict_sums['<=300']+=nums

        elif nums >300 and nums<=600:
            count['<=600']+=1
            dict_sums['<=600']+=nums
        
        else:
            count['<1000']+=1
            dict_sums['<1000']+=nums

#storing the averages of each range in dictioanry average
    average['<=300']= round(dict_sums['<=300']/ count['<=300'], 2)
    average['<=600']= round(dict_sums['<=600']/ count['<=600'],2)
    average['<1000']= round(dict_sums['<1000']/ count['<1000'],2)


#printing to the console
    for keys in dict_nums.keys():
        print('Number of items in category {} = {} and average of numbers in this category is {}'.format(keys, dict_nums[keys],average[keys]))