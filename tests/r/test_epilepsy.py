from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.epilepsy import epilepsy


def test_epilepsy():
  """Test module epilepsy.py by downloading
   epilepsy.csv and testing shape of
   extracted data has 236 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = epilepsy(test_path)
  try:
    assert x_train.shape == (236, 6)
  except:
    shutil.rmtree(test_path)
    raise()
