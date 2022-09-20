from behave import given, when, then


@then('User can see {product_result} search result')
def verify_product_search_result(context, product_result):
    context.app.search_result_page.verify_product_search_result(product_result)


@then('User can see an error message for irrelevant search')
def verify_error_message_unavailable_product(context):
    context.app.search_result_page.verify_error_message_unavailable_product()