from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hawk_tail import hawk_tail


def test_hawk_tail():
  """Test module hawk_tail.py by downloading
   hawk_tail.csv and testing shape of
   extracted data has 838 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hawk_tail(test_path)
  try:
    assert x_train.shape == (838, 2)
  except:
    shutil.rmtree(test_path)
    raise()
