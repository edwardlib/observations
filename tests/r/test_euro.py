from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.euro import euro


def test_euro():
  """Test module euro.py by downloading
   euro.csv and testing shape of
   extracted data has 11 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = euro(test_path)
  try:
    assert x_train.shape == (11, 1)
  except:
    shutil.rmtree(test_path)
    raise()
