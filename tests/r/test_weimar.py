from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.weimar import weimar


def test_weimar():
  """Test module weimar.py by downloading
   weimar.csv and testing shape of
   extracted data has 10 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = weimar(test_path)
  try:
    assert x_train.shape == (10, 11)
  except:
    shutil.rmtree(test_path)
    raise()
