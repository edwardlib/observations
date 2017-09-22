from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.guerry import guerry


def test_guerry():
  """Test module guerry.py by downloading
   guerry.csv and testing shape of
   extracted data has 86 rows and 23 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = guerry(test_path)
  try:
    assert x_train.shape == (86, 23)
  except:
    shutil.rmtree(test_path)
    raise()
