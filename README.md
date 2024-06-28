# GeoTracker.py 🌍📞

## Overview
GeoTracker.py is a Python script that helps you locate the geographical coordinates and service provider of a phone number using the OpenCage Geocoder API and Phonenumbers library.

### Features
- Retrieve location and service provider details of any international phone number.
- Calculate distance between your current location and the target phone number's location.
- Open Google Maps with directions from your location to the target.

## Requirements
Before running the script, ensure you have:
- Python 3.x installed.
- An API key from OpenCage Geocoder (get one at [OpenCage Geocoder](https://opencagedata.com/)).

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/CHEGEBB/Geo-Phone-Tracker.git
   cd Geo-Phone-Tracker

2. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Setup API Key
1. Sign up for an API key at [OpenCage Geocoder](https://opencagedata.com/).
2. Create a `.env` file in the root directory of the project.
3. Add your API key to the `.env` file:
   ```
   OPENCAGE_API_KEY=your_opencage_api_key_here
   ```

## Usage
Run the script from the command line:
```bash
python GeoTracker.py
```

### Steps:
1. Choose option `1` to locate a phone number.
2. Enter the phone number in international format (e.g., `+123456789`).
3. The script will:
   - Determine the country and service provider of the phone number.
   - Retrieve the coordinates of the location associated with the phone number.
   - Prompt you to enter your current location (city or address).
   - Calculate the distance between your location and the phone number's location.
   - Open Google Maps in your default browser with directions from your location to the phone number's location.

## Example
Let's say you want to locate a phone number `+123456789`:

1. Enter `+123456789` when prompted.
2. The script will display the location (Kenya) and service provider (Safaricom) associated with the phone number.
3. It will ask for your current location to calculate and display the distance between your location and the phone number's location.
4. Finally, it will open Google Maps with directions to the phone number's location.

Enjoy exploring the Phone Number Locator!

## Author
- Created by CHEGEBB
- GitHub: [CHEGEBB](https://github.com/CHEGEBB)

```

### Notes:
- Customize the GitHub repository URL (`https://github.com/yourusername/GeoTracker.git`) and author information (`CHEGEBB`) as appropriate.
- Ensure your `.env` file and API key are correctly set up before running the script.

