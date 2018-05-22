from functools import reduce
import operator
from more_itertools import unique_everseen
from formatters.common import CommonFormatters


class Mappers:
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

        return Mappers.map_list(genre_list, mapping)

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
            'BS': 'Bahamas',
            'BH': 'Bahrain',
            'BD': 'Bangladesh',
            'BY': 'Belarus',
            'BE': 'Belgium',
            'BZ': 'Belize',
            'BJ': 'Benin',
            'BT': 'Bhutan',
            'BO': 'Boliva',
            'BA': 'Bosnia and Herzegovina',
            'BW': 'Botswana',
            'BR': 'Brazil',
            'BN': 'Brunei',
            'BG': 'Bulgaria',
            'BF': 'Burkina-Faso',
            'BI': 'Burundi',
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
            'MK': 'Macdeonia',
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
            'EH': 'Western Sahara',
            'YE': 'Yemen',
            'ZM': 'Zambia',
            'ZW': 'Zimbabwe'
        }
        return Mappers.map_list(countries, mapping)

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
            6: "Television",
        }

        timeline = []
        # print(release_dates)
        for territory in release_dates['results']:
            for release_date in territory['release_dates']:
                data = {
                    "type": type_mapping.get(release_date['type']),
                    # This is a convoluted way to map a single country
                    "territory": Mappers.map_countries([territory['iso_3166_1']])[0],
                    "media": media_mapping.get(release_date['type']),
                    "start_date": CommonFormatters.format_date(release_date['release_date']),
                    "note": release_date.get('note', '')
                }
                timeline.append(data)

        return timeline
