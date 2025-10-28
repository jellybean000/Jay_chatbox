from datetime import datetime
bot_input = input('Please enter your bot name: ')
print(f'Welcome {bot_input} to your jelchat box!')

while True:
    user_input = input('You: ').lower()
    
    if user_input in ['hi', 'hello', 'hey']:
        print(f"{bot_input}: Hello! How are you today?")
    elif user_input in ['bye', 'see you']:
        print(f"{bot_input}: Goodbye! Have a great day!")
        break
    elif user_input in ['how are you', 'how is it going']:
        print(f"{bot_input}: I'm just a bot, but thanks for asking!")
    elif user_input in ['time', 'what time is it']:
        print(f"{bot_input}: the current time is {datetime.now().strftime('%H:%M:%S')}")
    elif user_input in ['what is your name', 'how do you say speel your name']:
        print(f'my name is spelled {bot_input}')
    elif user_input in ['+', 'add']:
        print(f'{bot_input}: Please enter two numbers you want to add: ')
        try:
            num1 = float(input('First number: '))
            num2 = float(input('Second number: '))
            result = num1 + num2
            print(f'{bot_input}: The sum of {num1} and {num2} is {result}.')
        except ValueError:
            print(f'{bot_input}: Invalid input. Please enter numeric values. Try again.')
    else:
        print(f"{bot_input}: I'm sorry, I did not understand that. Please try again.")
