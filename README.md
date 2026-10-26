# Microplastics map and particle visualization

This fork of [vasu-era/nanoparicle_simulation](https://github.com/vasu-era/nanoparicle_simulation) preserves the upstream Flask/Folium map, CSV datasets and a desktop particle visualization. Upstream authorship remains with its contributors; this fork's setup corrections do not make the simulation original work by the fork owner. No new license is assigned.

## View the saved map

With Python 3.11+ in an activated virtual environment:

```sh
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000/. Flask serves `templates/microplastics_map.html`, a pre-generated Folium visualization. Map tiles and JavaScript dependencies require internet access. The web route does not run the desktop simulation. On a Linux host the existing `Procfile` starts `gunicorn app:app`; no deployed URL is asserted here.

## Optional desktop path

```sh
python -m pip install -r requirements-desktop.txt
python "integration_app .py"
```

The filename really contains a space before `.py`. This entry point reads the included CSVs, generates a separate root-level HTML map, opens a PyWebview window and launches `depth_modified.py` on map clicks. It requires a supported desktop webview runtime and graphical display. Run from the repository root. `depth_modified.py` can also run directly with optional latitude/longitude arguments.

`Microplastics_Clean_Essential.csv` contains sample locations, measurements, depth and color labels; `geocoded_500_successful.csv` provides industrial locations. Their original provenance, reuse terms and calibration are not established by this fork. Keep upstream data and attribution intact.

## Verify and interpret

Install `pytest`, then run `python -m pytest -q`. The test verifies that Flask serves the existing Leaflet map. Desktop rendering and external map tiles are separate checks. The stylized currents and toxicity colors are illustrative heuristics, not a validated environmental transport or exposure model. Historical logs and generated map assets remain preserved.

Standard-library modules such as `sys`, `math`, `pathlib` and `subprocess` are supplied by Python; they are no longer listed as packages to install. Desktop dependencies are optional so the web server can install without them.
