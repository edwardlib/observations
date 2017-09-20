from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_stamps import us_stamps


def test_us_stamps():
  """Test module us_stamps.py by downloading
   us_stamps.csv and testing shape of
   extracted data has 25 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_stamps(test_path)
  try:
    assert x_train.shape == (25, 2)
  except:
    shutil.rmtree(test_path)
    raise()
