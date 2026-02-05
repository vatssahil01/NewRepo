from enum import Enum

class AudienceType(str, Enum):
    clinician = "clinician"
    researcher = "researcher"
    administrator = "administrator"

class CitationStyle(str, Enum):
    AMA = "AMA"
    APA = "APA"
    Vancouver = "Vancouver"
