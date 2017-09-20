from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.recid import recid


def test_recid():
  """Test module recid.py by downloading
   recid.csv and testing shape of
   extracted data has 1445 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = recid(test_path)
  try:
    assert x_train.shape == (1445, 18)
  except:
    shutil.rmtree(test_path)
    raise()
