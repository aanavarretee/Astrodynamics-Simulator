import math

from astrosim import constants as c


def test_leo_period_at_400_km():
    a = c.R_EARTH_EQ + 400.0
    period_min = 2 * math.pi * math.sqrt(a**3 / c.MU_EARTH) / 60
    assert 92.0 < period_min < 93.0


def test_mass_ratios():
    assert math.isclose(c.MU_SUN / c.MU_EARTH, 332946, rel_tol=1e-3)
    assert math.isclose(c.MU_EARTH / c.MU_MOON, 81.3, rel_tol=1e-3)