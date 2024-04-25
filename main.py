import configparser
from classes.EmailSender import EmailSender
from classes.EmailValidator import EmailValidator
from classes.EmailSplitter import EmailSplitter
from classes.DomainPrefixAttacher import DomainPrefixAttacher

config = configparser.ConfigParser()
config.read('config.ini')

def getValidEmail():
    email = input('Por favor, insira o email da empresa (por exemplo, empresa@exemplo.com): ')
    while not email or not EmailValidator.check(email):
        email = input('Por favor, insira um email válido (por exemplo, empresa@exemplo.com): ')
    return email

def main():
    email = getValidEmail()
    prefix, domain = EmailSplitter.split_email(email)

    prefixes = config['EMAIL']['prefixes'].split(',')
    if prefix not in prefixes:
        prefixes.append(prefix)

    attacher = DomainPrefixAttacher(domain, prefixes)
    recipients = attacher.attach_prefixes()

    email_sender = EmailSender(
        config['AUTH']['email'],
        config['AUTH']['password']
    )

    email_sender.send(
        config['EMAIL']['subject'],
        config['EMAIL']['body'],
        recipients,
        config['EMAIL']['filename'],
        config['EMAIL']['attachment']
    )

    print('Email enviado com sucesso!')

if __name__ == "__main__":
    main()