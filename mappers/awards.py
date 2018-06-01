# from mappers.util import MapperUtil


class AwardMapper:

    @staticmethod
    def map_award(award_title):
        organization_mapping = {
            "Academy": "Academy of Motion Picture Arts and Sciences",
            "BAFTA": "British Academy of Film and Television Arts",
            "César": "Académie des Arts et Techniques du Cinéma",
            "Amanda": "Norwegian International Film Festival"
        }

        # trophy_mapping = {
        #     "Academy": "Oscar",
        #     "BAFTA": "BAFTA Award",
        #     "César": "César Award",
        #     "Amanda": "Amanda Award"
        # }

        trophy_mapping = {
            "Academy": "Academy Award",
            "BAFTA": "BAFTA Award",
            "César": "César Award",
            "Amanda": "Amanda Award"
        }

        category_mapping = {
            "Best Actor": "Best Actor",
            "Best Actress": "Best Actress",
            "Best Adapted Screenplay": "Best Adapted Screenplay",
            "Best Animated Feature": "Best Animated Feature",
            "Best Animated Short": "Best Animated Short",
            "Best Art Direction": "Best Art Direction",
            "Best Arts Documentary": "Best Arts Documentary",
            "Best Biography Documentary": "Best Biography Documentary",
            "Best Cinematography": "Best Cinematography",
            "Best Costume Design": "Best Costume Design",
            "Best Directing in an Animated Television Productio": "Best Directing in an Animated Television Productio",
            "Best Director": "Best Director",
            "Best Documentary Feature": "Best Documentary Feature",
            "Best Documentary Short": "Best Documentary Short",
            "Best Editing": "Best Editing",
            "Best First Feature Film": "Best First Feature Film",
            "Best Foreign Language Film": "Best Foreign Language Film",
            "Best Horror Film": "Best Horror Film",
            "Best Makeup": "Best Makeup",
            "Best Motion Picture - Drama": "Best Motion Picture - Drama",
            "Best Motion Picture - Musical or Comedy": "Best Motion Picture - Musical or Comedy",
            "Best Original Score": "Best Original Score",
            "Best Original Screenplay": "Best Original Screenplay",
            "Best Original Song": "Best Original Song",
            "Best Picture": "Best Picture",
            "Best Presentation on Television": "Best Presentation on Television",
            "Best Sound Editing": "Best Sound Editing",
            "Best Sound Mixing": "Best Sound Mixing",
            "Best Supporting Actor": "Best Supporting Actor",
            "Best Supporting Actress": "Best Supporting Actress",
            "Best Television Series - Musical or Comedy": "Best Television Series - Musical or Comedy",
            "Best Visual Effects": "Best Visual Effects",
            "Critics' Choice": "Critics' Choice",
            "Newcomer of the Year": "Newcomer of the Year",
            "Outstanding Drama Series": "Outstanding Drama Series",
            "Outstanding Lead Actor in a Comedy Series": "Outstanding Lead Actor in a Comedy Series",
            "Outstanding Supporting Actor": "Outstanding Supporting Actor",
            "People's Choice": "People's Choice",
            "Best Sound": "Best Sound",
            "Best Foreign Film": "Best Foreign Film",
            "Best Makeup and Hair": "Best Makeup and Hair",
            "Best Makeup and Hairstyling": "Best Makeup and Hairstyling",
            "Best Production Design": "Best Production Design",
            "Best Writing, Adapted Screenplay": "Best Writing, Adapted Screenplay",
            "Best Foreign Feature Film": "Best Foreign Feature Film",
            "Best Film Editing": "Best Film Editing",
            "Best Cinematography, Color": "Best Cinematography, Color",
            "Best Score, Adaptation or Treatment": "Best Score, Adaptation or Treatment",
            "Best Film": "Best Film",
            "Best Writing, Original Screenplay": "Best Writing, Original Screenplay",
            "Best Original Song Score": "Best Original Song Score",
            "Best Cinematography, Black-and-White": "Best Cinematography, Black-and-White",
            "Best Art Direction, Color": "Best Art Direction, Color",
            "Best Original Musical Score": "Best Original Musical Score",
            "Best Costume Design, Color": "Best Costume Design, Color",
            "Best Costume Design, Black-and-White": "Best Costume Design, Black-and-White",
            "Best Art Direction, Black and White": "Best Art Direction, Black and White",
        }

        organization = None
        trophy = None
        category = None

        if award_title.find(" Award for") > 0:
            organization = organization_mapping.get(award_title[:award_title.index(" Award for")])
            trophy = trophy_mapping.get(award_title[:award_title.index(" Award for")])
            raw_category = award_title[award_title.index(" Award for " ) +len(" Award for "):]
            category = category_mapping.get(raw_category, None)

        else:
            print(award_title)
            # quit()

        if organization and trophy and category:
            award = {
                "organization": organization,
                "trophy": trophy,
                "category": category
            }

            return award
        else:
            print(award_title)

