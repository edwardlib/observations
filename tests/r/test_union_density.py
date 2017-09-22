from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.union_density import union_density


def test_union_density():
  """Test module union_density.py by downloading
   union_density.csv and testing shape of
   extracted data has 20 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = union_density(test_path)
  try:
    assert x_train.shape == (20, 4)
  except:
    shutil.rmtree(test_path)
    raise()
