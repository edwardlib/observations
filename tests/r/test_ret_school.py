from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ret_school import ret_school


def test_ret_school():
  """Test module ret_school.py by downloading
   ret_school.csv and testing shape of
   extracted data has 5225 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ret_school(test_path)
  try:
    assert x_train.shape == (5225, 17)
  except:
    shutil.rmtree(test_path)
    raise()
