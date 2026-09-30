API Reference
=============

.. currentmodule:: khriss

This page documents Khriss's public API: the single function
``khriss.get()``. Everything else in the ``khriss`` package (the journal
classes it uses internally) is a private implementation detail and may
change without notice.

khriss.get
----------

.. py:function:: get(journal_name, columns=None, **kwargs)

   Return the figure size, in inches, for a named journal or book layout.

   :param journal_name: Which target's dimensions to use. One of
      ``"mnras"``, ``"pasa"``, or ``"book"`` (case-insensitive).
   :type journal_name: str
   :param columns: Which layout to return for that target. Defaults to
      ``"onecol"``. See `Supported layouts`_ below for the valid values
      per target.
   :type columns: str, optional
   :param kwargs: Forwarded to the underlying layout's constructor.
      Currently the only recognised keyword is ``aspect_ratio``, which
      overrides the default golden-ratio aspect ratio
      (``(1 + 5 ** 0.5) / 2``) used to derive a height from a width.
   :type kwargs: float
   :returns: A ``(width, height)`` tuple in inches, ready to pass to
      Matplotlib's ``figsize``.
   :rtype: tuple(float, float)
   :raises ValueError: If ``journal_name`` does not match a known target.

   .. code-block:: python

      >>> import khriss
      >>> khriss.get("mnras")
      (7.0291960702919605, 4.3442820850276265)
      >>> khriss.get("mnras", columns="twocol")
      (3.3762280337622803, 2.0866236786353167)

Supported layouts
------------------

``"mnras"`` and ``"pasa"``
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20

   * - ``columns``
     - MNRAS (in)
     - PASA (in)
     - Notes
   * - ``onecol`` (default)
     - 7.029 x 4.344
     - 7.126 x 4.404
     - A single column
   * - ``twocol``
     - 3.376 x 2.087
     - 3.429 x 2.119
     - The full text width
   * - ``full_page``
     - 7.029 x 8.493
     - 7.126 x 8.504
     - A full page, 90% of the page height

``"book"``
~~~~~~~~~~

Defined for each size ``0``-``5`` (A0 is the largest, A5 the smallest).
The table below shows A0-A5; substitute the size you need.

.. list-table::
   :header-rows: 1
   :widths: 25 25 25

   * - ``columns``
     - Landscape (in)
     - Portrait (in)
   * - ``A0`` / ``LandscapeA0``
     - 104.504 x 64.587
     - --
   * - ``PortraitA0``
     - --
     - 94.759 x 153.323
   * - ``A1`` / ``LandscapeA1``
     - 52.252 x 32.293
     - --
   * - ``PortraitA1``
     - --
     - 47.379 x 76.661
   * - ``A2`` / ``LandscapeA2``
     - 26.126 x 16.147
     - --
   * - ``PortraitA2``
     - --
     - 23.690 x 38.331
   * - ``A3`` / ``LandscapeA3``
     - 13.063 x 8.073
     - --
   * - ``PortraitA3``
     - --
     - 11.845 x 19.165
   * - ``A4`` / ``LandscapeA4``
     - 6.531 x 4.037
     - --
   * - ``PortraitA4``
     - --
     - 5.922 x 9.583
   * - ``A5`` / ``LandscapeA5``
     - 3.266 x 2.018
     - --
   * - ``PortraitA5``
     - --
     - 2.961 x 4.791

Two additional convenience layouts are defined for ``"book"``:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - ``columns``
     - Size (in)
     - Equivalent to
   * - ``onecol_A4``
     - 3.266 x 2.018
     - Half the A4 landscape width; identical to ``A5``
   * - ``A4_fullwidth``
     - 6.531 x 4.037
     - The full A4 landscape width; identical to ``A4``

.. note::

   All dimensions above use the default golden-ratio aspect ratio. Pass
   ``aspect_ratio=...`` to :py:func:`get` to change the height for any
   layout that derives it from a width (every layout except
   ``full_page``, which uses a fixed page fraction instead).

Exceptions
----------

.. py:exception:: ValueError

   Raised by :py:func:`get` when ``journal_name`` does not match a known
   target (``"mnras"``, ``"pasa"``, or ``"book"``).
