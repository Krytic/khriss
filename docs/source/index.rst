.. khriss documentation master file, created by
   sphinx-quickstart on Wed Sep 30 13:56:23 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Khriss
======

Khriss is a small Python utility for producing print-quality, correctly-sized
figures for academic papers and books. Instead of guessing a ``figsize`` and
fighting with LaTeX column widths afterwards, you ask Khriss for the exact
dimensions a given journal (or book page) expects, in inches, and hand that
straight to Matplotlib.

Currently supported targets:

* **MNRAS** (Monthly Notices of the Royal Astronomical Society)
* **PASA** (Publications of the Astronomical Society of Australia)
* **Book** layouts, including the A0-A5 series (portrait and landscape) and
  a generic A4 one-column/full-width size

This project is a work in progress: the :doc:`guide` and :doc:`api` below
document what's implemented today, with more journals and features planned.
See the `GitHub repository <https://github.com/Krytic/khriss>`_ for source
and to open issues, including requests for
`new journals <https://github.com/Krytic/khriss/issues/new?template=new-journal.md>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   guide
   luxe
   api
