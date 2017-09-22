from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fatality import fatality


def test_fatality():
  """Test module fatality.py by downloading
   fatality.csv and testing shape of
   extracted data has 336 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fatality(test_path)
  try:
    assert x_train.shape == (336, 10)
  except:
    shutil.rmtree(test_path)
    raise()
