from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rental import rental


def test_rental():
  """Test module rental.py by downloading
   rental.csv and testing shape of
   extracted data has 128 rows and 23 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rental(test_path)
  try:
    assert x_train.shape == (128, 23)
  except:
    shutil.rmtree(test_path)
    raise()
