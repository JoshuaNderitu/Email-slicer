#collect email from user
#split the email using @, save the first prat as the user name 
#save the second part as  domain
#spit the domain using the dot

def main():
    print('Welcome to email slicer')
    print('')

    email_input = input('Enter Your Email: ')

    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')

    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension)

while True:
    main()