import geopandas as gpd
from shapely.geometry import box
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

# Load the GeoJSON data into a GeoDataFrame
desa = gpd.read_file('static/data.geojson')
bts = gpd.read_file('static/bts.geojson')
# uso = gdp.read_file('static/uso.geojson')

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/desa')
# @cross_origin()
def desaGeojson():
    # Parse the bounding box coordinates from the request query parameters
    xmin = float(request.args.get('xmin'))
    ymin = float(request.args.get('ymin'))
    xmax = float(request.args.get('xmax'))
    ymax = float(request.args.get('ymax'))

    # Create a bounding box geometry from the coordinates
    bbox = box(xmin, ymin, xmax, ymax)

    # Filter the GeoDataFrame to select only features that intersect with the bounding box
    filtered_gdf = desa[desa.geometry.intersects(bbox)]

    # Convert the filtered GeoDataFrame to GeoJSON format and return it as a response
    response_data = filtered_gdf.to_json()
    response = jsonify(response_data)
    response.headers.add('Content-Type', 'application/json')

    return response
@app.route('/bts')
# @cross_origin()
def btsGeojson():
    # Parse the bounding box coordinates from the request query parameters
    xmin = float(request.args.get('xmin'))
    ymin = float(request.args.get('ymin'))
    xmax = float(request.args.get('xmax'))
    ymax = float(request.args.get('ymax'))

    # Create a bounding box geometry from the coordinates
    bbox = box(xmin, ymin, xmax, ymax)

    # Filter the GeoDataFrame to select only features that intersect with the bounding box
    filtered_gdf = bts[bts.geometry.intersects(bbox)]

    # Convert the filtered GeoDataFrame to GeoJSON format and return it as a response
    response_data = filtered_gdf.to_json()
    response = jsonify(response_data)
    response.headers.add('Content-Type', 'application/json')

    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')