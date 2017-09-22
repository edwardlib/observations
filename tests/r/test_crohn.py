from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.crohn import crohn


def test_crohn():
  """Test module crohn.py by downloading
   crohn.csv and testing shape of
   extracted data has 387 rows and 212 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = crohn(test_path)
  try:
    assert x_train.shape == (387, 212)
  except:
    shutil.rmtree(test_path)
    raise()
