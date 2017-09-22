from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hi_hours_worked import hi_hours_worked


def test_hi_hours_worked():
  """Test module hi_hours_worked.py by downloading
   hi_hours_worked.csv and testing shape of
   extracted data has 22272 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hi_hours_worked(test_path)
  try:
    assert x_train.shape == (22272, 13)
  except:
    shutil.rmtree(test_path)
    raise()
