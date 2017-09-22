from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.quarrels import quarrels


def test_quarrels():
  """Test module quarrels.py by downloading
   quarrels.csv and testing shape of
   extracted data has 779 rows and 84 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = quarrels(test_path)
  try:
    assert x_train.shape == (779, 84)
  except:
    shutil.rmtree(test_path)
    raise()
