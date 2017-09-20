from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.aulatlong import aulatlong


def test_aulatlong():
  """Test module aulatlong.py by downloading
   aulatlong.csv and testing shape of
   extracted data has 10 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = aulatlong(test_path)
  try:
    assert x_train.shape == (10, 2)
  except:
    shutil.rmtree(test_path)
    raise()
