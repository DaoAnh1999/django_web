import csv
from .tests import TaskAPITest

def export_test_results_to_csv(test_results):
    with open('api_test_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Test Name', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for test in test_results:
            writer.writerow({'Test Name': test._testMethodName, 'Status': 'Passed' if test.wasSuccessful() else 'Failed'})

if __name__ == '__main__':
    import unittest
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TaskAPITest)
    test_results = unittest.TextTestRunner().run(test_suite)
    export_test_results_to_csv(test_results)
