import json

def extract_polygon_coordinates_to_file(geojson_file_path, output_file_path):
    """
    Extracts polygon coordinates from a GeoJSON file and saves them to a text file.
    Coordinates are saved in the format: latitude,longitude (e.g., 31.9600,34.8000).
    Only coordinates from Polygon and MultiPolygon geometries are extracted.
    """
    try:
        with open(geojson_file_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        all_polygon_coords = []

        def process_geometry_recursively(geometry_object):
            # Check if the geometry_object itself is None
            if geometry_object is None:
                return

            # Check if 'type' and 'coordinates' keys exist
            geom_type = geometry_object.get("type")
            coordinates = geometry_object.get("coordinates")

            if geom_type is None:
                # This might be a FeatureCollection or GeometryCollection at this level
                if "features" in geometry_object:
                    for feature in geometry_object["features"]:
                        if "geometry" in feature:
                            process_geometry_recursively(feature["geometry"])
                elif "geometries" in geometry_object:
                    for geom in geometry_object["geometries"]:
                        process_geometry_recursively(geom)
                return

            # Now proceed with handling specific geometry types if coordinates exist
            if coordinates is None:
                print(f"Warning: Geometry of type '{geom_type}' has no 'coordinates'. Skipping.")
                return

            if geom_type == "Polygon":
                for ring in coordinates:
                    for coord_pair in ring:
                        # GeoJSON is [longitude, latitude], output needs to be latitude,longitude
                        all_polygon_coords.append(f"{coord_pair[1]},{coord_pair[0]}")
            elif geom_type == "MultiPolygon":
                for polygon in coordinates:
                    for ring in polygon:
                        for coord_pair in ring:
                            # GeoJSON is [longitude, latitude], output needs to be latitude,longitude
                            all_polygon_coords.append(f"{coord_pair[1]},{coord_pair[0]}")
            elif geom_type == "GeometryCollection":
                # Recursively process geometries within a GeometryCollection
                for geom in coordinates: # In GeometryCollection, 'coordinates' holds the list of geometries
                    process_geometry_recursively(geom)
            # Add other geometry types here if you want to extract their coords,
            # but for polygon_coordinates.txt, we only focus on polygons.
            elif geom_type in ["Point", "LineString", "MultiPoint", "MultiLineString"]:
                # Optionally, you can add a print statement if you encounter other types
                # that you explicitly want to ignore for this specific output.
                # print(f"Info: Skipping geometry type '{geom_type}' as it's not a Polygon.")
                pass
            else:
                print(f"Warning: Unhandled geometry type '{geom_type}' encountered.")

        # Start processing from the top level of the GeoJSON data
        if "features" in geojson_data:
            for feature in geojson_data["features"]:
                if "geometry" in feature:
                    process_geometry_recursively(feature["geometry"])
                else:
                    print("Warning: Feature found without a 'geometry' key. Skipping.")
        elif "geometry" in geojson_data:
            process_geometry_recursively(geojson_data["geometry"])
        else:
            print("Unsupported GeoJSON structure. Expected 'features' or 'geometry' at top level.")
            return

        # Write extracted coordinates to the output file
        if all_polygon_coords:
            with open(output_file_path, 'w', encoding='utf-8') as outfile:
                for coord_str in all_polygon_coords:
                    outfile.write(coord_str + '\n')
            print(f"Successfully extracted polygon coordinates to {output_file_path}")
        else:
            print("No polygon coordinates were found in the GeoJSON file.")


    except FileNotFoundError:
        print(f"Error: GeoJSON file not found at {geojson_file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {geojson_file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage example:
geojson_input_file = 'export.geojson'
output_txt_file = 'polygon_coordinates.txt'
extract_polygon_coordinates_to_file(geojson_input_file, output_txt_file)