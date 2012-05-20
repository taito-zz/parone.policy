from Products.CMFCore.utils import getToolByName
from parone.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone upgrades."""

    def setUp(self):
        self.portal = self.layer['portal']
        from plone.app.testing import TEST_USER_ID
        from plone.app.testing import setRoles
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_upgrades_0_to_1(self):

        from parone.policy.upgrades import upgrade_0_to_1
        upgrade_0_to_1(self.portal)
