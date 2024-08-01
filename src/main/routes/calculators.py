from flask import Blueprint, jsonify, request
from src.main.calculators.calculator_1 import Calculator1

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    calculator1 = Calculator1()
    calculator1.calculate(request)
    
    return jsonify({
        "success": True
    }), 200