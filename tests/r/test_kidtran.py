from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.kidtran import kidtran


def test_kidtran():
  """Test module kidtran.py by downloading
   kidtran.csv and testing shape of
   extracted data has 863 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = kidtran(test_path)
  try:
    assert x_train.shape == (863, 6)
  except:
    shutil.rmtree(test_path)
    raise()
