import sys
from contextlib import contextmanager
from io import StringIO
from os import listdir, path
from unittest import TestCase
from unittest.mock import patch

from chess_move_checker.__main__ import main


@contextmanager
def capture_stdout():
    sys.stdout, tmp = StringIO(), sys.stdout
    try:
        yield sys.stdout
    finally:
        sys.stdout = tmp


class RegressionTests(TestCase):
    def test_regression(self):
        regression_test_dir = path.dirname(path.abspath(__file__))
        inputs = [path.join(regression_test_dir, "inputs/", x) for x in
                  listdir(path.join(regression_test_dir, "inputs/"))]
        inputs.sort()
        outputs = [path.join(regression_test_dir, "outputs/", x) for x in
                   listdir(path.join(regression_test_dir, "outputs/"))]
        outputs.sort()
        for input_file, output_file in zip(inputs, outputs):
            # capture standard out and patch the script
            with capture_stdout() as out, patch.object(sys, "argv", ["program", "-i", input_file]):
                main()
            with open(output_file) as expected_output:
                with self.subTest("Testing {}".format(input_file)):
                    self.assertEqual(expected_output.read(), out.getvalue())
