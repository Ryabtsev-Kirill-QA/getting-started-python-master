from selene.support.shared import browser
from selene import have


def test_user_form_check():

    browser.open('https://demoqa.com/text-box')

    browser.element('#userName').type('Ivanov Ivan')
    browser.element('#userEmail').type('Ivanov_Ivan@gmail.com')
    browser.element('#currentAddress').type('Pushkina 1')
    browser.element('#permanentAddress').type('Plushkina 1')
    browser.element('.btn-primary').click()

    browser.element('#name').should(have.text('Ivanov Ivan'))
    browser.element('#email').should(have.text('Ivanov_Ivan@gmail.com'))
    browser.element('#output #currentAddress').should(have.text('Pushkina 1'))
    browser.element('#output #permanentAddress').should(have.text('Plushkina 1'))