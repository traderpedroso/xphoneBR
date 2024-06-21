import re
from num2words import num2words

# Regular expression matching whitespace:
_whitespace_re = re.compile(r"\s+")

rep_map = {
    "：": ",",
    "；": ",",
    "，": ",",
    "。": ".",
    "！": "!",
    "？": "?",
    "\n": ".",
    "·": ",",
    "、": ",",
    "...": ".",
    "…": ".",
    "$": ".",
    "“": "'",
    "”": "'",
    "‘": "'",
    "’": "'",
    "（": "'",
    "）": "'",
    "(": "'",
    ")": "'",
    "《": "'",
    "》": "'",
    "【": "'",
    "】": "'",
    "[": "'",
    "]": "'",
    "—": "",
    "～": "-",
    "~": "-",
    "「": "'",
    "」": "'",
    "& ": " e ",
}

# Lista de pares (expressão regular, substituição) para abreviações em português do Brasil:
abbreviations = [
    (re.compile(r"\b%s\b" % re.escape(x[0]), re.IGNORECASE), x[1])
    for x in [
        ("sr", "senhor"),
        ("sra", "senhora"),
        ("dr", "doutor"),
        ("dra", "doutora"),
        ("prof", "professor"),
        ("eng", "engenheiro"),
        ("ltda", "limitada"),
        ("adv", "advogado"),
        ("etc.", "etcetera"),
        ("kb", "kilobyte"),
        ("gb", "gigabyte"),
        ("mb", "megabyte"),
        ("kw", "quilowatt"),
        ("mw", "megawatt"),
        ("gw", "gigawatt"),
        ("kg", "quilograma"),
        ("hz", "hertz"),
        ("khz", "quilo-hertz"),
        ("mhz", "mega-hertz"),
        ("ghz", "giga-hertz"),
        ("km", "quilômetro"),
        ("ltda", "limitada"),
        ("jan", "janeiro"),
        ("fev", "fevereiro"),
        ("mar", "março"),
        ("abr", "abril"),
        ("mai", "maio"),
        ("jun", "junho"),
        ("jul", "julho"),
        ("ago", "agosto"),
        ("set", "setembro"),
        ("out", "outubro"),
        ("nov", "novembro"),
        ("dez", "dezembro"),
        ("pág", "página"),
        ("págs", "páginas"),
        ("s.a", "sociedade anônima"),
        ("cia", "companhia"),
        ("etc", "et cetera"),
    ]
]


def replace_punctuation(text):
    pattern = re.compile("|".join(re.escape(p) for p in rep_map.keys()))
    replaced_text = pattern.sub(lambda x: rep_map[x.group()], text)
    return replaced_text


def lowercase(text):
    return text.lower()


def collapse_whitespace(text):
    return re.sub(_whitespace_re, " ", text).strip()


def remove_punctuation_at_begin(text):
    return re.sub(r"^[,.!?]+", "", text)


def remove_aux_symbols(text):
    text = re.sub(r"[\<\>\(\)\[\]\"\«\»\']+", "", text)
    return text


def _normalize_percentages(text):
    return re.sub(
        r"(\d+)%", lambda m: num2words(m.group(1), lang="pt") + " por cento", text
    )


def _normalize_time(text):
    def time_to_words(match):
        hours = int(match.group(1))
        minutes = int(match.group(2))
        hours_text = num2words(hours, lang="pt", to="cardinal")
        if minutes == 0:
            return f"{hours_text} hora" + ("s" if hours > 1 else "")
        minutes_text = num2words(minutes, lang="pt", to="cardinal")
        return (
            f"{hours_text} hora"
            + ("s" if hours > 1 else "")
            + f" e {minutes_text} minuto"
            + ("s" if minutes > 1 else "")
        )

    return re.sub(r"(\d{1,2}):(\d{2})", time_to_words, text)


def _normalize_money(text):
    def money_to_words_millions(match):
        currency = match.group(1)
        integer_part = match.group(2).replace(".", "")
        suffix = match.group(3)

        amount_text = num2words(int(integer_part), lang="pt")
        return f"{amount_text} {suffix} de reais"

    def money_to_words_cents(match):
        currency = match.group(1)
        integer_part = match.group(2).replace(".", "")
        decimal_part = match.group(3)

        integer_amount_text = num2words(int(integer_part), lang="pt")
        decimal_amount_text = num2words(int(decimal_part), lang="pt")
        return f"{integer_amount_text} reais e {decimal_amount_text} centavos"

    def money_to_words_integers(match):
        currency = match.group(1)
        integer_part = match.group(2).replace(".", "")

        amount = int(integer_part)
        amount_text = num2words(amount, lang="pt")

        if amount > 1:
            currency_text = "reais"
        else:
            currency_text = "real"

        return f"{amount_text} {currency_text}"

    # Expressão regular para valores com milhões e bilhões
    text = re.sub(r"(R\$|€|£|\$) (\d+)( milhões| bilhões)", money_to_words_millions, text)
    text = re.sub(r"(R\$|€|£|\$)(\d+)( milhões| bilhões)", money_to_words_millions, text)

    # Expressão regular para valores com centavos
    text = re.sub(r"(R\$|€|£|\$) (\d+),(\d{2})", money_to_words_cents, text)
    text = re.sub(r"(R\$|€|£|\$)(\d+),(\d{2})", money_to_words_cents, text)

    # Expressão regular para valores inteiros
    text = re.sub(r"(R\$|€|£|\$) (\d+)", money_to_words_integers, text)
    text = re.sub(r"(R\$|€|£|\$)(\d+)", money_to_words_integers, text)

    return text


def _normalize_numbers(text):
    return re.sub(r"\b\d+\b", lambda x: num2words(x.group(), lang="pt"), text)


def _normalize_abbreviations(text):
    for regex, substitution in abbreviations:
        text = regex.sub(substitution, text)
    return text


def _normalize_am_pm_times(text):
    def am_pm_to_words(match):
        hours = int(match.group(1))
        period = match.group(2).lower()
        if period == "pm" and hours != 12:
            hours += 12
        elif period == "am" and hours == 12:
            hours = 0
        hours_text = num2words(hours, lang="pt", to="cardinal")
        return f"{hours_text} horas"

    return re.sub(r"(\d{1,2})(am|pm)", am_pm_to_words, text)


def _normalize_numbers_with_letters(text):
    return re.sub(
        r"(\d+)([a-zA-Z]+)",
        lambda m: f"{num2words(m.group(1), lang='pt')} {m.group(2)}",
        text,
    )



def normalizer(text):
        text = _normalize_percentages(text)
        text = _normalize_time(text)
        text = _normalize_money(text)
        text = _normalize_am_pm_times(text)
        text = _normalize_numbers_with_letters(text)
        text = _normalize_numbers(text)
        text = _normalize_abbreviations(text)
        text = replace_punctuation(text)
        text = remove_aux_symbols(text)
        text = remove_punctuation_at_begin(text)
        text = collapse_whitespace(text)
        text = re.sub(r"([^\.,!\?\-…])$", r"\1.", text)
        return text
