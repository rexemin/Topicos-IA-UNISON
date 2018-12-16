"""
Plots the behavior of the vc-dimension given the size of a data training set.

Author: Ivan A. Moreno Soto.
Last updated: 2018/December/15.
"""

import Plots
# Yes, I actually want to use LaTeX strings because they're pretty.
using LaTeXStrings
# And I want to use PyPlot because it ain't broken in 1.0.0.
Plots.pyplot()

number_points = 300
d_vc_values = [2, 3, 5, 10, 15, 20]

# Generates 6 plots.
for d_vc in d_vc_values
    points = [N for N in range(1, stop = 20*d_vc, length = number_points)]
    f_dvc = [N^d_vc * exp(-N) for N in points]

    Plots.plot(points, f_dvc, title = string(L"f_{d_{vc}} = N^{d_{vc}} * exp(-N)", " para ", L"d_{vc}", " = $(d_vc)"))
    Plots.xaxis!("N")
    Plots.yaxis!(L"f_{d_{vc}}")
    Plots.savefig(string("_test-f_dvc-", d_vc))
end
