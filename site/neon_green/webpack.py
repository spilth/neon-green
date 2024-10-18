"""JS/CSS Webpack bundles for Neon Green."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "gpx_js": "./js/neon_green/gpx.js",
                "gpx_css": "./css/neon_green/gpx.css"
            },
            dependencies={
                "leaflet": "^1.9.4",
                "leaflet-gpx": "^2.1.2"
            }
        ),
    },
)
