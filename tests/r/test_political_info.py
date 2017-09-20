from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.political_info import political_info


def test_political_info():
  """Test module political_info.py by downloading
   political_info.csv and testing shape of
   extracted data has 1807 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = political_info(test_path)
  try:
    assert x_train.shape == (1807, 8)
  except:
    shutil.rmtree(test_path)
    raise()
