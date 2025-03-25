def correct_orders(ordering: list, results: dict):
    for i in range(len(ordering) - 1):
        team1 = ordering[i]
        team2 = ordering[i+1]
        if (team1, team2) in results and results[(team1, team2)] == 'lost':
            return False
    return True


def permutations(elements):
    # here is our base case
    if len(elements) <= 1:
        return [elements]

    all_permutations = []
    for i in range(len(elements)):
        current_element = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        # here we have recursion
        for permutation in permutations(remaining_elements):
            all_permutations.append([current_element] + permutation)

    return all_permutations


def find_correct_orders_sequence(teams: set, results: dict):
    team_list = list(teams)  # convert a set to list
    # all permutations of list of teams
    all_permutations = permutations(team_list)
    for perm in all_permutations:
        if correct_orders(perm, results):  # if it has a correct order return that
            return perm
    else:  # if not return None
        return None


# User input
def UserInput():
    team_count = int(input("Enter the number of teams: "))
    teams = set(range(1, team_count + 1))

    match_count = (team_count * (team_count - 1)) // 2

    match_results = {}
    print('The team names should be in numbers eg: 1= team1 , 2=team2 and so on ..')
    print()
    print('result should be shown as `win` `draw` or `lost`')
    print()
    print('all threre parameters should be provided seprated by space')
    print()
    for i in range(match_count):
        team1, team2, result = input(
            "Enter match details (team1 team2 result): ").split()
        match_results[(int(team1), int(team2))] = result

    valid_ordering = find_correct_orders_sequence(teams, match_results)
    if valid_ordering:
        print("A valid ordering exists:", valid_ordering)
    else:
        print("No valid ordering exists.")


# UserInput()
