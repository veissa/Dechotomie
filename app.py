from flask import Flask, render_template, request, session
import random
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.urandom(24)  # Required for session

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'target' not in session:
        session['target'] = random.randint(0, 100)
        session['attempts'] = 0
        session['game_over'] = False
        session['won'] = False

    message = ""
    if request.method == 'POST':
        if session['game_over']:
            session['target'] = random.randint(0, 100)
            session['attempts'] = 0
            session['game_over'] = False
            session['won'] = False
            return render_template('index.html', message="New game started! Guess a number between 0 and 100", attempts=0, game_over=False)

        try:
            guess = int(request.form['guess'])
            session['attempts'] += 1

            if guess < 0 or guess > 100:
                message = "Please enter a number between 0 and 100"
                session['attempts'] -= 1
            elif guess < session['target']:
                message = "Too low!"
            elif guess > session['target']:
                message = "Too high!"
            else:
                message = f"Congratulations! Bizzuu! The flag is: CIT{{nf3atk_prepa_a_bizu_la}}"
                session['game_over'] = True
                session['won'] = True

            if session['attempts'] >= 10 and not session['won']:
                message = f"Game Over! yakh yakh awdi al9raya, awdi alprepa!"
                session['game_over'] = True

        except ValueError:
            message = "Please enter a valid number"
            session['attempts'] -= 1

    return render_template('index.html', 
                         message=message, 
                         attempts=session['attempts'],
                         game_over=session['game_over'])

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Use 0.0.0.0 to make the server publicly available
    app.run(host='0.0.0.0', port=port, debug=False) 