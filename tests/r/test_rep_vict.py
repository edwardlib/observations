from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rep_vict import rep_vict


def test_rep_vict():
  """Test module rep_vict.py by downloading
   rep_vict.csv and testing shape of
   extracted data has 8 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rep_vict(test_path)
  try:
    assert x_train.shape == (8, 8)
  except:
    shutil.rmtree(test_path)
    raise()
