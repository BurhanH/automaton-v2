import unittest
from selenium import webdriver

WAIT_IMPL = 10
WINDOW_SIZE = 1280, 1024
BROWSER = 'firefox'


class TestBrowser(unittest.TestCase):
    """
    This test suite for browser testing.
    """
    def setUp(self):
        """
        Initiate driver for each test
        """
        if BROWSER == 'chrome':
            self.driver = webdriver.Chrome()
        if BROWSER == 'firefox':
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(WAIT_IMPL)
        self.driver.set_window_size(WINDOW_SIZE[0], WINDOW_SIZE[1])

    def _set_and_verify(self, set_width, set_height) -> None:
        """ Common method to set browser resolution and verify it.

        Args:
            set_width (int): width of a browser window
            set_height (int): height of a browser window

        Returns:
            None

        Rises:
            AssertionError
        """
        self.driver.set_window_size(set_width, set_height)
        resolution = self.driver.get_window_size()
        width = resolution.get('width')
        height = resolution.get('height')

        errors = []

        if width != set_width:
            errors.append(u'Width is {} expecting {}'.format(width, set_width))
        if height != set_height:
            errors.append(u'Height is {} expecting {}'.format(height, set_height))

        error_msgs = '\n'.join(errors)

        if errors:
            raise AssertionError(error_msgs)

    def test_resolution_1(self):
        """
        Testing resolution 800, 600
        """
        self._set_and_verify(800, 600)

    def test_resolution_2(self):
        """
        Testing resolution 1280, 1024
        """
        self._set_and_verify(1280, 1024)

    def test_resolution_3(self):
        """
        Testing resolution 1600, 1200
        """
        self._set_and_verify(1600, 1200)

    def test_resolution_4(self):
        """
        Testing resolution 1680, 1050
        """
        self._set_and_verify(1680, 1050)

    def test_resolution_5(self):
        """
        Testing resolution 1900, 1200
        """
        self._set_and_verify(1900, 1200)

    def test_search_in_google(self):
        """
        Testing search in Google
        """
        # Going to google.com
        self.driver.get('https://www.google.com')
        # Searching for the input field by name and entering data
        search = self.driver.find_element_by_name('q')
        search.is_displayed()
        search.send_keys('python')
        # Searching and waiting the search drop-down menu
        menu = self.driver.find_element_by_css_selector('.FPdoLc.VlcLAe')
        menu.is_displayed()
        # Clicking Google Search button
        search_btn = self.driver.find_element_by_css_selector("input[name='btnK']")
        search_btn.is_displayed()
        search_btn.is_enabled()
        search_btn.click()
        # Verifying search results
        self.assertTrue(
            self.driver.find_element_by_css_selector('.bNg8Rb').is_displayed(),
            "Unable to find results on a page!"
        )

    def tearDown(self):
        """
        Closing driver after each test
        """
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
