#importing numpy
import numpy as np 

#read the text file using numpy
words_ = np.genfromtxt('words_file.txt', dtype = str)

#convert the array into two dimensional array
words = np.reshape(words_, (300,1))
#words = np.expand_dims(words, axis=1)


# #############################################################

# # ## add the lowercase words into the array
lower = [w.lower() for w in words_]
lower = np.reshape(lower, (300,1))
#lower = np.expand_dims(lower, axis=1)

##############################################################

#add the dictioanry of characters into the array
single_dict = []
for word in words_:
    dict_list = {}

    #create a string of lowercase alphabets
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    #create a dictionary of alphabets as keys and initialize the values to zero
    for i in alphabets:
        dict_list[i]= 0
    for char in word:
        for alphabet in alphabets:
            if char.lower()==alphabet:
                dict_list[alphabet]+=1

                #create a single dictioanary to add as a column to the array
    single_dict.append(dict_list)

#add the dictionary to the array
single_dict = np.reshape(single_dict, (300,1))
#single_dict = np.expand_dims(single_dict, axis=1)

#############################################################

#add length of the words as a column in the array
leng = []
for word in words_:
    leng.append(len(word))
#print(leng)

leng = np.reshape(leng, (300,1))
#leng = np.expand_dims(leng, axis =1)

array = np.concatenate((words, lower, single_dict, leng), axis = 1)
#############################################################

#print the array
print(array)


##############################################################
#print the mean, sum, median and standard deviation of the lengths
mean_lengths = np.mean(array[:,3])
print('Mean of lengths= '+ str(np.round((mean_lengths),2)))

sum_lengths = np.sum(array[:,3])
print('sum of lengths = '+ str(sum_lengths))


median_lengths = np.median(array[:,3])
print('median of lengths = '+ str(np.round((median_lengths),1)))

sdv_lengths = np.std(array[:,3])
print('Standard deviation of lengths = '+ str(np.round((sdv_lengths), 2)))

###################################################################

#count the number of zeros and percentage of zeros using counter variable and print them

counter = 0
for dict_ in array[:,2]:
    for key, value in dict_.items():
        if value == 0:
            counter+=1

print('Total number of zeros = '+ str(counter))

percentage = (counter / (counter + sum_lengths))*100
print('percentage of zeros = ' + str(np.round((percentage),2)))