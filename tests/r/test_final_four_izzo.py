from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.final_four_izzo import final_four_izzo


def test_final_four_izzo():
  """Test module final_four_izzo.py by downloading
   final_four_izzo.csv and testing shape of
   extracted data has 1664 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = final_four_izzo(test_path)
  try:
    assert x_train.shape == (1664, 4)
  except:
    shutil.rmtree(test_path)
    raise()
