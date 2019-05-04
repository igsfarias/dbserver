# coding=utf-8
import unittest
import HtmlTestRunner
import dbserver_testcases.testcases


class TestSuite(unittest.TestCase):

    def test_suite_complete(self):
        all_tests = unittest.TestSuite()
        # inserindo casos de testes na suite de teste a ser executada
        all_tests.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(dbserver_testcases.testcases.TestCasesAutomationPractice)
        ])

        # configurando modelo de report
        exec = HtmlTestRunner.HTMLTestRunner(
            report_title='Test Report - www.automationpractice.com'.upper(),
            report_name='Results'
        )
        # rodando suite de teste
        exec.run(all_tests)


if __name__ == '__main__':
    unittest.main()
