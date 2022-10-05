from . import bp as app
from flask import render_template, request, redirect, url_for, flash, g
from app.blueprints.main.models import User, Pokemon
from app import db
from app.blueprints.main.forms import PokemonGift, PokemonCapture
from flask_login import current_user, login_required

@app.route('/', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)
        pokemons = Pokemon.query.all()
        users = User.query.all()
        form = PokemonCapture()

        if request.method == 'GET':
            return render_template('home.html', current=current, pokemons=pokemons, users=users, form=form, currentCall=currentCall)

        if request.method == 'POST':
            enteredPokemon = form.capture.data.lower()
            stringPokemon = str(enteredPokemon)

            wantedPokemon = Pokemon.query.filter_by(name=stringPokemon).first()
            wantedPokemon.user_id = int(current.id)
            db.session.commit()
            flash(f'{stringPokemon} Captured!', 'success')
            return redirect(url_for('main.home'))

        else:
            return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('auth.login'))

@app.route('/gift', methods=['GET', 'POST'])
@login_required
def createGift():
    form = PokemonGift()
    if request.method == 'GET':
        return render_template('gift.html', form = form)
    if request.method == 'POST':
        name = request.form['name'].lower()
        description = request.form['description'].lower()
        type = request.form['type'].lower()
        
        gift = Pokemon(name=name, description=description, type=type, user_id=None)

        try:
            db.session.add(gift)
            db.session.commit()
            flash('This Pokemon has been gifted successfully, thank you!', 'success')
            return redirect(url_for('main.home'))

        except:
            flash('You cannot add this Pokemon, please try again!', 'success')
            return redirect(url_for('main.home'))
    else:
        return redirect(url_for('auth.login'))

@app.route('/collection')
@login_required
def collection():
    users = User.query.all()
    pokemons = Pokemon.query.all()
    return render_template('collection.html', users=users, pokemons=pokemons)

@app.route('/user/<id>')
@login_required
def user(id):
    user = User.query.get(id)
    pokemons = Pokemon.query.all()
    return render_template('user.html', user=user, pokemons=pokemons)

@app.route('/profile')
@login_required
def profile():
    if current_user.is_authenticated:
        currentCall = current_user.get_id()
        current = User.query.get(currentCall)
        pokemons = Pokemon.query.all()
        users = User.query.all()
        form = PokemonCapture()

        if request.method == 'GET':
            return render_template('profile.html', current=current, pokemons=pokemons, users=users, form=form, currentCall=currentCall)

        if request.method == 'POST':
            enteredPokemon = form.capture.data.lower()
            stringPokemon = str(enteredPokemon)

            wantedPokemon = Pokemon.query.filter_by(name=stringPokemon).first()
            wantedPokemon.user_id = int(current.id)
            db.session.commit()
            flash(f'{stringPokemon} Captured!', 'success')
            return redirect(url_for('main.profile'))

        else:
            return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('auth.login'))

