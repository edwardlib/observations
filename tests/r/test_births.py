from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.births import births


def test_births():
  """Test module births.py by downloading
   births.csv and testing shape of
   extracted data has 7305 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = births(test_path)
  try:
    assert x_train.shape == (7305, 8)
  except:
    shutil.rmtree(test_path)
    raise()
