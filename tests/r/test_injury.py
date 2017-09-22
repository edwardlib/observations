from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.injury import injury


def test_injury():
  """Test module injury.py by downloading
   injury.csv and testing shape of
   extracted data has 7150 rows and 30 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = injury(test_path)
  try:
    assert x_train.shape == (7150, 30)
  except:
    shutil.rmtree(test_path)
    raise()
