from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.head_injury import head_injury


def test_head_injury():
  """Test module head_injury.py by downloading
   head_injury.csv and testing shape of
   extracted data has 3121 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = head_injury(test_path)
  try:
    assert x_train.shape == (3121, 11)
  except:
    shutil.rmtree(test_path)
    raise()
