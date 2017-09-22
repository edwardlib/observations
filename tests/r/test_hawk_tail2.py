from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hawk_tail2 import hawk_tail2


def test_hawk_tail2():
  """Test module hawk_tail2.py by downloading
   hawk_tail2.csv and testing shape of
   extracted data has 577 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hawk_tail2(test_path)
  try:
    assert x_train.shape == (577, 3)
  except:
    shutil.rmtree(test_path)
    raise()
