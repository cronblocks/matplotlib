from mpl_toolkits.axes_grid1.parasite_axes import (
    host_axes_class_factory, parasite_axes_class_factory,
    subplot_class_factory)
from mpl_toolkits.axisartist.axislines import Axes


ParasiteAxes = parasite_axes_class_factory(Axes)
HostAxes = host_axes_class_factory(Axes)
SubplotHost = subplot_class_factory(HostAxes)
