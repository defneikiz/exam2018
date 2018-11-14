def get_scores():
    dict = {}
    val = 1
    for i in range(26):
        dict[chr(97+i)] = val
        val += 1
    return dict

def get_name_list(file_name):
    
    '''load text file, get all the first names to the name_list'''
    
    with open(file_name,'r') as f:
        name_list = [line.rstrip('\n').split(' ')[0].lower() for line in f]
    f.close()
    return name_list

def get_words(file_name):
    ''' return a list of words'''
 
    with open(file_name,'r') as w:
        word_list = [line.rstrip('\n') for line in w]
    w.close()
    return word_list

def get_word_value(word):
    score_dict = get_scores()
    score = 0
    for i in word:
        if i in score_dict:
            score += score_dict[i]
    return score

def get_name_value(name_list):
    ''' return the value of given name'''
 
    name_values ={}
    for name in name_list:
        name_values [name] = get_word_value(name)

    return name_values
    
def who_has_highest_value(name_list):
    '''return the highest value of names'''
    points=[]
    for name in name_list:
        points.append (sum([ord(letter)-96 for letter in name]))

    individual_points = dict(zip(name_list,points))
    
    mvp = max(individual_points, key = individual_points.get)
    return mvp



def get_words_with_same_value(word_list,value):
    '''return a list of matched words'''
    word_list = get_words('positive-words.txt')
    same_value = []
    for word in word_list:
        if get_word_value(word) == value:
            same_value.append(word)
        return same_value
    



def main():

    name_list = get_name_list("roster.txt")
    word_list = get_words('words.txt')
    score_dict = get_scores()
    name_values = get_name_value(name_list)
    print ('The most valuable person in our class is:')
    print(who_has_highest_value(name_list))


    word_list = get_words('positive-words.txt')
    same_value = get_words_with_same_value(word_list , name_values ['defne'])
    print('Words with the same value as my name are: ')
    print(same_value)
if __name__ == '__main__':
    main()
    