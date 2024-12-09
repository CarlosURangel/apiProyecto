from flask import Blueprint, jsonify, request
from models.transaction import MinisuperTransaction, TelcelTransaction, DalefonTransaction, BaitTransaction
from utils.db import db

transactions = Blueprint('transactions', __name__)

@transactions.route('/new', methods=['POST'])
def add_transaction():
    if not request.is_json:
        return jsonify({"error": "Formato JSON requerido"}), 400

    data = request.get_json()

    phone = data.get('phone_number')
    amount = data.get('amount')
    company = data.get('company')

    if not phone or not amount or not company:
        return jsonify({"error": "Faltan datos en la solicitud"}), 400

    try:
        num_amount = float(amount)
        commission_rate = 0.05
        commission = num_amount * commission_rate

        # Registrar en la base de datos del minisúper
        new_minisuper_transaction = MinisuperTransaction(
            phone_number=phone,
            amount=num_amount,
            response="Pending",
            commission=commission
        )
        db.session.add(new_minisuper_transaction)

        # Registrar en la base de datos de la compañía seleccionada
        if company == 'telcel':
            new_transaction = TelcelTransaction(
                phone_number=phone,
                amount=num_amount,
                response="Pending",
                commission=commission
            )
        elif company == 'dalefon':
            new_transaction = DalefonTransaction(
                phone_number=phone,
                amount=num_amount,
                response="Pending",
                commission=commission
            )
        elif company == 'bait':
            new_transaction = BaitTransaction(
                phone_number=phone,
                amount=num_amount,
                response="Pending",
                commission=commission
            )
        else:
            return jsonify({"error": "Compañía no válida"}), 400

        db.session.add(new_transaction)
        db.session.commit()

        return jsonify({"message": "Transacción registrada con éxito", "transaction_id": new_minisuper_transaction.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
