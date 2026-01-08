import grasp2alm as g2a
import numpy as np
import matplotlib.pyplot as plt

gridfile00 = "input/20251212/Forebaffle_diffraction_farfield_40GHz_FOVxedge_xpol_job25_polar.grd"
gridfile45 = "input/20251212/Forebaffle_diffraction_farfield_40GHz_FOVxedge_ypol_job25_polar.grd"

grid = g2a.BeamGrid_MOD(gridfile00, gridfile45)
g2polar0, g2polarC, g2polarS = grid.to_polar(copol_axis="x")

nside = 256
outOftheta_val = hp.UNSEEN # Default
gmap0 = g2polar0.to_map(nside, outOftheta_val=outOftheta_val, interp_method="linear")
gmapC = g2polarC.to_map(nside, outOftheta_val=outOftheta_val, interp_method="linear")
gmapS = g2polarS.to_map(nside, outOftheta_val=outOftheta_val, interp_method="linear")

gmapP = (gmapC - 1j * gmapS) / 2
gmapM = (gmapC + 1j * gmapS) / 2

galm0 = gmap0.to_alm()
galmC = gmapC.to_alm()
galmS = gmapS.to_alm()

