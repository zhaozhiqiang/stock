import optparse
from hu_shen_gang_tong import HuShenGangTong


class Command(object):
    '''Base class for any command line action in stock.
    '''

    common = False
    _optparse = None

    def wantPager(self, _opt):
        return False

    @property
    def optionParser(self):
        if self._optparse is None:
            try:
                me = 'stock %s' % self.NAME
                usage = self.helpUsage.strip().replace('%prog', me)
            except AttributeError:
                usage = 'stock %s' % self.NAME

            self._optparse = optparse.OptionParser(usage=usage)
            self._optparse(self._optparse)
        return self._optparse

    def _options(self, p):
        '''Initialize the option parser.
        '''

    def usage(self):
        '''Display usage and terminate.
        '''
        self.optionParser.print_usage()
        sys.exit(1)

    def execute(self, opt, args):
        '''Perform the action, after option parsing is complete
        '''
        raise NotImplementedError


class InteractiveCommand(Command):
    ''' Command which requires user interaction on the tty and
        must not run within a pager, even if the user asks to.
    '''
    def wantPager(self, _opt):
        return False


class PagedCommand(Command):
    ''' Command which defaults to output in a pager, as its
        display tends to be larger than one screen full.
    '''
    def wantPager(self, _opt):
        return True


class MirrorCommand(Command):
    ''' Command permits itself to run within a mirror,
        and does not require a working directory.
    '''


class CommandHSG(Command):

    def __init__(self):
        self.tasks = []
        self.tasks.append(HuShenGangTong('hgt'))
        self.tasks.append(HuShenGangTong('sgt'))

    def execute(self):
        pass