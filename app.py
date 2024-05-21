from flask import Flask,render_template
import requests 
from dotenv import load_dotenv,dotenv_values 

config = dotenv_values('pokedex_app/.env')

app = Flask(__name__)

def get_pokemon_data(pokemon):
    URL_API = config['URL_API']
    url = f'{URL_API}/pokemon/{pokemon}'
    r = requests.get(url).json()
    return r

@app.route('/',methods=['GET', 'POST'])
def index():
    r = get_pokemon_data('charmander')
    pokemon = {
        'name':r.get('name'),
        'order':r.get('order'),
        'height':r.get('height'),
        'weight':r.get('weight'),
        'sprite':r.get('sprites').get('other').get('official-artwork').get('front_default')
    }
    print(pokemon)

    return render_template('index.html', pokemon = pokemon)


if __name__ == '__main__':
    app.run(debug=True)