"""Monkey-patching autosummary to emit the autosummary-gather-context event."""
from __future__ import annotations

from inspect import signature
from typing import TYPE_CHECKING

from sphinx.errors import ExtensionError
from sphinx.ext.autosummary.generate import (
    generate_autosummary_content,
    generate_autosummary_docs,
)

if TYPE_CHECKING:
    from sphinx.application import Sphinx

GENERATE_SIGNATURE = signature(generate_autosummary_content)


def generate_autosummary_content_with_context(*args: object, **kwargs: object) -> str:
    """Wrap generate_autosummary_content to emit autosummary-gather-context."""
    ba = GENERATE_SIGNATURE.bind_partial(*args, **kwargs)
    app = ba.arguments["app"]
    if app:
        name = ba.arguments["name"]
        obj = ba.arguments["obj"]
        parent = ba.arguments["parent"]
        context = ba.arguments["context"]
        results = app.emit("autosummary-gather-context", name, obj, parent, context)
        for extra_context in results:
            if extra_context:
                context.update(extra_context)
    return generate_autosummary_content(*args, **kwargs)  # type: ignore[arg-type]


def setup(app: Sphinx) -> None:
    """Monkey-patch the autosummary-gather-context event if not present."""
    # try connecting a mock callback to autosummary-gather-context
    try:
        listener_id = app.connect("autosummary-gather-context", lambda: None)
    except ExtensionError:
        listener_id = None

    if listener_id is not None:
        # event exists, all good
        app.disconnect(listener_id)
    else:
        # patch generate_autosummary_docs to call the wrapper above
        generate_autosummary_docs.__globals__[
            "generate_autosummary_content"
        ] = generate_autosummary_content_with_context

        # register the new event
        app.add_event("autosummary-gather-context")
