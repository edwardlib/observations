from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ams_survey import ams_survey


def test_ams_survey():
  """Test module ams_survey.py by downloading
   ams_survey.csv and testing shape of
   extracted data has 24 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ams_survey(test_path)
  try:
    assert x_train.shape == (24, 5)
  except:
    shutil.rmtree(test_path)
    raise()
