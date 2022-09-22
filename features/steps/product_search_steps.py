from behave import given, when, then


@when('Click on the first product of laptop category')
def click_first_product_laptop(context):
    context.app.search_result_page.click_first_product_laptop()


@then('User can see {product_result} search result')
def verify_product_search_result(context, product_result):
    context.app.search_result_page.verify_product_search_result(product_result)


@then('User can see an error message for irrelevant search')
def verify_error_message_unavailable_product(context):
    context.app.search_result_page.verify_error_message_unavailable_product()


@then('user can shuffle through product images using image slider')
def user_can_shuffle_images(context):
    context.app.search_result_page.user_can_shuffle_images()


