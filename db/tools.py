from datetime import datetime

def normalize_date(date):
    formats = ['%Y', '%Y-%m', '%Y-%m-%d']
    for format in formats:
        try:
            date_ = datetime.strptime(date, format)
            print(f'normalized: {date_.strftime('%Y-%m-%d')}')
            #print(date_.__str__)
            return date_.strftime('%Y-%m-%d')
        except:
            pass
    return None