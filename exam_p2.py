def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    f = open('babynames'+'/'+ file_name)
    name_details = [line.strip('\n').split(',') for line in f]
    return name_details


def total_births(year, gender):
    """
    :param year: an integer, between 1880 and 2010
    :param gender: a string, "F" or "M"
    :return: an integer, the total births of all the babies in that year
    """
    births = 0

    for i in get_year_list(year):
        if gender == i[1]:
            births += int(i[2])
    return births

def get_year_list(year):
    year_string = str(year)
    return process_file('yob' + year_string + '.txt')

def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    for i in get_year_list(year):
        if i[0].lower() == name.lower() and i[1] == gender :
            return int(i[2]) / total_births(year, gender)


def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    proportionList = {}
    for year in range(1880, 2011):
        p = proportion(name, gender, year)
        if p:
            proportionList[str(year)] = p

    return max(proportionList, key=proportionList.get)


def main():
    print('My name had the highest proportion among females in the year:')
    print(highest_year('Defne', 'F'))

if __name__ == '__main__':
    main()
