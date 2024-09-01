# to run the app  ---> flasky

from app import create_app

if __name__=='__main__':
    app = create_app()
    app.run(debug=True)