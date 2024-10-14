import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
from pyrockstats.distrebutions import weibull, lognorm, paretoexp, gengamma
from pyrockstats import ecdf


s = np.load('sampling.npy')

x, eF = ecdf(s)
x_min = np.min(x)
x_max = np.max(x)

model = {
	"lognorm": lognorm,
	"weibull": weibull,
	"paretoexp": paretoexp,
	"gengamma": gengamma,
}

theta, distribution, cdf = {}, {}, {}
for name in model:
	theta[name] = model[name].fit(s)
	print(name, theta[name])
	distribution[name] = model[name](*theta[name])
	cdf[name] = distribution[name].cdf(x)

fig = plt.figure(figsize=(16, 4))
ax = [fig.add_subplot(1, 1, 1)]
ax[0].plot(x, eF, color='black')
ax[0].plot(x, cdf["lognorm"], color='red')
ax[0].plot(x, cdf["weibull"], color='green')
ax[0].plot(x, cdf["paretoexp"], color='red')
ax[0].plot(x, cdf["gengamma"], color='blue')
ax[0].set_xlim([x_min, x_max])
ax[0].set_xscale('log')
plt.show()


