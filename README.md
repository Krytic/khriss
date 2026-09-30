# Khriss

Khriss is a small Python utility for producing print-quality, correctly-sized figures for academic papers and books. Instead of guessing a `figsize` and fighting with LaTeX column widths afterwards, you ask Khriss for the exact dimensions a given journal (or book page) expects, in inches, and hand that straight to Matplotlib.

Currently supported targets:

- **MNRAS** (Monthly Notices of the Royal Astronomical Society)
- **PASA** (Publications of the Astronomical Society of Australia)
- **Book** layouts, including the A0–A5 series (portrait and landscape) and a generic A4 one-column/full-width size

This project is a work in progress — the API below is what's implemented today, with more journals and features planned.

## Installation

### Prerequisites

For best performance, you should install a TeX distribution (we recommend TeXLive) and the CMU fonts:

```bash
sudo apt install texlive
sudo apt install fonts-cmu
```

### From PyPI

Once published, Khriss will be installable from PyPI:

```bash
pip install khriss
```

Until then, you can install it directly from GitHub:

```bash
pip install git+https://github.com/Krytic/khriss.git
```

## Usage

`khriss.get()` returns a `(width, height)` tuple in inches, ready to pass to Matplotlib's `figsize`:

```python
import matplotlib.pyplot as plt
import khriss

# A one-column MNRAS figure
figsize = khriss.get("mnras")

fig, ax = plt.subplots(figsize=figsize)
ax.plot([0, 1, 2], [0, 1, 4])
ax.set_xlabel("x")
ax.set_ylabel("y")

fig.savefig("figure.pdf", bbox_inches="tight")
```

Two-column and full-page variants are available via the `columns` argument:

```python
onecol = khriss.get("mnras")                  # default
twocol = khriss.get("mnras", columns="twocol")
full   = khriss.get("mnras", columns="full_page")
```

The same pattern works for `"pasa"`. The `"book"` target additionally exposes the A-series page sizes:

```python
khriss.get("book", columns="A4")               # landscape A4
khriss.get("book", columns="PortraitA4")
khriss.get("book", columns="LandscapeA4")
khriss.get("book", columns="onecol_A4")
khriss.get("book", columns="A4_fullwidth")
```

Sizes are available for `A0` through `A5`.

### API

```python
khriss.get(journal_name, columns=None, **kwargs)
```

- **`journal_name`** (`str`) — one of `"mnras"`, `"pasa"`, or `"book"` (case-insensitive).
- **`columns`** (`str`, optional) — which layout to return. Defaults to `"onecol"`. Valid values depend on `journal_name`; see above.
- **`**kwargs`** — forwarded to the underlying layout, e.g. `aspect_ratio` to override the default golden-ratio aspect ratio used to compute heights from widths.

Raises `ValueError` if `journal_name` isn't recognized.

### Re

## Requirements

- Python >= 3.11

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

If Khriss is useful in your research, please consider citing it:

```bibtex
@software{khriss,
  author  = {Richards, Sean M.},
  title   = {Khriss: print-quality figures in Python},
  url     = {https://github.com/Krytic/khriss},
  version = {1.0.0a},
}
```

_(A DOI / Zenodo archive will be added here once one exists.)_

## License

Khriss is released under the [MIT License](LICENSE).