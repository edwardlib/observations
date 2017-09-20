from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.doctor_contacts import doctor_contacts


def test_doctor_contacts():
  """Test module doctor_contacts.py by downloading
   doctor_contacts.csv and testing shape of
   extracted data has 20186 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = doctor_contacts(test_path)
  try:
    assert x_train.shape == (20186, 15)
  except:
    shutil.rmtree(test_path)
    raise()
