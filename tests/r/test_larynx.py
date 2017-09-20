from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.larynx import larynx


def test_larynx():
  """Test module larynx.py by downloading
   larynx.csv and testing shape of
   extracted data has 90 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = larynx(test_path)
  try:
    assert x_train.shape == (90, 5)
  except:
    shutil.rmtree(test_path)
    raise()
