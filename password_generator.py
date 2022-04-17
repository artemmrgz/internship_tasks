import random
from string import ascii_uppercase, ascii_lowercase, punctuation, digits

LENGTH = 14


def generate_password(length):
    characters = ascii_uppercase + ascii_lowercase + punctuation + digits
    password = list(map(random.choice,
                        (ascii_uppercase, ascii_lowercase, punctuation, digits)
                        ))
    for i in range(length - len(password)):
        password.append(random.choice(characters))
    random.shuffle(password)
    return ''.join(password)


if __name__ == '__main__':
    print(generate_password(LENGTH))
