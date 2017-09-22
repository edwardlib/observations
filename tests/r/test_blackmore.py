from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.blackmore import blackmore


def test_blackmore():
  """Test module blackmore.py by downloading
   blackmore.csv and testing shape of
   extracted data has 945 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = blackmore(test_path)
  try:
    assert x_train.shape == (945, 4)
  except:
    shutil.rmtree(test_path)
    raise()
