# Take function from math module
from math import sin, cos, sqrt, atan2, radians

# Declaration of the arrays
locations = [
    {'id': 1000, 'zip_code': '37069', 'lat': 45.31, 'lng': 10.81},
    {'id': 1000, 'zip_code': '37069', 'lat': 45.33, 'lng': 10.82},
    {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84}, 
    {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99}, 
    {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00}, 
    {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02},
    {'id': 1002, 'zip_code': '37133', 'lat': 45.47, 'lng': 11.03},
    {'id': 1002, 'zip_code': '37133', 'lat': 45.46, 'lng': 11.05}

];

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True}, 
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True}, 
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': True}, 
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': True}, 
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': True}, 
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': True}, 
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': True},
];

# Haversine function
def haversine(lat1, lng1, lat2, lng2): 
    # approximate radius of earth in km
    R = 6373.0;

    #transform the coordinates in radians from degrees
    lat1 = radians(lat1);
    lng1 = radians(lng1);
    lat2 = radians(lat2);
    lng2 = radians(lng2);

    #calculate the distance
    dlng = lng2 - lng1;
    dlat = lat2 - lat1;

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2;
    c = 2 * atan2(sqrt(a), sqrt(1 - a));

    distance = R * c;
    return distance;

# Coverage function
def coverage(locations, shoppers):
    coverageShoppers = [];

    for shop in shoppers:
        coverageShop = dict();
        coverageShop['shopper_id'] = shop['id'];

        coverageLocation = 0;

        # Check the number of enabled locations
        for location in locations:
            if (haversine(shop['lat'], shop['lng'], location['lat'], location['lng']) < 10):
                coverageLocation = coverageLocation + 1;
            
        
        coverageShop['coverage'] = (coverageLocation * 100) / len(locations);

        # Keep only the enabled shoppers 
        if (coverageShop['coverage'] > 0):
            coverageShoppers.append(coverageShop);

        # Sort the array
        coverageShoppersSorted = sorted(coverageShoppers, key=lambda dct: dct['coverage'], reverse=True);

    return coverageShoppersSorted;

# Print the result
shoppersCoverage = coverage(locations,shoppers);
print(shoppersCoverage);