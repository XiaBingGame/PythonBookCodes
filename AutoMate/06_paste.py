import sys
import pyperclip

PASSWORD = {'email': 'F7min18ajfoejioje',
            'blog': 'fwoeihoigfioanf',
            'luggage': '123456'}

if __name__ == '__main__':
    account = 'email'
    if account in PASSWORD:
        print(PASSWORD[account])
        pyperclip.copy(PASSWORD[account])
    else:
        print('No account')

    print('Done.')
    sys.exit(0)
