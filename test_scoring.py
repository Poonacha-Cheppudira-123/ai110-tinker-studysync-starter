"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


# TODO: add at least one more test, e.g. a boundary case for "Skip" (a score
# of 59) or the exact boundary for "Good" (a score of 80).


def test_session_rating_boundary_30_is_skip():
    assert session_rating(30) == "Skip"


# Lower and upper edges of the valid domain (0-100 inclusive) should still
# work normally -- only values outside that range should be rejected.
def test_session_rating_boundary_0_is_skip():
    assert session_rating(0) == "Skip"


def test_session_rating_boundary_100_is_great():
    assert session_rating(100) == "Great"


# Negative and >100 scores are input the function was never meant to
# receive -- it treats them the same as the nearest valid tier instead of
# crashing.
def test_session_rating_negative_is_skip():
    assert session_rating(-20) == "Skip"


def test_session_rating_above_100_is_great():
    assert session_rating(105) == "Great"


# A float combined_score is a real bug: minutes and focus are always ints,
# so combined_score should never be fractional. The function truncates it
# back to a whole number instead of crashing.
def test_session_rating_decimal_is_good():
    assert session_rating(87.5) == "Good"
