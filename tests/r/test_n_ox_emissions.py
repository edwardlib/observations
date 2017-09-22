from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.n_ox_emissions import n_ox_emissions


def test_n_ox_emissions():
  """Test module n_ox_emissions.py by downloading
   n_ox_emissions.csv and testing shape of
   extracted data has 8088 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = n_ox_emissions(test_path)
  try:
    assert x_train.shape == (8088, 4)
  except:
    shutil.rmtree(test_path)
    raise()
