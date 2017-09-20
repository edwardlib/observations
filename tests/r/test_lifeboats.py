from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lifeboats import lifeboats


def test_lifeboats():
  """Test module lifeboats.py by downloading
   lifeboats.csv and testing shape of
   extracted data has 18 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lifeboats(test_path)
  try:
    assert x_train.shape == (18, 8)
  except:
    shutil.rmtree(test_path)
    raise()
