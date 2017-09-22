from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ofp import ofp


def test_ofp():
  """Test module ofp.py by downloading
   ofp.csv and testing shape of
   extracted data has 4406 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ofp(test_path)
  try:
    assert x_train.shape == (4406, 19)
  except:
    shutil.rmtree(test_path)
    raise()
