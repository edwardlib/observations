from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.survey import survey


def test_survey():
  """Test module survey.py by downloading
   survey.csv and testing shape of
   extracted data has 237 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = survey(test_path)
  try:
    assert x_train.shape == (237, 12)
  except:
    shutil.rmtree(test_path)
    raise()
