

import sys

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from lantz.core import Driver, MessageBasedDriver
from lantz.core.foreign import LibraryDriver
from lantz.core import Feat, DictFeat, Action
from lantz.core import ureg, Q_

from lantz.core import initialize_many, finalize_many
from lantz.core.flock import Flock
from lantz.core.processors import DimensionalityWarning

from lantz.core import errors, log, messagebased, driver, processors
sys.modules['lantz.log'] = log
sys.modules['lantz.errors'] = errors
sys.modules['lantz.messagebased'] = messagebased
sys.modules['lantz.driver'] = driver
sys.modules['lantz.processors'] = processors


import argparse


class ArgumentParserSC(argparse.ArgumentParser):

    def __init__(self, required_name, required_choices, *args, **kwargs):
        super().__init__(*args, add_help=False, **kwargs)

        self.add_argument('-h', '--help', action='store_true')

        self.add_argument(required_name,
                          choices=list(required_choices.keys()),
                          nargs='?')

        self.__required_name = required_name
        self.__choices = required_choices

    def dispatch(self, args):
        args, pending = self.parse_known_args(args)

        required_value = getattr(args, self.__required_name)

        if required_value is None:
            if args.help:
                self.print_help()
                self.exit()
            else:
                self.error('%s is a required argument' % self.__required_name)
        else:
            if args.help:
                pending += ['--help', ]

            self.__choices[required_value](pending)
