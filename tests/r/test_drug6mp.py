from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.drug6mp import drug6mp


def test_drug6mp():
  """Test module drug6mp.py by downloading
   drug6mp.csv and testing shape of
   extracted data has 21 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = drug6mp(test_path)
  try:
    assert x_train.shape == (21, 5)
  except:
    shutil.rmtree(test_path)
    raise()
