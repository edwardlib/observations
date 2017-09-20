from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.presidents import presidents


def test_presidents():
  """Test module presidents.py by downloading
   presidents.csv and testing shape of
   extracted data has 120 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = presidents(test_path)
  try:
    assert x_train.shape == (120, 2)
  except:
    shutil.rmtree(test_path)
    raise()
