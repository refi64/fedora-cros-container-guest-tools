import dnf
import dnf.cli
from dnfpluginscore import logger

class GarconTrigger(dnf.Plugin):
    name = 'garcon-trigger'

    def transaction(self):
        logger.debug('Triggering garcon...')
        with open('/usr/share/applications/.garcon_trigger', 'w') as fp:
            pass
