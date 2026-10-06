"""
Physical and astrodynamic constants for astrosim.

Units: km and s (and combinations: km^3/s^2, km/s).
Each constant cites its source; do not change a value without updating its source.
"""

from typing import Final

# --- Gravitational parameters (GM), km^3/s^2 --------------------------------
# Source: JPL DE440 ephemerides (Park et al. 2021, AJ 161:105), published by
# NAIF in gm_de440.tpc: naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/
MU_SUN: Final[float] = 1.3271244004127942e11
MU_EARTH: Final[float] = 3.9860043550702266e5
MU_MOON: Final[float] = 4.9028001184575496e3

# --- Radii, km --------------------------------------------------------------
# Source: IAU WGCCRE 2015 report (Archinal et al. 2018), via NAIF pck00011.tpc.
R_EARTH_EQ: Final[float] = 6378.1366
R_EARTH_POLAR: Final[float] = 6356.7519
R_MOON: Final[float] = 1737.4
R_SUN: Final[float] = 695700.0

# --- Earth shape (dimensionless) --------------------------------------------
# Source: IERS Conventions (2010), Table 1.1 ("zero-tide" value).
J2_EARTH: Final[float] = 1.0826359e-3