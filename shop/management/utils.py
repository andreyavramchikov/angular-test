from selenium import webdriver


def _get_firefox_profile():
    # # get the Firefox profile object
    firefox_profile = webdriver.FirefoxProfile()
    ## Disable CSS
    firefox_profile.set_preference('permissions.default.stylesheet', 2)
    ## Disable images
    firefox_profile.set_preference('permissions.default.image', 2)
    ## Disable Flash
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',

                                   'false')
    return firefox_profile