from website import create_app
app = create_app()
if __name__ == '__main__':
    app.run(debug=True) # these two lines make the program so
    # that it only runs when the main.py file is run, 
    # not if the main.py file is imported
    # debug=True means that it will rerun the server every time we edit the code


 