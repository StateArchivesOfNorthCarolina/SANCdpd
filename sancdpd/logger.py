"""
This module creates and manages the runtime log files for SANCdpd.
"""

import conf


def begin():
    """
    Create a new timestamped log file.
    Begin logging by writing the first line to it.
    """
