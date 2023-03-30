from selene import have
import allure


@allure.title('Successful authorization')
def test_auth(app, add_labels):
    app.open('')
    with allure.step('Verify successful authorization message is displayed'):
        app.element(".account").should(have.text("ChevChelios@gu.ru"))


@allure.title('Update customer info')
def test_update_customer_info(demoshop, app, add_labels):
    app.open('')
    with allure.step('Customer info'):
        demoshop.patch('/customer/info', json={'Customer-info.FirstName': 'John',
                                               'Customer-info.LastName': 'Deer',
                                               'Customer-info.Email': 'John@example.com'
                                               })


@allure.title('Adding and checking item in the cart')
def test_filling_cart(demoshop, app, add_labels):
    app.open('')
    with allure.step('Adding product to cart'):
        demoshop.post('/addproducttocart/catalog/31/1/1')
    with allure.step('Checking the cart'):
        app.element('.ico-cart').click()
        app.element('.product-name').should(have.text('14.1-inch Laptop'))


@allure.title('Removing an item from the shopping cart')
def test_delete_product_from_cart(demoshop, app, add_labels):
    app.open('')
    with allure.step('Remove cart'):
        app.element('.ico-cart').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


@allure.title('Search functionality: Non-existent product')
def test_search_box(demoshop, app, add_labels):
    app.open('')
    with allure.step('Enter non-existent product name in search box'):
        app.element('.search-box-text').type('00000').press_enter()
    with allure.step('Checking the error output'):
        app.element('.result').should(have.text('No products were found that matched your criteria.'))


@allure.title('Successful logout')
def test_logout(app, add_labels):
    app.open("")
    with allure.step('Clicking the logout button'):
        app.element('.ico-logout').click()
        app.element('.ico-login').should(have.text('Log in'))
