from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.education import education


def test_education():
  """Test module education.py by downloading
   education.csv and testing shape of
   extracted data has 50 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = education(test_path)
  try:
    assert x_train.shape == (50, 6)
  except:
    shutil.rmtree(test_path)
    raise()
