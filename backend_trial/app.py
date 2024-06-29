from flask import Flask, request, jsonify
from flask_cors import CORS
from phonenumbers import parse, geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import os
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests
geocoder = OpenCageGeocode(os.getenv('OPENCAGE_API_KEY', ''))

@app.route('/locatePhoneNumber', methods=['POST'])
def locate_phone_number():
    data = request.get_json()
    phone_number = data.get('phoneNumber')

    try:
        parsed_number = parse(phone_number)
        location = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")
        result = geocoder.geocode(location)

        if result and len(result) > 0:
            latitude = result[0]['geometry']['lat']
            longitude = result[0]['geometry']['lng']
            response = {
                'location': location,
                'serviceProvider': service_provider,
                'latitude': latitude,
                'longitude': longitude
            }
            return jsonify(response), 200
        else:
            return jsonify({'error': 'Failed to geocode location'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/locateDeviceByIMEI', methods=['POST'])
def locate_device_by_imei():
    data = request.get_json()
    imei = data.get('imei')
    gmail = data.get('gmail')
    password = data.get('password')

    # Perform your IMEI tracking logic here
    # Replace with actual logic to get location coordinates based on IMEI

    latitude = 41.8781
    longitude = -87.6298  # Example coordinates

    response = {
        'latitude': latitude,
        'longitude': longitude
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
