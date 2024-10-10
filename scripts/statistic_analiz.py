import numpy as np
from pyrockstats.distrebutions import weilbull, lognorm, paretoexp


weilbull.Weilbull(2, 2)


s = np.load('sampling.npy')
theta_1 = lognorm.fit_mle(s)
# theta_2 = weilbull.fit_mle(s)
# theta_3 = paretoexp.fit_mle(s)
#
print(theta_1)
# print(theta_2)
# print(theta_3)
