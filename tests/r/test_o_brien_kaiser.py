from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.o_brien_kaiser import o_brien_kaiser


def test_o_brien_kaiser():
  """Test module o_brien_kaiser.py by downloading
   o_brien_kaiser.csv and testing shape of
   extracted data has 16 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = o_brien_kaiser(test_path)
  try:
    assert x_train.shape == (16, 17)
  except:
    shutil.rmtree(test_path)
    raise()
