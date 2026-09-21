import inspect
import sys


class __Journal:
    def __init__(self, aspect_ratio=(1 + 5**0.5) / 2):
        self.aspect_ratio = aspect_ratio
        self.pt = 1/72.27
        self.inches_per_mm = 2.54*10


class __MNRAS(__Journal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.onecol = (508.0*self.pt, 508.0*self.pt/self.aspect_ratio)
        self.twocol = (244.0*self.pt, 244.0*self.pt/self.aspect_ratio)
        self.full_page = (508.0*self.pt, 0.9*682.0*self.pt)


class __BOOK(__Journal):
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

        # self.A3 = ((472.0312*2)*self.pt,
        #            (472.0312*2)*self.pt/self.aspect_ratio)

        # self.PortraitA3 = ((692.54008*2)*self.pt/self.aspect_ratio,
        #                    (692.54008*2)*self.pt)

        self.onecol_A4 = ((472.0312 / 2)*self.pt,
                          (472.0312 / 2)*self.pt/self.aspect_ratio)

        self.A4_fullwidth = ((472.0312)*self.pt,
                             (472.0312)*self.pt/self.aspect_ratio)


def get(journal_name, columns=None, **kwargs):
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