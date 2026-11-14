"""The localized READMEs must carry exactly the same facts as README.md (no network, no GPU).

A localized README is written for its readers, not translated word for word. What may never differ:
commands, file names, flags, environment variables, addresses and numbers. This test compares those
tokens between README.md and every README.<code>.md, and looks for invisible characters.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ["ar", "da", "de", "el", "es", "fi", "fr", "he", "hi", "id", "it", "ja", "km", "ko", "lo", "ms", "my", "nb",
         "nl", "pl", "pt", "ru", "sv", "sw", "th", "tl", "tr", "vi", "zh"]
INVISIBLE = "".join(chr(c) for c in (0x200B, 0x200C, 0x200D, 0x200E, 0x200F, 0x202A, 0x202B, 0x202C, 0x202D,
                                      0x202E, 0x2066, 0x2067, 0x2068, 0x2069, 0xFEFF, 0x00AD))


def fenced_blocks(text):
    return [b.strip("\n") for b in re.findall(r"^```[^\n]*\n(.*?)^```", text, re.S | re.M)]


def without_fences(text):
    return re.sub(r"^```[^\n]*\n.*?^```", "", text, flags=re.S | re.M)


def inline_code(text):
    return sorted(set(re.findall(r"`([^`\n]+)`", without_fences(text))))


def urls(text):
    return sorted(set(u.rstrip(".,;") for u in re.findall(r"https?://[^\s)>\]\"']+", text)))


def link_targets(text):
    """Relative link and image targets; the language bar is compared separately."""
    body = "\n".join(text.splitlines()[1:])
    return sorted(set(t for t in re.findall(r"\]\(([^)\s]+)\)", body) if not t.startswith("http")))


def numbers(text):
    """Numbers outside code, as written (digits with inner , . or space kept)."""
    plain = re.sub(r"`[^`\n]+`", " ", without_fences(text))
    plain = re.sub(r"\]\([^)]*\)", "]", plain)
    plain = re.sub(r"https?://\S+", " ", plain)
    return sorted(set(re.findall(r"\d+(?:[.,]\d+)*", plain)))


def slots(text):
    """{{name}} slots: numbers that a script fills in every README at once, so they are the same everywhere."""
    return sorted(re.findall(r"\{\{\w+\}\}", text))


def language_bar(text):
    return re.sub(r"\*\*", "", text.splitlines()[0])


class Readmes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.en = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.found = {c: ROOT / ("README.%s.md" % c) for c in LANGS if (ROOT / ("README.%s.md" % c)).is_file()}

    def test_language_bar_lists_only_files_that_exist(self):
        for target in re.findall(r"\]\((README[^)]*\.md)\)", self.en.splitlines()[0]):
            self.assertTrue((ROOT / target).is_file(), "the language bar links to missing %s" % target)

    def test_same_commands_names_addresses_and_numbers(self):
        for code, path in sorted(self.found.items()):
            text = path.read_text(encoding="utf-8")
            with self.subTest(lang=code):
                self.assertEqual(fenced_blocks(text), fenced_blocks(self.en), "code blocks differ")
                missing = [c for c in inline_code(self.en) if c not in inline_code(text)]
                self.assertEqual(missing, [], "inline code missing")
                self.assertEqual(urls(text), urls(self.en), "addresses differ")
                self.assertEqual(link_targets(text), link_targets(self.en), "relative links differ")
                missing = [n for n in numbers(self.en) if n not in numbers(text)]
                self.assertEqual(missing, [], "numbers missing or rewritten")
                self.assertEqual(slots(text), slots(self.en), "number slots differ")

    def test_language_bar_is_the_same_everywhere(self):
        for code, path in sorted(self.found.items()):
            first = path.read_text(encoding="utf-8").splitlines()[0]
            with self.subTest(lang=code):
                # the current language is bold and not a link; every other entry is the same link as in README.md
                bar = language_bar(first)
                for label, target in re.findall(r"\[([^\]]+)\]\((README[^)]*\.md)\)", language_bar(self.en.splitlines()[0])):
                    if target == "README.%s.md" % code:
                        self.assertIn(label, bar)
                    else:
                        self.assertIn("[%s](%s)" % (label, target), bar)
                self.assertIn("(README.md)", bar)

    def test_no_invisible_characters(self):
        for path in [ROOT / "README.md"] + sorted(self.found.values()):
            text = path.read_text(encoding="utf-8")
            with self.subTest(file=path.name):
                bad = sorted(set("U+%04X" % ord(ch) for ch in text if ch in INVISIBLE or (ord(ch) < 32 and ch not in "\n\t")))
                self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
