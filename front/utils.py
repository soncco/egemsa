from datetime import datetime, timedelta, time

def fechas(fecha):
    largo = len(fecha)
    fecha = int(fecha)
    if largo != 10:
        fecha = fecha/1000
    fecha = datetime.fromtimestamp(fecha)
    tomorrow = fecha + timedelta(1)
    fecha_start = datetime.combine(fecha, time())
    fecha_end = datetime.combine(tomorrow, time())
    return fecha, fecha_end, fecha_start


def get_fecha(fecha):
    largo = len(fecha)
    fecha = int(fecha)
    if largo != 10:
        fecha = fecha/1000
    return datetime.fromtimestamp(fecha)
