from input_ import Input_
from user import User
from project import Project


def main():
    PROJECT_FILE = "./csvs/projects.csv"
    Project.print_projects(PROJECT_FILE)

    Input_.print_title("Welcome to DADO")
    leave = False
    while not leave:

        current_user = User()

        options = {"L": "Login", "R": "Registre", "V": "Veure projectes"}

        current_user.authenticator(options)


if __name__ == "__main__":
    main()
