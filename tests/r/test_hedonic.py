from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hedonic import hedonic


def test_hedonic():
  """Test module hedonic.py by downloading
   hedonic.csv and testing shape of
   extracted data has 506 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hedonic(test_path)
  try:
    assert x_train.shape == (506, 15)
  except:
    shutil.rmtree(test_path)
    raise()
