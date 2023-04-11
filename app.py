import geopandas as gpd
from shapely.geometry import box
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

desa = gpd.read_file('static/data.geojson')
bts = gpd.read_file('static/bts.geojson')
uso = gpd.read_file('static/uso.geojson')
sl = gpd.read_file('static/sl.geojson')

@app.route('/desa')
def desaGeojson():
    xmin = float(request.args.get('xmin'))
    ymin = float(request.args.get('ymin'))
    xmax = float(request.args.get('xmax'))
    ymax = float(request.args.get('ymax'))

    bbox = box(xmin, ymin, xmax, ymax)

    filtered_gdf = desa[desa.geometry.intersects(bbox)]

    response_data = filtered_gdf.to_json()
    response = jsonify(response_data)
    response.headers.add('Content-Type', 'application/json')

    return response
@app.route('/bts')
def btsGeojson():
    xmin = float(request.args.get('xmin'))
    ymin = float(request.args.get('ymin'))
    xmax = float(request.args.get('xmax'))
    ymax = float(request.args.get('ymax'))

    bbox = box(xmin, ymin, xmax, ymax)

    filtered_gdf = bts[bts.geometry.intersects(bbox)]

    response_data = filtered_gdf.to_json()
    response = jsonify(response_data)
    response.headers.add('Content-Type', 'application/json')

    return response

@app.route('/uso')
def usoGeojson():
    response_data = uso.to_json()
    response = jsonify(response_data)
    response.headers.add('Content-Type', 'application/json')

    return response

@app.route('/sl')
def slGeojson():
    response_data = sl.to_json()
    response = jsonify(response_data)
    response.headers.add('Content-Type', 'application/json')

    return response

if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')