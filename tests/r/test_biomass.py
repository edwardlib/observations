from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.biomass import biomass


def test_biomass():
  """Test module biomass.py by downloading
   biomass.csv and testing shape of
   extracted data has 153 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = biomass(test_path)
  try:
    assert x_train.shape == (153, 8)
  except:
    shutil.rmtree(test_path)
    raise()
