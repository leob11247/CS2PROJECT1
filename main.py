from gui import *


def main():
    window = Tk()
    window.title('Voting Form Application')
    window.geometry('500x500')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()

'''
def vote_menu():
    print('-' * 20)
    print('Vote Menu')
    print('-' * 20)
    print('v: Vote\nx: Exit')
    user_input = input('Option: ').lower().strip()
    while user_input != 'x' and user_input != 'v':
        user_input = input('Option (v/x): ').lower().strip()
    return user_input


def canidate_menu():
    print('-' * 20)
    print('Candidate Menu')
    print('-' * 20)
    print('1. John')
    print('2. Jane')
    voter_choice = int(input('1/2: '))
    while voter_choice != 1 and voter_choice != 2:
        voter_choice = int(input('Choose 1 or 2: '))
    if voter_choice == 1:
        print('Voted for John')
        return voter_choice
    elif voter_choice == 2:
        print('Voted for Jane')
        return voter_choice


def main():
    John_votes = 0
    Jane_votes = 0
    response = vote_menu()
    while response != 'x':
        vote = canidate_menu()
        if vote == 1:
            John_votes += 1
        elif vote == 2:
            Jane_votes += 1
        response = vote_menu()

    print('The final results look like this:')
    print(f'John Votes: {John_votes}')
    print(f'Jane Votes: {Jane_votes}')


main()
'''