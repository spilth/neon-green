# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2021 Northwestern University.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""GPX rendering."""

from flask import render_template

from invenio_previewer.proxies import current_previewer

previewable_extensions = ["gpx"]


def can_preview(file):
    """Check if file can be previewed."""
    return file.is_local() and file.has_extensions(".gpx")


def preview(file):
    """Render Markdown."""
    return render_template(
        "neon_green/gpx.html",
        file=file,
        js_bundles=current_previewer.js_bundles,
        css_bundles=current_previewer.css_bundles,
    )
