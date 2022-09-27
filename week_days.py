
days = ['Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']


def day_of_week():
    # Let's start simple, and build up from there.
    # 1.1 TODO: Write a for loop that prints out each day in the `days` variable above.
    for day in days:
        print(day)
    # 1.2 TODO: Write another for loop that does the same thing, but this time use the range function
    for x in range(len(days)):
        print(days[x])


# '''
def favorite_activities():

    user_activities = []
    for y in range(len(days)):
        activity = input(f'what do you like to do on {days[y]}s? ')
        user_activities.append(activity)
#     # NOTE: Make sure to use an f-string so that the user knows which day they're being asked about.
    print(user_activities)

    for x in range(len(days)):
        print(
            f'On {days[x]}s, your favorite activity is to {user_activities[x]}.')
# favorite_activities()

def temp_by_day():

    for x in range(len(days)):
        current_temp = int(input('whats the temp?'))
        if current_temp < 50:
            print('Brr, put on a jacket!')
        elif current_temp >= 50 and current_temp <= 65:
            print('Cozy, grab a sweater')
        else:
            print('Put on some sunscreen!')


def temp_by_day_continuous():

    temp_outside = int(input('what is the temp outside? '))
    while temp_outside < 65:
        print('Wear a sweater')
        temp_outside = int(input('what is the temp outside? '))

    print('Spring has sprung!')
