from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.twoyear import twoyear


def test_twoyear():
  """Test module twoyear.py by downloading
   twoyear.csv and testing shape of
   extracted data has 6763 rows and 23 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = twoyear(test_path)
  try:
    assert x_train.shape == (6763, 23)
  except:
    shutil.rmtree(test_path)
    raise()
