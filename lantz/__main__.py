
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

    import argparse

    scs, ers = get_subcommands()

    if ers:
        lines = ('- %s: %s' % (k, v) for k, v in ers.items())
        epilog = '\n'.join(lines)
        epilog = 'Could not load the following subcommands:\n' + epilog
    else:
        epilog = None

    parser = argparse.ArgumentParser(description='Lantz', epilog=epilog, add_help=False)
    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('subcommand',
                        choices=list(scs.keys()),
                        nargs='?')
    args, pending = parser.parse_known_args(args)

    if args.subcommand is None:
        if args.help:
            parser.print_help()
        else:
            parser.print_usage()
    else:
        if args.help:
            pending += ['--help', ]
        scs[args.subcommand](pending)


if __name__ == '__main__':
    main()
