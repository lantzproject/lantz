
import pkg_resources

def get_subcommands():
    sc = {}
    for entry_point in pkg_resources.iter_entry_points('lantz_subcommands'):
        sc[entry_point.name] = entry_point.load()
    return sc


def main(args=None):
    """Dispatch to sub commands
    """

    import argparse

    scs = get_subcommands()

    parser = argparse.ArgumentParser(description='Lantz')
    parser.add_argument('subcommand', choices=list(scs.keys()))
    args, pending = parser.parse_known_args(args)

    scs[args.subcommand](pending)


if __name__ == '__main__':
    main()
