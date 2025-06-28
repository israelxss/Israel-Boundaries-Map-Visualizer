Israel Geographical Map Visualizer (Extended)
---------------------------------------------

This project offers a straightforward, yet powerful, way to visualize the geographical boundaries of **Israel, including areas under Israeli security control and the Gaza Strip**, on an interactive web map. After extensive searching for convenient tools, I decided to build my own solution to simplify the process of displaying these complex geographical polygons.

Project Overview
----------------

This repository contains the necessary files to display detailed geographical polygons on a simple web map. It addresses the common challenge of easily rendering complex GeoJSON data for map visualization, now with an added layer for areas under Israeli security control.

The core components are:

*   **export.geojson**: The raw geographical data for Israel and the Gaza Strip in GeoJSON format.
    
*   **convert.py**: A Python script that transforms the GeoJSON data from both export.geojson and security\_control\_areas.geojson into a simplified text file.
    
*   **polygon\_coordinates.txt**: The output of convert.py, containing just the raw latitude and longitude coordinates for all combined areas.
    
*   **index.html**: The web page that loads and displays the map using the data from polygon\_coordinates.txt, potentially using different styling for the various regions.
    

Files in This Repository
------------------------

Here's a breakdown of the files you'll find and their roles:

*   **convert.py**: This Python script is the workhorse for data transformation. It parses export.geojson and (now) security\_control\_areas.geojson to create polygon\_coordinates.txt.
    
*   **export.geojson**: This file holds the comprehensive geographic data, including boundaries for Israel and the Gaza Strip, sourced from OpenStreetMap.
    
*   **security\_control\_areas.geojson**: This **new file** contains the geographical data specifically for areas under Israeli security control. You'll need to obtain or generate this file.
    
*   **index.html**: This is your map! It's a simple HTML file that uses JavaScript to read polygon\_coordinates.txt and render the polygons on an interactive map. You'll likely need to adjust this file to differentiate between the various types of polygons (e.g., using different colors).
    

Generating GeoJSON Data
-----------------------

The export.geojson file was generated with the help of **Overpass Turbo** ([https://overpass-turbo.eu/](https://overpass-turbo.eu/)), a powerful web-based data mining tool for OpenStreetMap. I used the following Overpass Query to extract the relevant geographical data for Israel and Gaza:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   [out:json][timeout:25];  relation(6195356); // This ID typically refers to Israel's borders as a whole  out geom;   `

**For security\_control\_areas.geojson**, you will need to find the appropriate OpenStreetMap relation IDs or draw the polygons yourself on Overpass Turbo. For example, for **Area C in the West Bank**, you might need to search for specific relations or combine several smaller ones. This part might require some research and experimentation on Overpass Turbo to accurately capture the desired areas.

Getting Started
---------------

To view the interactive map, follow these simple steps:

1.  **Ensure you have Python installed** on your system.
    
2.  **Clone this repository** to your local machine.
    
3.  **Obtain or generate security\_control\_areas.geojson** and place it in the project directory.
    
4.  **Run convert.py** to process both GeoJSON files and update polygon\_coordinates.txt.
    
5.  **Navigate to the project directory** in your terminal or command prompt.
    
6.  Bash `python -m http.server 8080`
    
7.  **Open your web browser** and go to http://localhost:8080/index.html.
    

You should now see the map displayed in your browser, showcasing the boundaries of Israel and the areas under Israeli security control.
