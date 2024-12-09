from flask import Flask
from routes.transactions import transactions
from utils.db import db

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/minisuper'
app.config['SQLALCHEMY_BINDS'] = {
    'telcel': 'mysql://root:@localhost/telcel',
    'dalefon': 'mysql://root:@localhost/dalefon',
    'bait': 'mysql://root:@localhost/bait',
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db.init_app(app)

# Registrar blueprints
app.register_blueprint(transactions)
