import unittest

def test_suites():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('src', pattern='test_*.py')
    return test_suite

test_suite = test_suites()
runner = unittest.TextTestRunner(verbosity=1)
runner.run(test_suite)
