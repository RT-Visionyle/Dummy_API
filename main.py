from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Read API key from environment variable (set later in Render)
VALID_API_KEY = os.getenv("API_KEY", "my-secret-key-123")

PRODUCTS = [
    {"id": 1, "name": "Quantum Widget", "category": "Gadgets", "price": 19.99, "description": "A compact device for enhancing signal strength.", "life_cycle_status": "Active"},
    {"id": 2, "name": "Gizmo Pro", "category": "Gadgets", "price": 29.50, "description": "Multi-functional gadget with touch controls.", "life_cycle_status": "In Development"},
    {"id": 3, "name": "Thingamajig", "category": "Tools", "price": 9.75, "description": "Versatile tool for precision tasks.", "life_cycle_status": "Active"},
    {"id": 4, "name": "Smart Bulb", "category": "Home", "price": 14.99, "description": "Wi-Fi enabled LED bulb with color options.", "life_cycle_status": "Active"},
    {"id": 5, "name": "Eco Charger", "category": "Electronics", "price": 24.95, "description": "Solar-powered phone charger.", "life_cycle_status": "In Development"},
    {"id": 6, "name": "Flex Hammer", "category": "Tools", "price": 12.50, "description": "Ergonomic hammer with rubber grip.", "life_cycle_status": "Active"},
    {"id": 7, "name": "Nano Drone", "category": "Gadgets", "price": 49.99, "description": "Miniature drone with HD camera.", "life_cycle_status": "Active"},
    {"id": 8, "name": "Therma Mug", "category": "Kitchen", "price": 18.75, "description": "Insulated mug for hot and cold drinks.", "life_cycle_status": "Active"},
    {"id": 9, "name": "VR Headset X", "category": "Electronics", "price": 199.99, "description": "Immersive virtual reality headset.", "life_cycle_status": "In Development"},
    {"id": 10, "name": "Power Drill", "category": "Tools", "price": 59.99, "description": "Cordless drill with multiple speed settings.", "life_cycle_status": "Active"},
    {"id": 11, "name": "Smart Thermostat", "category": "Home", "price": 89.50, "description": "Energy-saving thermostat with app control.", "life_cycle_status": "Active"},
    {"id": 12, "name": "Glow Lamp", "category": "Home", "price": 22.30, "description": "Adjustable brightness desk lamp.", "life_cycle_status": "Discontinued"},
    {"id": 13, "name": "Fitness Tracker", "category": "Wearables", "price": 39.99, "description": "Tracks steps, heart rate, and sleep.", "life_cycle_status": "Active"},
    {"id": 14, "name": "Blender Pro", "category": "Kitchen", "price": 79.99, "description": "High-speed blender for smoothies.", "life_cycle_status": "Active"},
    {"id": 15, "name": "Wireless Mouse", "category": "Electronics", "price": 15.99, "description": "Ergonomic mouse with long battery life.", "life_cycle_status": "Active"},
    {"id": 16, "name": "Camping Stove", "category": "Outdoor", "price": 45.00, "description": "Portable stove for outdoor cooking.", "life_cycle_status": "Active"},
    {"id": 17, "name": "Air Purifier", "category": "Home", "price": 129.99, "description": "HEPA filter for clean indoor air.", "life_cycle_status": "Active"},
    {"id": 18, "name": "Smart Speaker", "category": "Electronics", "price": 69.99, "description": "Voice-activated speaker with AI assistant.", "life_cycle_status": "In Development"},
    {"id": 19, "name": "Yoga Mat", "category": "Fitness", "price": 24.99, "description": "Non-slip mat for yoga and exercise.", "life_cycle_status": "Active"},
    {"id": 20, "name": "Solar Lantern", "category": "Outdoor", "price": 19.50, "description": "Rechargeable lantern for camping.", "life_cycle_status": "Active"},
    {"id": 21, "name": "Coffee Maker", "category": "Kitchen", "price": 49.99, "description": "Programmable drip coffee machine.", "life_cycle_status": "Active"},
    {"id": 22, "name": "Dash Cam", "category": "Electronics", "price": 59.95, "description": "HD dashboard camera for vehicles.", "life_cycle_status": "Active"},
    {"id": 23, "name": "Toolbox Set", "category": "Tools", "price": 89.99, "description": "Complete toolkit for home repairs.", "life_cycle_status": "Active"},
    {"id": 24, "name": "Wireless Earbuds", "category": "Electronics", "price": 39.99, "description": "Noise-canceling earbuds with case.", "life_cycle_status": "Active"},
    {"id": 25, "name": "Portable Grill", "category": "Outdoor", "price": 65.00, "description": "Compact grill for tailgating.", "life_cycle_status": "Active"},
    {"id": 26, "name": "Smart Lock", "category": "Home", "price": 99.99, "description": "Keyless entry lock with app control.", "life_cycle_status": "In Development"},
    {"id": 27, "name": "Electric Kettle", "category": "Kitchen", "price": 29.99, "description": "Fast-boiling kettle with auto shut-off.", "life_cycle_status": "Active"},
    {"id": 28, "name": "Robot Vacuum", "category": "Home", "price": 199.99, "description": "Automated vacuum for pet hair.", "life_cycle_status": "Active"},
    {"id": 29, "name": "Gaming Mouse", "category": "Electronics", "price": 49.99, "description": "Customizable mouse for gaming.", "life_cycle_status": "Active"},
    {"id": 30, "name": "Hiking Backpack", "category": "Outdoor", "price": 79.99, "description": "Water-resistant backpack for hiking.", "life_cycle_status": "Active"},
    {"id": 31, "name": "Smart Watch", "category": "Wearables", "price": 149.99, "description": "Fitness and notification smartwatch.", "life_cycle_status": "Active"},
    {"id": 32, "name": "Cordless Vacuum", "category": "Home", "price": 129.99, "description": "Lightweight vacuum for quick cleanups.", "life_cycle_status": "Active"},
    {"id": 33, "name": "Food Processor", "category": "Kitchen", "price": 89.99, "description": "Multi-function food prep appliance.", "life_cycle_status": "Active"},
    {"id": 34, "name": "Action Camera", "category": "Electronics", "price": 99.99, "description": "Waterproof camera for adventures.", "life_cycle_status": "Active"},
    {"id": 35, "name": "Treadmill", "category": "Fitness", "price": 499.99, "description": "Foldable treadmill with digital display.", "life_cycle_status": "Active"},
    {"id": 36, "name": "Smart Doorbell", "category": "Home", "price": 129.99, "description": "Video doorbell with motion detection.", "life_cycle_status": "In Development"},
    {"id": 37, "name": "Electric Screwdriver", "category": "Tools", "price": 34.99, "description": "Rechargeable screwdriver with bits.", "life_cycle_status": "Active"},
    {"id": 38, "name": "Portable Speaker", "category": "Electronics", "price": 49.99, "description": "Bluetooth speaker with deep bass.", "life_cycle_status": "Active"},
    {"id": 39, "name": "Camping Tent", "category": "Outdoor", "price": 89.99, "description": "4-person tent with rainfly.", "life_cycle_status": "Active"},
    {"id": 40, "name": "Toaster Oven", "category": "Kitchen", "price": 59.99, "description": "Compact oven for baking and toasting.", "life_cycle_status": "Active"},
    {"id": 41, "name": "Smart Plug", "category": "Home", "price": 19.99, "description": "Wi-Fi enabled plug for automation.", "life_cycle_status": "Active"},
    {"id": 42, "name": "Fitness Dumbbells", "category": "Fitness", "price": 49.99, "description": "Adjustable weight dumbbell set.", "life_cycle_status": "Active"},
    {"id": 43, "name": "Laptop Stand", "category": "Electronics", "price": 29.99, "description": "Ergonomic stand for laptops.", "life_cycle_status": "Active"},
    {"id": 44, "name": "Sleeping Bag", "category": "Outdoor", "price": 39.99, "description": "Warm sleeping bag for cold weather.", "life_cycle_status": "Active"},
    {"id": 45, "name": "Air Fryer", "category": "Kitchen", "price": 79.99, "description": "Healthy frying with minimal oil.", "life_cycle_status": "Active"},
    {"id": 46, "name": "Smart Scale", "category": "Fitness", "price": 34.99, "description": "Body composition scale with app.", "life_cycle_status": "Active"},
    {"id": 47, "name": "Cordless Saw", "category": "Tools", "price": 99.99, "description": "Battery-powered saw for woodworking.", "life_cycle_status": "Active"},
    {"id": 48, "name": "Noise Machine", "category": "Home", "price": 29.99, "description": "White noise machine for sleep.", "life_cycle_status": "Active"},
    {"id": 49, "name": "Gaming Keyboard", "category": "Electronics", "price": 69.99, "description": "RGB mechanical keyboard.", "life_cycle_status": "Active"},
    {"id": 50, "name": "Cooler Bag", "category": "Outdoor", "price": 24.99, "description": "Insulated bag for picnics.", "life_cycle_status": "Active"},
    {"id": 51, "name": "Electric Blanket", "category": "Home", "price": 49.99, "description": "Heated blanket with timer.", "life_cycle_status": "Active"},
    {"id": 52, "name": "Smart Fridge", "category": "Kitchen", "price": 999.99, "description": "Refrigerator with touchscreen display.", "life_cycle_status": "In Development"},
    {"id": 53, "name": "Power Bank", "category": "Electronics", "price": 29.99, "description": "High-capacity portable charger.", "life_cycle_status": "Active"},
    {"id": 54, "name": "Hedge Trimmer", "category": "Tools", "price": 79.99, "description": "Cordless trimmer for gardening.", "life_cycle_status": "Active"},
    {"id": 55, "name": "Smart Mirror", "category": "Home", "price": 199.99, "description": "Interactive mirror with fitness apps.", "life_cycle_status": "In Development"},
    {"id": 56, "name": "Kettlebell", "category": "Fitness", "price": 39.99, "description": "Cast iron kettlebell for workouts.", "life_cycle_status": "Active"},
    {"id": 57, "name": "Dash Blender", "category": "Kitchen", "price": 49.99, "description": "Single-serve blender for quick drinks.", "life_cycle_status": "Active"},
    {"id": 58, "name": "Smart Glasses", "category": "Wearables", "price": 249.99, "description": "Augmented reality glasses.", "life_cycle_status": "In Development"},
    {"id": 59, "name": "Leaf Blower", "category": "Tools", "price": 89.99, "description": "Electric blower for yard cleanup.", "life_cycle_status": "Active"},
    {"id": 60, "name": "Humidifier", "category": "Home", "price": 39.99, "description": "Ultrasonic humidifier for dry air.", "life_cycle_status": "Active"},
    {"id": 61, "name": "Smart Kettle", "category": "Kitchen", "price": 59.99, "description": "App-controlled kettle with presets.", "life_cycle_status": "In Development"},
    {"id": 62, "name": "Dashcam Pro", "category": "Electronics", "price": 79.99, "description": "4K dashcam with night vision.", "life_cycle_status": "Active"},
    {"id": 63, "name": "Camp Chair", "category": "Outdoor", "price": 29.99, "description": "Foldable chair for camping.", "life_cycle_status": "Active"},
    {"id": 64, "name": "Smart Fan", "category": "Home", "price": 69.99, "description": "Wi-Fi enabled fan with remote.", "life_cycle_status": "Active"},
    {"id": 65, "name": "Rowing Machine", "category": "Fitness", "price": 299.99, "description": "Compact rower for home workouts.", "life_cycle_status": "Active"},
    {"id": 66, "name": "LED Strip", "category": "Home", "price": 19.99, "description": "Color-changing LED strip lights.", "life_cycle_status": "Active"},
    {"id": 67, "name": "Cordless Sander", "category": "Tools", "price": 69.99, "description": "Battery-powered sander for projects.", "life_cycle_status": "Active"},
    {"id": 68, "name": "Smart Camera", "category": "Home", "price": 89.99, "description": "Security camera with cloud storage.", "life_cycle_status": "Active"},
    {"id": 69, "name": "Espresso Machine", "category": "Kitchen", "price": 149.99, "description": "Compact espresso maker with frother.", "life_cycle_status": "Active"},
    {"id": 70, "name": "Fitness Bike", "category": "Fitness", "price": 249.99, "description": "Stationary bike with resistance levels.", "life_cycle_status": "Active"},
    {"id": 71, "name": "Smart Alarm", "category": "Home", "price": 39.99, "description": "Alarm clock with sunrise simulation.", "life_cycle_status": "Active"},
    {"id": 72, "name": "Portable Monitor", "category": "Electronics", "price": 129.99, "description": "USB-C powered second screen.", "life_cycle_status": "Active"},
    {"id": 73, "name": "Hammock", "category": "Outdoor", "price": 49.99, "description": "Lightweight hammock for camping.", "life_cycle_status": "Active"},
    {"id": 74, "name": "Rice Cooker", "category": "Kitchen", "price": 39.99, "description": "Multi-function rice and grain cooker.", "life_cycle_status": "Active"},
    {"id": 75, "name": "Smart Blinds", "category": "Home", "price": 149.99, "description": "Automated blinds with app control.", "life_cycle_status": "In Development"},
    {"id": 76, "name": "Power Washer", "category": "Tools", "price": 199.99, "description": "High-pressure washer for cleaning.", "life_cycle_status": "Active"},
    {"id": 77, "name": "Smart Ring", "category": "Wearables", "price": 99.99, "description": "Fitness and sleep tracking ring.", "life_cycle_status": "In Development"},
    {"id": 78, "name": "Electric Grill", "category": "Kitchen", "price": 89.99, "description": "Indoor grill with adjustable heat.", "life_cycle_status": "Active"},
    {"id": 79, "name": "Smart Sprinkler", "category": "Outdoor", "price": 129.99, "description": "Wi-Fi controlled sprinkler system.", "life_cycle_status": "Active"},
    {"id": 80, "name": "Massage Gun", "category": "Fitness", "price": 99.99, "description": "Percussive therapy for muscle recovery.", "life_cycle_status": "Active"},
    {"id": 81, "name": "Smart Oven", "category": "Kitchen", "price": 249.99, "description": "Wi-Fi enabled oven with recipes.", "life_cycle_status": "In Development"},
    {"id": 82, "name": "Laser Level", "category": "Tools", "price": 49.99, "description": "Self-leveling laser for construction.", "life_cycle_status": "Active"},
    {"id": 83, "name": "Smart Light Switch", "category": "Home", "price": 29.99, "description": "Wi-Fi enabled light switch.", "life_cycle_status": "Active"},
    {"id": 84, "name": "Gaming Headset", "category": "Electronics", "price": 79.99, "description": "Surround sound headset for gaming.", "life_cycle_status": "Active"},
    {"id": 85, "name": "Backpacking Stove", "category": "Outdoor", "price": 39.99, "description": "Lightweight stove for backpacking.", "life_cycle_status": "Active"},
    {"id": 86, "name": "Slow Cooker", "category": "Kitchen", "price": 49.99, "description": "Programmable cooker for meals.", "life_cycle_status": "Active"},
    {"id": 87, "name": "Smart Projector", "category": "Electronics", "price": 299.99, "description": "Portable projector with streaming.", "life_cycle_status": "In Development"},
    {"id": 88, "name": "Resistance Bands", "category": "Fitness", "price": 19.99, "description": "Set of bands for strength training.", "life_cycle_status": "Active"},
    {"id": 89, "name": "Smart Garage", "category": "Home", "price": 99.99, "description": "App-controlled garage door opener.", "life_cycle_status": "Active"},
    {"id": 90, "name": "Cordless Jigsaw", "category": "Tools", "price": 79.99, "description": "Battery-powered jigsaw for cutting.", "life_cycle_status": "Active"},
    {"id": 91, "name": "Smart Earplugs", "category": "Wearables", "price": 49.99, "description": "Noise-filtering earplugs with app.", "life_cycle_status": "In Development"},
    {"id": 92, "name": "Ice Maker", "category": "Kitchen", "price": 99.99, "description": "Countertop ice maker for parties.", "life_cycle_status": "Active"},
    {"id": 93, "name": "Smart Humidifier", "category": "Home", "price": 79.99, "description": "App-controlled humidifier.", "life_cycle_status": "Active"},
    {"id": 94, "name": "Camping Lantern", "category": "Outdoor", "price": 29.99, "description": "Rechargeable lantern with SOS mode.", "life_cycle_status": "Active"},
    {"id": 95, "name": "Smart Toaster", "category": "Kitchen", "price": 69.99, "description": "Toaster with digital settings.", "life_cycle_status": "In Development"},
    {"id": 96, "name": "Fitness Roller", "category": "Fitness", "price": 24.99, "description": "Foam roller for muscle recovery.", "life_cycle_status": "Active"},
    {"id": 97, "name": "Smart Thermometer", "category": "Home", "price": 39.99, "description": "Wi-Fi enabled indoor thermometer.", "life_cycle_status": "Active"},
    {"id": 98, "name": "Cordless Blower", "category": "Tools", "price": 69.99, "description": "Battery-powered blower for debris.", "life_cycle_status": "Active"},
    {"id": 99, "name": "Smart Headphones", "category": "Electronics", "price": 149.99, "description": "Noise-canceling headphones with AI.", "life_cycle_status": "In Development"},
    {"id": 100, "name": "Portable Hammock", "category": "Outdoor", "price": 59.99, "description": "Quick-setup hammock for travel.", "life_cycle_status": "Active"}
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Dummy Product API"}), 200

@app.route("/products", methods=["GET"])
def get_products():
    api_key = request.headers.get("x-api-key")
    if not api_key:
        return jsonify({"error": "API key missing"}), 401

    if api_key != VALID_API_KEY:
        return jsonify({"error": "Invalid API key"}), 401

    category = request.args.get("category")
    if category:
        filtered = [p for p in PRODUCTS if p["category"].lower() == category.lower()]
        return jsonify(filtered), 200

    return jsonify(PRODUCTS), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

