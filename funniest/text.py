from markdown import markdown

try:
    import importlib.resources as importlib_resources
except ImportError:
    # In PY<3.7 fall-back to backported `importlib_resources`.
    import importlib_resources


def joke():
    return markdown(
        "Wenn ist das Nunst\u00fcck git und Slotermeyer?"
        "Ja! ... **Beiherhund** das Oder die Flipperwaldt "
        "gersput."
    )


def print_raw():
    import os

    cur = os.path.dirname(os.path.abspath(__file__))
    print(cur)

    with importlib_resources.open_text(
        package="funniest.data", resource="raw.txt"
    ) as fr:
        for line in fr:
            print(line.strip())
