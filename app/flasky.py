# to run the app  ---> flasky

# the entry to run project
from app import create_app

if __name__=='__main__':
    app = create_app()
    app.run(debug=True)