from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.stars_cyg import stars_cyg


def test_stars_cyg():
  """Test module stars_cyg.py by downloading
   stars_cyg.csv and testing shape of
   extracted data has 47 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = stars_cyg(test_path)
  try:
    assert x_train.shape == (47, 2)
  except:
    shutil.rmtree(test_path)
    raise()
