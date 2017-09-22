from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hhs_cybsec_breaches import hhs_cybsec_breaches


def test_hhs_cybsec_breaches():
  """Test module hhs_cybsec_breaches.py by downloading
   hhs_cybsec_breaches.csv and testing shape of
   extracted data has 1151 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hhs_cybsec_breaches(test_path)
  try:
    assert x_train.shape == (1151, 9)
  except:
    shutil.rmtree(test_path)
    raise()
