import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills" / "peyar" / "scripts"))

import check_name  # noqa: E402
import score36  # noqa: E402
import score  # noqa: E402


def test_syllables():
    assert score.syllables("Nuke") == 1
    assert score.syllables("Become") == 2
    assert score.syllables("Peyar") == 2
    assert score.syllables("Zepto") == 2
    assert score.syllables("Unacademy") == 5


def test_short_known_words_beat_long_foreign_compounds():
    """The Frozen Iris lesson: short, sayable names should rank higher."""
    s = {n: score.analyse(n)["score"] for n in ["Nuke", "Become", "Frozen Iris"]}
    assert s["Nuke"] > s["Frozen Iris"]
    assert s["Become"] > s["Frozen Iris"]


def test_long_descriptive_name_scores_low():
    r = score.analyse("Chennai Premium Quality Idli Company")
    assert r["score"] < 50
    assert any("words" in f for f in r["flags"])


def test_unpronounceable_flagged():
    r = score.analyse("Xqzrtv")
    assert any("consonant cluster" in f for f in r["flags"])
    assert r["score"] < 70


def test_accent_traps_flagged():
    flags = score.analyse("Wavez")["flags"]
    assert any("v/w" in f for f in flags)
    assert any("z/j" in f for f in flags)


def test_alphanumeric_note():
    assert any("alphanumeric" in f for f in score.analyse("Bira 91")["flags"])


def test_hiatus_syllables():
    assert score.syllables("Tieout") == 2
    assert score.syllables("Lekhio") == 3


def test_no_false_cluster_on_double_letters_or_common_clusters():
    for n in ["Pebble", "Nibbl", "Strand", "Mullai"]:
        assert not any("consonant cluster" in f for f in score.analyse(n)["flags"]), n


def test_indian_digraphs_not_clusters():
    for n in ["Tanishq", "Bhakti", "Akhshay", "Dhruv"]:
        assert not any("consonant cluster" in f for f in score.analyse(n)["flags"]), n


def test_ll_not_confusable():
    assert not any("letter shapes" in f for f in score.analyse("Mullai")["flags"])


def test_whois_tlds_configured():
    assert "io" in check_name.WHOIS
    assert {"in", "co.in", "com"} <= set(check_name.WHOIS_FALLBACK)


def test_score36_math_and_unverified():
    r = score36.compute("X", "PPPPPP PPPPPP PPPPPP UPPUPP PPUPUP PPPPUU")
    assert r["display"] == "100 (6 unverified)"
    r = score36.compute("Y", "WWWWWW PPPPPP PPPPPP UPPUPP PPUPUP PPPPUU")
    assert r["score"] == round(100 * 54 / 60)


def test_score36_d_fail_is_out():
    r = score36.compute("Z", "PPPPPP PPPPPP PPPPPP PPPFPP PPPPPP PPPPPP")
    assert r["verdict"].startswith("OUT") and "D4" in r["verdict"]


def test_score36_rejects_bad_input():
    try:
        score36.compute("Q", "PPP")
    except ValueError:
        return
    raise AssertionError("short input accepted")


def test_slug_and_handle():
    assert check_name.slug("Paper Boat") == "paperboat"
    assert check_name.handle("Bira 91!") == "bira91"


def test_manual_links_include_ip_india_and_mca():
    links = check_name.manual_links("Peyar")
    joined = " ".join(links.values())
    assert "ipindia.gov.in" in joined
    assert "mca.gov.in" in joined


if __name__ == "__main__":  # run without pytest: python3 tests/test_score.py
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"ok   {name}")
            except AssertionError as e:
                fails += 1
                print(f"FAIL {name}: {e!r}")
    sys.exit(1 if fails else 0)
