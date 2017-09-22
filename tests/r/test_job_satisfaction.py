from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.job_satisfaction import job_satisfaction


def test_job_satisfaction():
  """Test module job_satisfaction.py by downloading
   job_satisfaction.csv and testing shape of
   extracted data has 8 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = job_satisfaction(test_path)
  try:
    assert x_train.shape == (8, 4)
  except:
    shutil.rmtree(test_path)
    raise()
