import re
from datetime import date, datetime


class CommonFormatters:
    @staticmethod
    def format_project_title(project_title):
        project_title = re.sub(r'^The (.*)', r'\1, The', project_title)
        project_title = re.sub(r'^A (.*)', r'\1, A', project_title)
        project_title = re.sub(r'^An (.*)', r'\1, An', project_title)

        return project_title

    @staticmethod
    def format_date(input_date):
        if "T" in input_date:
            input_date = input_date[:input_date.index("T")]

        output_date = datetime.strptime(input_date, "%Y-%m-%d").date().strftime("%m/%d/%Y")

        return output_date

    @staticmethod
    def format_date_year_only(input_date):
        if "T" in input_date:
            input_date = input_date[:input_date.index("T")]

        output_date = datetime.strptime(input_date, "%Y-%m-%d").date().strftime("%Y")

        return output_date

    @staticmethod
    def format_language(input_language):
        mapping = {
            "af": "Afrikaans",
            "sq": "Albanian",
            "ar": "Arabic",
            "hy": "Armenian",
            "az": "Azeri",
            "eu": "Basque",
            "be": "Belarusian",
            "bg": "Bulgarian",
            "ca": "Catalan",
            "hr": "Croatian",
            "cs": "Czech",
            "da": "Danish",
            "dv": "Dhivehi",
            "nl": "Dutch",
            "en": "English",
            "et": "Estonian",
            "fo": "Faroese",
            "fa": "Farsi",
            "fil": "Filipino",
            "fi": "Finnish",
            "fr": "French",
            "ga": "Gaelic",
            "gl": "Galician",
            "ka": "Georgian",
            "de": "German",
            "el": "Greek",
            "gu": "Gujarati",
            "he": "Hebrew",
            "hi": "Hindi",
            "hu": "Hungarian",
            "is": "Icelandic",
            "id": "Indonesian",
            "iu": "Inuit",
            "it": "Italian",
            "ja": "Japanese",
            "kn": "Kannada",
            "kk": "Kazakh",
            "kok": "Konkani",
            "ko": "Korean",
            "ky": "Kyrgyz",
            "lv": "Latvian",
            "lt": "Lithuanian",
            "mk": "Macedonian",
            "ms": "Malay",
            "mr": "Marathi",
            "mn": "Mongolian",
            "no": "Norwegian",
            "pl": "Polish",
            "pt": "Portuguese",
            "pa": "Punjabi",
            "ro": "Romanian",
            "ru": "Russian",
            "sa": "Sanskrit",
            "sr": "Serbian",
            "sk": "Slovak",
            "sl": "Slovenian",
            "es": "Spanish",
            "sw": "Swahili",
            "sv": "Swedish",
            "syr": "Syriac",
            "ta": "Tamil",
            "tt": "Tatar",
            "te": "Telugu",
            "th": "Thai",
            "bo": "Tibetan",
            "tr": "Turkish",
            "uk": "Ukrainian",
            "ur": "Urdu",
            "uz": "Uzbek",
            "vi": "Vietnamese",
            "zu": "Zulu"
        }

        output = mapping.get(input_language, None)
        return output

    @staticmethod
    def format_languages(languages: [str]):
        return [CommonFormatters.format_language(language) for language in languages]

    @staticmethod
    def format_movie_project_status(status):
        mapping = {
            'Planned': 'Development',
            'In Production': 'Production',
            'Post Production': 'Post-Production',
            'Released': 'Catalog'
        }

        output = mapping.get(status, None)
        return output
