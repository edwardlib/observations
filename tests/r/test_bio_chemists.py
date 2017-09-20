from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bio_chemists import bio_chemists


def test_bio_chemists():
  """Test module bio_chemists.py by downloading
   bio_chemists.csv and testing shape of
   extracted data has 915 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bio_chemists(test_path)
  try:
    assert x_train.shape == (915, 6)
  except:
    shutil.rmtree(test_path)
    raise()
