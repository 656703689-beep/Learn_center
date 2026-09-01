import os
import subprocess
import sys
import unittest
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[1]
SCRIPT = WORKSPACE / "study_log.py"


class StudyLogScriptTests(unittest.TestCase):
    def run_script(self, user_input: str) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment["PYTHONIOENCODING"] = "utf-8"

        return subprocess.run(
            [sys.executable, str(SCRIPT)],
            input=user_input,
            text=True,
            capture_output=True,
            encoding="utf-8",
            env=environment,
            check=False,
        )

    def test_guess_secret_number(self) -> None:
        result = self.run_script("7\n")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("猜对了", result.stdout)
        self.assertIn("1次", result.stdout)

    def test_guess_too_large_then_secret(self) -> None:
        result = self.run_script("8\n7\n")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("大了", result.stdout)
        self.assertIn("猜对了", result.stdout)
        self.assertIn("2次", result.stdout)

    def test_guess_too_small_then_secret(self) -> None:
        result = self.run_script("6\n7\n")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("小了", result.stdout)
        self.assertIn("猜对了", result.stdout)
        self.assertIn("2次", result.stdout)


if __name__ == "__main__":
    unittest.main()
