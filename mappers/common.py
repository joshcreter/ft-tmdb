from functools import reduce
import operator
from more_itertools import unique_everseen
from formatters import CommonFormatters


class CommonMappers:
    @staticmethod
    def map_list(source_list, mapping_dict):
        output = []

        for item in source_list:
            mapped_item = mapping_dict.get(item, item)

            # If the item is not mapped, wrap it in a list
            # Doing this prevents the unmapped item string from exploding into single characters in the next step
            if isinstance(mapped_item, list):
                output.append(mapped_item)
            else:
                output.append([mapped_item])

        if output:
            # Now flatten the list of lists into a simple list
            output = reduce(operator.add, output)

            # Next deduplicate the flattened list
            output = list(unique_everseen(output))

            # Filter out blank items
            output = list(filter(None, output))

        return output

    @staticmethod
    def map_genres(genres):
        mapping = {
            "Sci-Fi & Fantasy": ["Sci-Fi", "Fantasy"],
            "Action & Adventure": ["Action", "Adventure"],
            "Science Fiction": "Sci-Fi"
        }

        genre_list = []
        for genre in genres:
            genre_list.append(genre['name'])

        return CommonMappers.map_list(genre_list, mapping)

    @staticmethod
    def map_countries(countries):
        # mapping = {
        #     "AU": "Australia",
        #     "GB": "United Kingdom",
        #     "MT": "Malta",
        #     "US": "United States of America",
        #     "CA": "Canada",
        #     "ES": "Spain",
        #     "JP": "Japan",
        #     "DE": "Germany"
        # }

        mapping = {
            'AF': 'Afghanistan',
            'AL': 'Albania',
            'DZ': 'Algeria',
            'AO': 'Angola',
            'AR': 'Argentina',
            'AU': 'Australia',
            'AT': 'Austria',
            'AZ': 'Azerbaijan',
            'BS': 'Bahamas',
            'BH': 'Bahrain',
            'BD': 'Bangladesh',
            'BY': 'Belarus',
            'BE': 'Belgium',
            'BZ': 'Belize',
            'BJ': 'Benin',
            'BT': 'Bhutan',
            'BO': 'Bolivia',
            'BA': 'Bosnia and Herzegovina',
            'BW': 'Botswana',
            'BR': 'Brazil',
            'BN': 'Brunei',
            'BG': 'Bulgaria',
            'BF': 'Burkina-Faso',
            'BI': 'Burundi',
            'KH': 'Cambodia',
            'CM': 'Cameroon',
            'CA': 'Canada',
            'CF': 'Central Africa Republic',
            'TD': 'Chad',
            'CL': 'Chile',
            'CN': 'China',
            'CO': 'Colombia',
            'CG': 'Congo',
            'CD': 'Congo',
            'CR': 'Costa Rica',
            'CI': 'Ivory Coast',
            'HR': 'Croatia',
            'CU': 'Cuba',
            'CY': 'Cyprus',
            'CZ': 'Czech Republic',
            'DK': 'Denmark',
            'DJ': 'Djibouti',
            'DO': 'Dominican Republic',
            'EC': 'Ecuador',
            'EG': 'Egypt',
            'SV': 'El Salvador',
            'GQ': 'Equatorial Guinea',
            'ER': 'Eritrea',
            'EE': 'Estonia',
            'ET': 'Ethiopia',
            'FJ': 'Fiji',
            'FI': 'Finland',
            'FR': 'France',
            'GF': 'French Guyana',
            'GA': 'Gabon',
            'GM': 'Gambia',
            'GE': 'Georgia',
            'DE': 'Germany',
            'GH': 'Ghana',
            'GR': 'Greece',
            'GT': 'Guatemala',
            'GN': 'Guinea',
            'GY': 'Guyana',
            'HT': 'Haiti',
            'HN': 'Honduras',
            'HK': 'Hong Kong',
            'HU': 'Hungary',
            'IS': 'Iceland',
            'IN': 'India',
            'ID': 'Indonesia',
            'IR': 'Iran',
            'IQ': 'Iraq',
            'IE': 'Ireland',
            'IL': 'Israel',
            'IT': 'Italy',
            'JM': 'Jamaica',
            'JP': 'Japan',
            'JO': 'Jordan',
            'KZ': 'Kazakhstan',
            'KE': 'Kenya',
            'KP': 'North Korea',
            'KR': 'South Korea',
            'KW': 'Kuwait',
            'KG': 'Kyrgyzstan',
            'LV': 'Latvia',
            'LB': 'Lebanon',
            'LS': 'Lesotho',
            'LR': 'Liberia',
            'LY': 'Libya',
            'LT': 'Lithuania',
            'LU': 'Luxembourg',
            'MK': 'Macedonia',
            'MG': 'Madagascar',
            'MW': 'Malawi',
            'MY': 'Malaysia',
            'MV': 'Maldives, The',
            'ML': 'Mali',
            'MT': 'Malta',
            'MR': 'Mauritania',
            'MU': 'Mauritius',
            'MX': 'Mexico',
            'FM': 'Micronesia',
            'MD': 'Moldova',
            'MC': 'Monaco',
            'MN': 'Mongolia',
            'ME': 'Serbia and Montenegro',
            'MA': 'Morocco',
            'MZ': 'Mozambique',
            'MM': 'Myanmar (Burma)',
            'NA': 'Namibia',
            'NL': 'Netherlands, The',
            'NZ': 'New Zealand',
            'NI': 'Nicaragua',
            'NE': 'Niger',
            'NG': 'Nigeria',
            'NO': 'Norway',
            'OM': 'Oman',
            'PK': 'Pakistan',
            'PS': 'Palestinian Authority',
            'PA': 'Panama',
            'PG': 'Papua New Guinea',
            'PY': 'Paraguay',
            'PE': 'Peru',
            'PH': 'Philippines',
            'PL': 'Poland',
            'PT': 'Portugal',
            'PR': 'Puerto Rico',
            'QA': 'Qatar',
            'RO': 'Romania',
            'RU': 'Russia',
            'RW': 'Rwanda',
            'SA': 'Saudi Arabia',
            'SN': 'Senegal',
            'RS': 'Serbia and Montenegro',
            'SL': 'Sierra Leone',
            'SG': 'Singapore',
            'SK': 'Slovakia',
            'SI': 'Slovenia',
            'SO': 'Somalia',
            'ZA': 'South Africa',
            'ES': 'Spain',
            'LK': 'Sri Lanka',
            'SD': 'Sudan',
            'SZ': 'Swaziland',
            'SE': 'Sweden',
            'CH': 'Switzerland',
            'SY': 'Syria',
            'TW': 'Taiwan, Province of China',
            'TJ': 'Tajikistan',
            'TZ': 'Tanzania',
            'TH': 'Thailand',
            'TG': 'Togo',
            'TO': 'Tonga',
            'TT': 'Trinidad and Tobago',
            'TN': 'Tunisia',
            'TR': 'Turkey',
            'TM': 'Turkmenistan',
            'UG': 'Uganda',
            'UA': 'Ukraine',
            'AE': 'United Arab Emirates',
            'GB': 'United Kingdom',
            'US': 'United States of America',
            'UY': 'Uruguay',
            'UZ': 'Uzbekistan',
            'VE': 'Venezuela',
            'VN': 'Vietnam',
            'EH': 'Western Sahara',
            'YE': 'Yemen',
            'ZM': 'Zambia',
            'ZW': 'Zimbabwe',
            'SU': 'Russia',
        }
        return CommonMappers.map_list(countries, mapping)

    @staticmethod
    def map_release_dates(release_dates):
        type_mapping = {
            1: "Premiere",
            2: "Release Date",
            3: "Release Date",
            4: "Release Date",
            5: "Release Date",
            6: "Release Date",
        }

        media_mapping = {
            1: "Theatrical",
            2: "Theatrical",
            3: "Theatrical",
            4: "Internet",
            5: "DVD",
            6: "Free TV",
        }

        timeline = []
        # print(release_dates)
        for territory in release_dates['results']:
            for release_date in territory['release_dates']:
                data = {
                    "type": type_mapping.get(release_date['type']),
                    # This is a convoluted way to map a single country
                    "territory": CommonMappers.map_countries([territory['iso_3166_1']])[0],
                    "media": media_mapping.get(release_date['type']),
                    "start_date": CommonFormatters.format_date(release_date['release_date']),
                    "note": release_date.get('note', '')
                }
                timeline.append(data)

        return timeline

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
            raw_category = award_title[award_title.index(" Award for ")+len(" Award for "):]
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

