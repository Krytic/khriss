"""Print-quality figure dimensions for academic journals and books.

Khriss answers one question: "how big should this figure be, in inches,
so it drops into my journal's column or page without LaTeX rescaling it?"

The public entry point is :func:`get`, which looks up the layout for a
named journal (or book page size) and returns a ``(width, height)`` tuple
suitable for passing directly to Matplotlib's ``figsize``.

Example:
    >>> import khriss
    >>> khriss.get("mnras")
    (7.0291960702919605, 4.3442820850276265)
"""

import inspect
import sys


class __Journal:
    """Base class for a publication's figure-sizing conventions.

    Stores the conversion factors shared by every journal/book layout
    (points to inches, mm to inches) and the default aspect ratio used
    to derive a height from a width when a layout only defines one.

    :param aspect_ratio: The width/height ratio used where a layout
        derives its height from its width. Defaults to the golden
        ratio, ``(1 + 5**0.5) / 2``.
    :type aspect_ratio: float
    """

    def __init__(self, aspect_ratio=(1 + 5**0.5) / 2):
        self.aspect_ratio = aspect_ratio
        self.pt = 1/72.27
        self.inches_per_mm = 2.54*10


class __MNRAS(__Journal):
    """Figure dimensions for Monthly Notices of the Royal Astronomical Society.

    Defines three layouts, each a ``(width, height)`` tuple in inches:

    * ``onecol`` -- a single MNRAS column.
    * ``twocol`` -- the full MNRAS text width (both columns).
    * ``full_page`` -- a full page, sized to 90% of the page height.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.onecol = (508.0*self.pt, 508.0*self.pt/self.aspect_ratio)
        self.twocol = (244.0*self.pt, 244.0*self.pt/self.aspect_ratio)
        self.full_page = (508.0*self.pt, 0.9*682.0*self.pt)


class __PASA(__Journal):
    """Figure dimensions for Publications of the Astronomical Society of Australia.

    Defines the same three layouts as :class:`__MNRAS` (``onecol``,
    ``twocol``, ``full_page``), each a ``(width, height)`` tuple in
    inches, using PASA's own column and page measurements.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.onecol = (514.99507*self.pt, 514.99507*self.pt/self.aspect_ratio)
        self.twocol = (247.79752*self.pt, 247.79752*self.pt/self.aspect_ratio)
        self.full_page = (514.99507*self.pt, 0.9*682.86615*self.pt)


class __BOOK(__Journal):
    """Figure dimensions for generic book pages, including the A-series.

    Defines, for each size in A0-A5:

    * ``A{n}`` / ``Landscape A{n}`` -- landscape page size.
    * ``PortraitA{n}`` -- portrait page size.

    Plus two A4-specific convenience layouts:

    * ``onecol_A4`` -- half the A4 landscape width, for a single column
      on an A4 page.
    * ``A4_fullwidth`` -- the full A4 landscape width.

    Each is a ``(width, height)`` tuple in inches.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for size in range(0, 6):
            landscape = ((472.0312*2**(4-size))*self.pt,
                         (472.0312*2**(4-size))*self.pt/self.aspect_ratio)

            portrait = ((692.54008*2**(4-size))*self.pt/self.aspect_ratio,
                        (692.54008*2**(4-size))*self.pt)

            setattr(self, f"A{size}", landscape)
            setattr(self, f"PortraitA{size}", portrait)
            setattr(self, f"LandscapeA{size}", landscape)

        self.onecol_A4 = ((472.0312 / 2)*self.pt,
                          (472.0312 / 2)*self.pt/self.aspect_ratio)

        self.A4_fullwidth = ((472.0312)*self.pt,
                             (472.0312)*self.pt/self.aspect_ratio)


def get(journal_name, columns=None, **kwargs):
    """Return the figure size, in inches, for a named journal or book layout.

    :param journal_name: Which target's dimensions to use. One of
        ``"mnras"``, ``"pasa"``, or ``"book"`` (case-insensitive).
    :type journal_name: str
    :param columns: Which layout to return for that target. Defaults to
        ``"onecol"``. ``"mnras"`` and ``"pasa"`` support ``"onecol"``,
        ``"twocol"``, and ``"full_page"``. ``"book"`` additionally
        supports ``"A0"``-``"A5"``, ``"PortraitA0"``-``"PortraitA5"``,
        ``"LandscapeA0"``-``"LandscapeA5"``, ``"onecol_A4"``, and
        ``"A4_fullwidth"``.
    :type columns: str, optional
    :param kwargs: Forwarded to the underlying layout's constructor,
        e.g. ``aspect_ratio`` to override the default golden-ratio
        aspect ratio used to derive height from width.
    :returns: A ``(width, height)`` tuple in inches, ready to pass to
        Matplotlib's ``figsize``.
    :rtype: tuple(float, float)
    :raises ValueError: If ``journal_name`` does not match a known
        target.

    Example:
        >>> import khriss
        >>> import matplotlib.pyplot as plt
        >>> width, height = khriss.get("mnras", columns="twocol")
        >>> fig, ax = plt.subplots(figsize=(width, height))
    """
    if columns is None:
        columns = 'onecol'

    internal_name = f"__{journal_name.upper()}"

    # Following line gets all classes defined in this file as long
    # as they start with a __ (two underscores).
    members = inspect.getmembers(sys.modules[__name__])

    classes = [cls_name
               for cls_name, cls_obj in members
               if inspect.isclass(cls_obj) and cls_name[:2] == "__"]

    if internal_name not in classes:
        raise ValueError(f"Journal {journal_name} is not defined.")

    class_instance = getattr(sys.modules[__name__], internal_name)(**kwargs)

    return getattr(class_instance, columns)
