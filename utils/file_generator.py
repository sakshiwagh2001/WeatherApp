# C:\Users\saksh\Desktop\Weather App\weather_project\utils\file_generator.py


def generate_weather_txt(records):
    lines = []
    header = "Region\tParameter\tYear\tJan\tFeb\tMar\tApr\tMay\tJun\tJul\tAug\tSep\tOct\tNov\tDec\tAnnual"
    lines.append(header)

    for record in records:
        line = f"{record.region}\t{record.parameter}\t{record.year}\t{record.jan}\t{record.feb}\t{record.mar}\t{record.apr}\t{record.may}\t{record.jun}\t{record.jul}\t{record.aug}\t{record.sep}\t{record.oct}\t{record.nov}\t{record.dec}\t{record.annual}"
        lines.append(line)

    return "\n".join(lines)
