from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.final_four_short import final_four_short


def test_final_four_short():
  """Test module final_four_short.py by downloading
   final_four_short.csv and testing shape of
   extracted data has 512 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = final_four_short(test_path)
  try:
    assert x_train.shape == (512, 4)
  except:
    shutil.rmtree(test_path)
    raise()
