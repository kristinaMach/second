top = '''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░[CaptKraken's]░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░                                                                           ░░
░░        ██████╗ ██╗   ██╗███████╗███████╗███████╗    ██╗████████╗██╗       ░░
░░       ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ██║╚══██╔══╝██║       ░░
░░       ██║  ███╗██║   ██║█████╗  ███████╗███████╗    ██║   ██║   ██║       ░░
░░       ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║    ██║   ██║   ╚═╝       ░░
░░       ╚██████╔╝╚██████╔╝███████╗███████║███████║    ██║   ██║   ██╗       ░░
░░        ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝    ╚═╝   ╚═╝   ╚═╝       ░░
░░                                                                           ░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░[a guess-the-number game]░░░
░░                                                                           ░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|Menu: [p]lay - [r]ules - [a]bout - [q]uit|░░░'''

breaker = '◌=============================================================================◌'
about = '◌===================================About=====================================◌'
rules = '◌===================================Rules=====================================◌'
welcome = '◌============================|Welcome to Guess It|============================◌'

rule_txt = f'''{rules}\nto win: you have to correctly guess a randomly generated number.
\ndifferent difficulty level gives you different ranges of numbers and tries:
1-easy: number ranges from 1 to 10. you have 5 chances to guess the number.
2-medium: number ranges from 1 to 100. you have 7 chances to guess the number.
3-hard: number ranges from -500 to 500. you have 10 chances to guess the number.
\nif you understand the concept of binary search algorithm, you can win this easy.
the explanation that stuck with me was the one from the "finding David" part of 
CS50 2020 Lecture 0 here\'s the link to the video:
https://youtu.be/Tpl7k8IOT6E?t=3364
\nthe basic idea is to target the number in the middle of the range. 
ie: if it's from 1-10, you should start with 5. see if it's a higher or lower 
number than the correct number, then you repeat the process until you win.\n{breaker}'''

about_txt = f'''{about}
► created on 16/Nov/2020
► a guess-the-number game
► made with Python3
► by KIM SONG @CaptKrakenatic
{breaker}'''