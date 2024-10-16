"""JS/CSS Webpack bundles for Neon Green."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "leaflet_js": "./js/neon_green/leaflet.js",
                "leaflet_css": "./css/neon_green/leaflet.css"
            },
            dependencies={
                "leaflet": "^1.9.4",
                "leaflet-gpx": "^2.1.2"
            }
        ),
    },
)
