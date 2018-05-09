"""
city_builder

Usage:
    city_builder roadmap
    city_builder polygons
    city_builder buildings
    city_builder -h | --help
    city_builder --version

Options:
    -h --help       Show this screen
    --version       Show version

Examples:
    city_builder roadmap

Help:
    For help using this tool, please open an issue on the Github repository:
    https://github.com/augustoerico/city-builder-cli
"""

from docopt import docopt

from city_builder import __version__


def main():
    from city_builder.commands import roadmap, polygons, buildings

    options = docopt(__doc__, version=__version__)

    for k, v in options.items():
        if v:
            if k == 'roadmap':
                roadmap.Roadmap(options).run()
            elif k == 'polygons':
                polygons.Polygons(options).run()
            elif k == 'buildings':
                buildings.Buildings(options).run()


if __name__ == '__main__':
    main()
