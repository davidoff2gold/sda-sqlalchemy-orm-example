from models import User
from session import session


def main():
    for user in session.query(User):
        print(user)


if __name__ == "__main__":
    main()
