
import pkg_resources

def get_subcommands():
    sc = {}
    er = {}
    for entry_point in pkg_resources.iter_entry_points('lantz_subcommands'):
        try:
            sc[entry_point.name] = entry_point.load()
        except Exception as e:
            er[entry_point.name] = str(e)

    return sc, er


def main(args=None):
    """Dispatch to sub commands
    """

    from . import ArgumentParserSC

    scs, ers = get_subcommands()

    if ers:
        lines = ('- %s: %s' % (k, v) for k, v in ers.items())
        epilog = '\n'.join(lines)
        epilog = 'Could not load the following subcommands:\n' + epilog
    else:
        epilog = None

    parser = ArgumentParserSC('subcommand', scs, description='Lantz', epilog=epilog)

    parser.dispatch(args)


if __name__ == '__main__':
    main()
