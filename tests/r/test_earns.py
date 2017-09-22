from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.earns import earns


def test_earns():
  """Test module earns.py by downloading
   earns.csv and testing shape of
   extracted data has 41 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = earns(test_path)
  try:
    assert x_train.shape == (41, 14)
  except:
    shutil.rmtree(test_path)
    raise()
