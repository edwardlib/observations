from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.final_four_long import final_four_long


def test_final_four_long():
  """Test module final_four_long.py by downloading
   final_four_long.csv and testing shape of
   extracted data has 2048 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = final_four_long(test_path)
  try:
    assert x_train.shape == (2048, 3)
  except:
    shutil.rmtree(test_path)
    raise()
