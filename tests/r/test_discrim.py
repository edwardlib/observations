from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.discrim import discrim


def test_discrim():
  """Test module discrim.py by downloading
   discrim.csv and testing shape of
   extracted data has 410 rows and 37 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = discrim(test_path)
  try:
    assert x_train.shape == (410, 37)
  except:
    shutil.rmtree(test_path)
    raise()
