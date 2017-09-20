from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nuts import nuts


def test_nuts():
  """Test module nuts.py by downloading
   nuts.csv and testing shape of
   extracted data has 52 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nuts(test_path)
  try:
    assert x_train.shape == (52, 8)
  except:
    shutil.rmtree(test_path)
    raise()
