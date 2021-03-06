from django.views.generic import UpdateView
from django.utils import timezone
from django.http import Http404

from .logger import RrsmLoggerMixin


class RrsmHelpers(RrsmLoggerMixin):
    def pga_pgv_centimeters_to_meters(self, pga_min, pga_max, pgv_min, pgv_max):
        """Convert PGA and PGV values from centimeters to meters.
        PGA and PGV values are rendered in the interface in centimerets,
        but the underlying web service is operating using meters.
        """
        if pga_min:
            pga_min = pga_min / 100
        if pga_max:
            pga_max = pga_max / 100
        if pgv_min:
            pgv_min = pgv_min / 100
        if pgv_max:
            pgv_max = pgv_max / 100
        return pga_min, pga_max, pgv_min, pgv_max
