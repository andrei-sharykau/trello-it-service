from flask import Flask, render_template, request, redirect,  url_for
from forms import LoginForm

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'a really really really really long secret key'

@app.route('/', methods=['get', 'post'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        print(login)
        print(password)


        # здесь логика базы данных

        print("\nData received. Now redirecting ...")
        return redirect(url_for('index'))


    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()