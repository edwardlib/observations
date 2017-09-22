from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.us_public_school import us_public_school


def test_us_public_school():
  """Test module us_public_school.py by downloading
   us_public_school.csv and testing shape of
   extracted data has 51 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = us_public_school(test_path)
  try:
    assert x_train.shape == (51, 4)
  except:
    shutil.rmtree(test_path)
    raise()
