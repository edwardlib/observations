from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mastectomy import mastectomy


def test_mastectomy():
  """Test module mastectomy.py by downloading
   mastectomy.csv and testing shape of
   extracted data has 44 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mastectomy(test_path)
  try:
    assert x_train.shape == (44, 3)
  except:
    shutil.rmtree(test_path)
    raise()
