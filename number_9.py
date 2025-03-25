# scientists parameter is a list of there element
# scientists[0]=scientist name
# scientists[1]=scientist date of birth
# scientists[2]=scientist date of death
def find_golden_timeLine(scientists: list):
    # time_line dict is to store the number  of scientists in each time line
    time_line = {}

    # Calculate the number of scientists in each time line with python dict logic
    for scientist in scientists:
        birth_year, death_year = scientist[1], scientist[2]
        for year in range(birth_year, death_year + 1):
            if year in time_line:  # if exists increment it by 1
                time_line[year] += 1
            else:  # if dose not exists : initialize it to 1
                time_line[year] = 1

    # since we are not allowd to use max() we impelent it to find the time line with the maximum number of scientists

    max_scientists = 0
    golden_timeline = []

    for time_line, count in time_line.items():
        if count > max_scientists:
            max_scientists = count
            golden_timeline = [time_line]
        elif count == max_scientists:
            golden_timeline.append(time_line)

    return golden_timeline


# User Input Section
def UserInput():
    number_of_scientists = int(input("Enter the number of scientists: "))
    scientists = []

    for i in range(number_of_scientists):
        name = input("Enter the name of the scientist: ")
        birth_year = int(input("Enter the birth year: "))
        death_year = int(input("Enter the death year: "))
        scientists.append((name, birth_year, death_year))

    # Find the golden period and the scientists in that period
    golden_periods = find_golden_timeLine(scientists)

    # Find the scientists in the golden Timelines
    scientists_in_golden_periods = []
    for scientist in scientists:
        name = scientist[0]
        birth_year = scientist[1]
        death_year = scientist[2]
        if birth_year <= golden_periods[0] <= death_year:
            scientists_in_golden_periods.append(name)

    # Print the results
    print("Golden Time lines are : ", golden_periods)
    print("Scientists in that periods are: ", scientists_in_golden_periods)


# UserInput()
