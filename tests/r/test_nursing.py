from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nursing import nursing


def test_nursing():
  """Test module nursing.py by downloading
   nursing.csv and testing shape of
   extracted data has 52 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nursing(test_path)
  try:
    assert x_train.shape == (52, 7)
  except:
    shutil.rmtree(test_path)
    raise()
