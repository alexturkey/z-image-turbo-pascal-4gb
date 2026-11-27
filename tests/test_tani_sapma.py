"""scripts/tani.py DEVIATIONS section (kit KL-23): read only, shows engine switches in the environment, hides names, writes nothing.
No network, no GPU. Run: python -m unittest discover -s tests
"""
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TANI = ROOT / "scripts" / "tani.py"


def run_tani(env_extra=None):
    env = dict(os.environ)
    env.update(env_extra or {})
    p = subprocess.run([sys.executable, "-I", "-X", "utf8", str(TANI), "--atla-kuru"], capture_output=True, env=env, timeout=120)
    return p.returncode, p.stdout.decode("utf-8", "replace")


def git_status():
    try:
        return subprocess.run(["git", "--no-optional-locks", "-C", str(ROOT), "status", "--porcelain", "-uno"], capture_output=True, timeout=60).stdout
    except OSError:
        return None


class Deviations(unittest.TestCase):
    def test_section_and_env_switch_visible(self):
        rc, out = run_tani({"SD_TEST_SWITCH": "1"})
        self.assertEqual(rc, 0, out[-300:])
        self.assertIn("## deviations from the defaults", out)
        self.assertIn("SD_TEST_SWITCH=1", out)
        self.assertIn("model ", out)

    def test_name_in_value_is_hidden(self):
        name = "Hidden" + "Person" + "Name"
        rc, out = run_tani({"SD_TEST_SWITCH": name, "USERNAME": name})
        self.assertEqual(rc, 0, out[-300:])
        self.assertNotIn(name, out)

    def test_writes_nothing(self):
        before = git_status()
        rc, _ = run_tani()
        self.assertEqual(rc, 0)
        self.assertEqual(git_status(), before)


if __name__ == "__main__":
    unittest.main()
