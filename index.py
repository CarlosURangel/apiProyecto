from app import app
from utils.db import db

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
