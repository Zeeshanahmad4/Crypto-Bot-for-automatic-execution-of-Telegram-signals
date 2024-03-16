from flask import Flask, render_template, request, redirect, url_for, flash
from .models import Trade, db
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your own secret key

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trades.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Define routes and views
@app.route('/')
def index():
    """Render the dashboard homepage."""
    trades = Trade.query.all()
    return render_template('index.html', trades=trades)

@app.route('/add_trade', methods=['POST'])
def add_trade():
    """Add a new trade."""
    # Extract trade data from the form
    coin = request.form['coin']
    action = request.form['action']
    quantity = request.form['quantity']
    timestamp = datetime.now()

    # Create a new Trade object and add it to the database
    new_trade = Trade(coin=coin, action=action, quantity=quantity, timestamp=timestamp)
    db.session.add(new_trade)
    db.session.commit()

    flash('Trade added successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
# Dashboard Application 
