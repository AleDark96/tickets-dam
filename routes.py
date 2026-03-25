from flask import request, jsonify
from models import db, User, Ticket, TicketComment

def register_routes(app):
    @app.route('/api/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        user = User(name=data['name'], email=data['email'], role=data.get('role','reporter'))
        db.session.add(user)
        db.session.commit()
        return jsonify({"data": {"id": user.id}}), 201

    @app.route('/api/tickets', methods=['POST'])
    def create_ticket():
        data = request.get_json()
        ticket = Ticket(user_id=data['user_id'], title=data['title'], body=data['body'])
        db.session.add(ticket)
        db.session.commit()
        return jsonify({"data": {"id": ticket.id}}), 201

    @app.route('/api/tickets', methods=['GET'])
    def list_tickets():
        tickets = Ticket.query.all()
        return jsonify({"data": [{"id": t.id, "title": t.title, "status": t.status} for t in tickets]})