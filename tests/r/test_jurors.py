from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.jurors import jurors


def test_jurors():
  """Test module jurors.py by downloading
   jurors.csv and testing shape of
   extracted data has 52 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = jurors(test_path)
  try:
    assert x_train.shape == (52, 4)
  except:
    shutil.rmtree(test_path)
    raise()
