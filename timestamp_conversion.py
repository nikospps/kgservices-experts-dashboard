import datetime

def conv(dt):
    a=dt.split('T')[0]
    date_object = datetime.datetime.strptime(a, '%Y-%m-%d').date()
    dt_final = date_object.strftime('%d-%m-%Y')
    return dt_final