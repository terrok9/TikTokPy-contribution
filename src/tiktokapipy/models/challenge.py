"""
Challenge (Hashtag) data models
"""

from __future__ import annotations

from typing import Iterable, Optional

from tiktokapipy.models import CamelCaseModel


class ChallengeStats(CamelCaseModel):
    """Stats specific to a Challenge"""

    video_count: int
    view_count: int


class Challenge(CamelCaseModel):
    """Challenge data"""

    id: int
    """The Challenge's unique id"""
    title: str
    desc: str
    is_commerce: bool
    """Presumably whether this challenge is sponsored."""
    stats: ChallengeStats

    videos: Optional[Iterable[Video]]
    """Set on return from API. Can be iterated over to load :class:`.Video`s."""


from tiktokapipy.models.video import Video  # noqa E402

Challenge.update_forward_refs()


def challenge_link(challenge: str) -> str:
    """
    Get a link to extract challenge data from its name.

    e.g.: ``challenge_link("fyp")``

    :param challenge: The name of the challenge (no ``'#'``).
    :return: a link that can be used to scrape data on the challenge.
    """
    return f"https://www.tiktok.com/tag/{challenge}"
