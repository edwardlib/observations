from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.terr_incidents import terr_incidents


def test_terr_incidents():
  """Test module terr_incidents.py by downloading
   terr_incidents.csv and testing shape of
   extracted data has 206 rows and 45 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = terr_incidents(test_path)
  try:
    assert x_train.shape == (206, 45)
  except:
    shutil.rmtree(test_path)
    raise()
