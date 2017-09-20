from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_cereal import us_cereal


def test_us_cereal():
  """Test module us_cereal.py by downloading
   us_cereal.csv and testing shape of
   extracted data has 65 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_cereal(test_path)
  try:
    assert x_train.shape == (65, 11)
  except:
    shutil.rmtree(test_path)
    raise()
