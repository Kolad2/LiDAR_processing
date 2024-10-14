import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
from pyrockstats.distrebutions import weibull, lognorm, paretoexp, gengamma
from pyrockstats import ecdf
from pyrockstats.empirical import lcdf_rvs
from pyrockstats.bootstrap.ks_statistics import get_ks_distribution

model = {
	"lognorm": lognorm,
	"weibull": weibull,
	"paretoexp": paretoexp,
	"gengamma": gengamma,
}

s = np.load('sampling.npy')


ks = get_ks_distribution(s, model["lognorm"], n_ks=100, x_min=None, x_max=None)

print(ks)
