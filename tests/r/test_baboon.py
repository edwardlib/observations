from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.baboon import baboon


def test_baboon():
  """Test module baboon.py by downloading
   baboon.csv and testing shape of
   extracted data has 152 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = baboon(test_path)
  try:
    assert x_train.shape == (152, 3)
  except:
    shutil.rmtree(test_path)
    raise()
