from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.vince111b import vince111b


def test_vince111b():
  """Test module vince111b.py by downloading
   vince111b.csv and testing shape of
   extracted data has 36 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = vince111b(test_path)
  try:
    assert x_train.shape == (36, 8)
  except:
    shutil.rmtree(test_path)
    raise()
