from abc import ABCMeta
import uuid
from datetime import datetime

class Model(object):
  """
  Abstract base class for all models -
  all models should extend this class
  """
  __metaclass__ = ABCMeta

  def __init__(self):
    """
    Initializes the model with a Universal Unique
    Identifier as an id
    """
    self.id = str(uuid.uuid1())
    self.created_at=int((datetime.now()-datetime(1970,1,1)).total_seconds())

  def to_dict(self):
    """
    Dictionary representation of this Model
    """
    return vars(self)

# A unique ID (see Model class that you should be extending from)
# A name
# A description
# A list of tags (like 'laundry', 'urgent', 'etc.')
# A time of creation
# # A due date

class Task(Model):
    def __init__(self, name, description, tags, due_date):
        Model.__init__(self)
        self.name = name
        self.description = description
        self.tags = tags
        self.due_date = due_date
