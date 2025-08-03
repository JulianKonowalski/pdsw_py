from dotenv import load_dotenv
from src.App import App

"""
Don't forget to add a .env file
and set the ROOT_FOLDER variable
to the project's root folder. 
"""
if __name__ == "__main__":
    load_dotenv()
    app: App = App()
    app.run()