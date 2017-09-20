from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.biomass_till import biomass_till


def test_biomass_till():
  """Test module biomass_till.py by downloading
   biomass_till.csv and testing shape of
   extracted data has 58 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = biomass_till(test_path)
  try:
    assert x_train.shape == (58, 4)
  except:
    shutil.rmtree(test_path)
    raise()
