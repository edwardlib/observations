from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.diamonds import diamonds


def test_diamonds():
  """Test module diamonds.py by downloading
   diamonds.csv and testing shape of
   extracted data has 351 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = diamonds(test_path)
  try:
    assert x_train.shape == (351, 6)
  except:
    shutil.rmtree(test_path)
    raise()
