# test_framework/core/environment.py
def setup_driver(context):
    from test_framework.utils.driver_factory import create_driver
    context.driver = create_driver()

def teardown_driver(context):
    context.driver.quit()