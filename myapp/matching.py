from random import shuffle
from .models import CustomUser, Match

def match_mentors_with_mentees():
    mentors = CustomUser.objects.filter(is_mentor=True)
    mentees = CustomUser.objects.filter(is_mentee=True)

    # Shuffle the mentors and mentees to ensure randomness in the matching process
    shuffle(list(mentors))
    shuffle(list(mentees))

    matches = []

    for mentor in mentors:
        # Filter mentees based on matching criteria (e.g., preferred language, major)
        potential_matches = mentees.filter(
            preferred_language=mentor.preferred_language,
            major=mentor.major,
            availability__in=mentor.availability.split(',')
        )

        for mentee in potential_matches:
            # Create a match and save it to the database
            match = Match.objects.create(mentor=mentor.mentor, mentee=mentee.mentee)
            matches.append(match)
            # Remove the mentee from the pool to avoid multiple matches
            mentees = mentees.exclude(pk=mentee.pk)
            break  # Break after the first successful match

    return matches
