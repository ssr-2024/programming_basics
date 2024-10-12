def test_output_hello_on_1(self):
        with patch('builtins.input', side_effect=['1']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, 'uml')
        self.assertEqual('Hello', s.getvalue().strip())