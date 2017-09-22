from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.stackloss import stackloss


def test_stackloss():
  """Test module stackloss.py by downloading
   stackloss.csv and testing shape of
   extracted data has 21 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = stackloss(test_path)
  try:
    assert x_train.shape == (21, 4)
  except:
    shutil.rmtree(test_path)
    raise()
