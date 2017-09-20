from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.school import school


def test_school():
  """Test module school.py by downloading
   school.csv and testing shape of
   extracted data has 568 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = school(test_path)
  try:
    assert x_train.shape == (568, 5)
  except:
    shutil.rmtree(test_path)
    raise()
