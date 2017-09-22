from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.swim_records import swim_records


def test_swim_records():
  """Test module swim_records.py by downloading
   swim_records.csv and testing shape of
   extracted data has 62 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = swim_records(test_path)
  try:
    assert x_train.shape == (62, 3)
  except:
    shutil.rmtree(test_path)
    raise()
