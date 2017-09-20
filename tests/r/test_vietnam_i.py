from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.vietnam_i import vietnam_i


def test_vietnam_i():
  """Test module vietnam_i.py by downloading
   vietnam_i.csv and testing shape of
   extracted data has 27765 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = vietnam_i(test_path)
  try:
    assert x_train.shape == (27765, 12)
  except:
    shutil.rmtree(test_path)
    raise()
