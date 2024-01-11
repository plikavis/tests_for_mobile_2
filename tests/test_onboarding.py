from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search(mobile_management, skip_onboarding):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))
    with step('Go to back'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton')).click()

def test_hide_news(mobile_management, skip_onboarding):
    with step('Check title "Featured article"'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/view_card_header_title")).first.should(have.text('Featured article'))
    with step('Open menu'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/view_list_card_header_menu")).first.click()
    with step('Hide card'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/title")).first.click()
    with step('Check new title "Top read"'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/view_card_header_title")).first.should(have.text('Top read'))
def test_open_article(mobile_management, skip_onboarding):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Selene')
    with step('Open article'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()
    with (step('Verify content opened')):
        browser.element((AppiumBy.XPATH, '(//android.widget.TextView[@text="Selene"])[1]')).should(have.text('Selene'))
    with step('Go to back'):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton')).click().click()


def test_onboarding(mobile_management):
    with (step('First screen')):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/secondaryTextView")
                        ).should(have.text('We’ve found the following on your device:'))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
    with step('Second screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('New ways to explore'))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
    with step('Third screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Reading lists with sync'))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
    with step('Forth screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Send anonymous data'))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/acceptButton")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/main_toolbar_wordmark")
                        ).should(be.visible)
