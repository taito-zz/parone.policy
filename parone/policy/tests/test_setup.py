from Products.CMFCore.utils import getToolByName
from parone.policy.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_parone_policy_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('parone.policy'))

    def test_parone_theme_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('parone.theme'))

    def test_collective_contentleadimage_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.contentleadimage'))

    def test_LinguaPlone_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('LinguaPlone'))

    def test_theme_installed(self):
        skins = getToolByName(self.portal, 'portal_skins')
        layer = skins.getSkinPath('Parone Theme')
        self.failUnless('parone_theme_custom_templates' in layer)
        self.assertEquals('Parone Theme', skins.getDefaultSkin())

    ## language
    def test_available_languages(self):
        languages = getToolByName(self.portal, 'portal_languages')
        self.assertEquals('fi', languages.getDefaultLanguage())
        self.assertEqual([('en', u'English'), ('fi', u'Finnish')], languages.listSupportedLanguages())

    def test_default_language(self):
        portal_properties = getToolByName(self.portal, 'portal_properties')
        site_properties = portal_properties.get('site_properties')
        self.assertEquals('fi', site_properties.getProperty('default_language'))

    ## portal_languages.xml
    def test_use_content_negotiation(self):
        languages = getToolByName(self.portal, 'portal_languages')
        self.failUnless(not languages.use_content_negotiation)
