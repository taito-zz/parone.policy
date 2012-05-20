from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-parone.policy:default'


def upgrade_0_to_1(context, logger=None):
    """Reinstall addons."""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(__name__)

    installer = getToolByName(context, 'portal_quickinstaller')
    products = [
        'LinguaPlone',
        'collective.contentleadimage',
        'parone.theme',
    ]
    logger.info('Reinstalling products.')
    installer.reinstallProducts(products)
    logger.info('Reinstalled products.')
