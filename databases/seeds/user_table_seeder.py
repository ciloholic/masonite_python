"""User Table Seeder.

You can run this seeder in order to generate users.

    - Each time it is ran it will generate 50 random users.
    - All users have the password of 'secret'.
    - You can run the seeder by running: craft seed:run.
"""

from app.User import User

from orator.seeds import Seeder


class UserTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.factory.register(User, self.users_factory)

        self.factory(User, 50).create()

    def users_factory(self, faker):
        return {
            'name': faker.name(),
            'email': faker.email(),
            'password': '$2b$12$WMgb5Re1NqUr.uSRfQmPQeeGWudk/8/aNbVMpD1dR.Et83vfL8WAu',  # == 'secret'
        }
