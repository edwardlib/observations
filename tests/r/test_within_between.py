from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.within_between import within_between


def test_within_between():
  """Test module within_between.py by downloading
   within_between.csv and testing shape of
   extracted data has 16 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = within_between(test_path)
  try:
    assert x_train.shape == (16, 10)
  except:
    shutil.rmtree(test_path)
    raise()
