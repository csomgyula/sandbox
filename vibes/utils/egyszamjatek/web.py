from flask import Flask, render_template, request, redirect, url_for
import os
import importlib.util
import shutil
from egyszam_jatek import ParhuzamosEgyszamJatek

UPLOAD_FOLDER = 'uploads'
PLAYER_FOLDER = os.path.join(UPLOAD_FOLDER, 'player')
TRNG_FOLDER = os.path.join(UPLOAD_FOLDER, 'trng')

os.makedirs(PLAYER_FOLDER, exist_ok=True)
os.makedirs(TRNG_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def list_modules(folder):
    return [f[:-3] for f in os.listdir(folder) if f.endswith('.py')]


def import_module_from_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@app.route('/')
def index():
    player_modules = list_modules(PLAYER_FOLDER)
    trng_modules = list_modules(TRNG_FOLDER)
    return render_template('index.html', players=player_modules, trngs=trng_modules)


@app.route('/upload_player', methods=['POST'])
def upload_player():
    file = request.files['player_file']
    if file and file.filename.endswith('.py'):
        file.save(os.path.join(PLAYER_FOLDER, file.filename))
    return redirect(url_for('index'))


@app.route('/upload_trng', methods=['POST'])
def upload_trng():
    file = request.files['trng_file']
    if file and file.filename.endswith('.py'):
        file.save(os.path.join(TRNG_FOLDER, file.filename))
    return redirect(url_for('index'))


@app.route('/play', methods=['POST'])
def play():
    korok_szama = int(request.form['korok'])
    trng_name = request.form['trng_name']

    # Betöltés
    player_files = list_modules(PLAYER_FOLDER)
    trng_module_path = os.path.join(TRNG_FOLDER, trng_name + '.py')
    trng_module = import_module_from_path(trng_name, trng_module_path)
    trng_class = trng_module.EgyszamJatekos

    trngs = [trng_class(korok_szama) for _ in range(len(player_files))]
    players = []
    player_names = []
    for fname in player_files:
        module_path = os.path.join(PLAYER_FOLDER, fname + '.py')
        module = import_module_from_path(fname, module_path)
        players.append(module.EgyszamJatekos(korok_szama))
        player_names.append(fname)

    jatek = ParhuzamosEgyszamJatek(korok_szama, trngs, players)
    jatek.run()

    return render_template(
        'eredmeny.html',
        korok_szama=korok_szama,
        trng_name=trng_name,
        player_names=player_names,
        eredmenyek=jatek.eredmenyek,
        vegso_eredmeny=jatek.vegso_eredmeny()
    )


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        UPLOAD_FOLDER = sys.argv[1]
    PLAYER_FOLDER = os.path.join(UPLOAD_FOLDER, 'player')
    TRNG_FOLDER = os.path.join(UPLOAD_FOLDER, 'trng')
    os.makedirs(PLAYER_FOLDER, exist_ok=True)
    os.makedirs(TRNG_FOLDER, exist_ok=True)
    app.run(debug=True)
