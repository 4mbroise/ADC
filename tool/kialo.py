from enum import Enum
import requests

class KialoSort(Enum):
  RANK_ACTIVITY = "rank_and_latest_activity"
  VIEW          = "view_count"
  LAST_ACTIVITY = "latest_activity"


class KialoTool:
  def getTags(self):
    tags = requests.get("https://www.kialo.com/api/v1/discussiontags")
