# GeoSearch Input Tool

## Features

The GeoSearch Input Tool is intended to be used as part of a larger model, as it allows the user to input an address that is converted to a geometry object.
1. Takes a specified address as input.
2. Issues a geocoding request to the Esri World Geocoding Service and captures the response.
3. Parces, processes, and creates point geometry representing the best match to the input address. 

The output is an ArcGIS Feature Layer sourced by an in-memory feature class that can be used as input to other ArcGIS geoprocessing functions.

## Instructions

1. Download the package.
2. Using ArcCatalog or ArcMap, browse to Toolbox.tbx and double-click on Input Address to launch the tool.
3. The tool is already configured and should require no additional changes. It can be used within a larger model, if desired, and published to a geoprocessing service. See the *BufferModel* model in the Toolbox for an example.

## Requirements

* ArcGIS Desktop 10.2 or higher

## Issues

If you find a bug or think of a new feature you'd like to see, please let be know by submitting an issue.

## Contributing

I follow the Esri Github guidelines for contributing. Please see [guidelines for contributing](https://github.com/esri/contributing).

## Licensing

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at


   http://www.apache.org/licenses/LICENSE-2.0


Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


A copy of the license is available in the repository.