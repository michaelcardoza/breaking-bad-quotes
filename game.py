import json
import requests

api_url_base = 'https://www.breakingbadapi.com/api'
headers = {'Content-Type': 'applications/json'}

figure_1 = '''
    ------
         |
         |
         |
         |
         |
       =====
'''
figure_2 = '''
    ------
    |    |
    O    |
         |
         |
         |
       =====
'''
figure_3 = '''
    ------
    |    |
    O    |
   /|\   |
         |
         |
       =====
'''
figure_4 = '''
    ------
    |    |
    O    |
   /|\   |
   / \   |
         |
       =====
'''


def get_quote_random():
    api_url = '{}/quote/random'.format(api_url_base)
    response = requests.get(api_url, headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))[0]
    else:
        return None


def who_said_it(author):
    answer = ''
    number_attemps = 1

    while answer != '' or answer != author.lower():
        answer = input('Who said it?: ').lower()

        if answer == author.lower():
            print('\n*****************')
            print('You Win!!! (^_^)')
            print('*****************')
            # print('Your answer is: {}'.format(answer))
            break

        if number_attemps == 4:
            wrong_anwser = 'You Lose!!! (-_-) | The answer was: {}'.format(author)

            print_figure(number_attemps)
            print('-' * len(wrong_anwser))
            print(wrong_anwser)
            print('-' * len(wrong_anwser))
            break
        else:
            print_figure(number_attemps)

        number_attemps += 1


def welcome(quote):
    quote = '* Quote: \'{}\' '.format(quote)
    print('*************************************************')
    print('Welcome to the game | Who said it? | Breaking Bad')
    print('************************************************* \n')

    print('-' * len(quote))
    print(quote)
    print('-' * len(quote) + '\n')


def print_figure(number_attemps):
    if number_attemps == 1:
        print(figure_1)
    elif number_attemps == 2:
        print(figure_2)
    elif number_attemps == 3:
        print(figure_3)
    elif number_attemps == 4:
        print(figure_4)


def init():
    quote = get_quote_random()
    # print(quote['author'])

    welcome(quote['quote'])
    who_said_it(quote['author'])


init()
