User Guide
==========

Installation
------------

Prerequisites
~~~~~~~~~~~~~

For best results, install a TeX distribution (TeXLive is recommended) and
the CMU fonts, so that figures rendered with LaTeX text match your
document:

.. code-block:: bash

   sudo apt install texlive
   sudo apt install fonts-cmu

From PyPI
~~~~~~~~~

Once published, Khriss will be installable from PyPI:

.. code-block:: bash

   pip install khriss

Until then, install it directly from GitHub:

.. code-block:: bash

   pip install git+https://github.com/Krytic/khriss.git

Basic usage
-----------

:func:`khriss.get` returns a ``(width, height)`` tuple in inches, ready to
pass to Matplotlib's ``figsize``:

.. code-block:: python

   import matplotlib.pyplot as plt
   import khriss

   # A one-column MNRAS figure
   figsize = khriss.get("mnras")

   fig, ax = plt.subplots(figsize=figsize)
   ax.plot([0, 1, 2], [0, 1, 4])
   ax.set_xlabel("x")
   ax.set_ylabel("y")

   fig.savefig("figure.pdf")

The figure is sized so that it can be dropped in to a manuscript and natively
produce a figure sized so that the axis labels and ticks are the same size as
the body text.

Choosing a layout
-----------------

Every target supports more than one layout, selected with the ``columns``
argument. For ``"mnras"`` and ``"pasa"``:

.. code-block:: python

   onecol = khriss.get("mnras")                  # default
   twocol = khriss.get("mnras", columns="twocol")
   full   = khriss.get("mnras", columns="full_page")

The same three layouts (``onecol``, ``twocol``, ``full_page``) are
available for ``"pasa"``.

You should choose the layout that makes sense for your use case. The names
are chosen as follows:

* :code:`onecol` should be used when you are generating a figure to occupy one
  column in a two-column document.
* :code:`twocol` should be used when you are generating a figure to occupy BOTH
  columns in a two-column document.
* :code:`full_page` should be used when you are generating a figure to occupy the
  entire page.

Book and page sizes
--------------------

The ``"book"`` target instead exposes the A-series page sizes, in both
orientations, plus two A4-specific convenience layouts:

.. code-block:: python

   khriss.get("book", columns="A4")               # landscape A4 (default orientation)
   khriss.get("book", columns="PortraitA4")
   khriss.get("book", columns="LandscapeA4")
   khriss.get("book", columns="onecol_A4")         # half the A4 landscape width
   khriss.get("book", columns="A4_fullwidth")      # full A4 landscape width

Sizes are defined for ``A0`` through ``A5``.

Overriding the aspect ratio
----------------------------

Every layout that derives a height from a width does so using an aspect
ratio, which defaults to the golden ratio. Pass ``aspect_ratio`` as a
keyword argument to override it for a single call:

.. code-block:: python

   # A squarer MNRAS one-column figure
   khriss.get("mnras", aspect_ratio=1.0)

See :doc:`api` for the full parameter and layout reference.
