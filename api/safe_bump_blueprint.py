from flask import Blueprint, request, jsonify

from services.predict import predict

safe_bump_blueprint = Blueprint('safe_bump_blueprint', __name__)


@safe_bump_blueprint.route("/api/predict_health")
def get_health_report():
    age = int(request.args.get('age'))
    systolicBP = int(request.args.get('systolic_bp'))
    diastolicBP = int(request.args.get('diastolic_bp'))
    bs = (request.args.get('bs'))
    bodyTemp = (request.args.get('body_temp'))
    heartRate = int(request.args.get('heart_rate'))
    try:
        return jsonify(result=predict(age, systolicBP, diastolicBP, bs, bodyTemp, heartRate), status=200, )
    except:
        return jsonify(result="Error", status=500)
