import pytest
from selene import browser, be, have


@pytest.fixture(scope='session')
def config_browser():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    yield
    browser.quit()


@pytest.fixture(scope='function')
def open_url_yandex():
    browser.open('https://ya.ru')


def test_yandex_find_result_success(config_browser, open_url_yandex):
    browser.element('#text').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('.organic__title').should(have.text('GitHub - yashaka/selene: User-oriented Web UI browser...'))


def test_yandex_find_result_unsuccess(config_browser, open_url_yandex):
    browser.element('#text').should(be.blank).type('hgdfhdfhdfbndfndfndfnd').press_enter()
    browser.element('.EmptySearchResults-Title').should(have.text('Ничего не нашли'))
