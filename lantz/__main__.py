
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
        epilog = '\n'.join(('- %s: %s' % k, v for k, v in ers.items()))
    else:
        epilog = None

    parser = argparse.ArgumentParser(description='Lantz', epilog=epilog)
    parser.add_argument('subcommand',
                        choices=list(scs.keys()))
    args, pending = parser.parse_known_args(args)

    scs[args.subcommand](pending)


if __name__ == '__main__':
    main()
