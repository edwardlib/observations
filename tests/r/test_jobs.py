from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.jobs import jobs


def test_jobs():
  """Test module jobs.py by downloading
   jobs.csv and testing shape of
   extracted data has 899 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = jobs(test_path)
  try:
    assert x_train.shape == (899, 17)
  except:
    shutil.rmtree(test_path)
    raise()
