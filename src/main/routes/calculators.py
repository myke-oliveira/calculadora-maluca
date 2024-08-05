from flask import Blueprint, jsonify, request
from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator2_factory import calculator2_factory

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    calculator1 = calculator1_factory()
    response = calculator1.calculate(request)
    
    return jsonify(response), 200

@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    calculator2 = calculator2_factory()
    response = calculator2.calculate(request)
    
    return jsonify(response), 200