from faker import Faker
from sqlalchemy.exc import IntegrityError

from models import Base, User
from session import session


def create_users(count=50):
    fake = Faker()
    return [
        User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            user_name=fake.user_name(),
            salary=fake.pyfloat(
                min_value=4000,
                max_value=10_000
            ),
            email=fake.email(),
        )
        for _ in range(count)
    ]


def main():
    # Create all tables
    Base.metadata.create_all()

    # Create users
    users = create_users(count=1001)
    for user in users:
        print(f"Adding user {user.user_name}")
        try:
            session.add(user)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"User {user.user_name} already exists")


if __name__ == "__main__":
    main()