from flask import Flask,redirect,url_for
import webbrowser
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Hello World"

@app.route('/welcome/<name>')
def welcomeuser(name):
    return "Welcome %s on flask" % name

@app.route('/welcome')
def welcomeadmin():
    return "Welcome Admin"

@app.route('/login')
def gotoLogin():
    return "TO LOGIN PAGE"

@app.route('/logout')
def gotoLogout():
    return "TO LOGOUT PAGE"

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('welcomeadmin'))
    else:
        return redirect(url_for('welcomeuser',name = name))
    
@app.route('/google')
def gotoGoogle():
    print("Opening google.com")
    return webbrowser.open_new_tab('www.google.com')
    
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog showing %d' %postID

if __name__ == '__main__':
    app.run()