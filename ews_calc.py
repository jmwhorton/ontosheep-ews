from importlib import import_module
import os
import requests

if not os.path.exists('lib/temperature_conversion.py'):
    url = 'https://raw.githubusercontent.com/jmwhorton/ontosheep-conversion/main/conversions/temperature/temperature_conversion.py'
    r = requests.get(url, allow_redirects=True)
    open('lib/temperature_conversion.py', 'wb').write(r.content)

convert = import_module('lib.temperature_conversion')

def calcqSOFA(person):
    score = 0
    respiratoryRate = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#respiratory_rate_measurement_datum']['value'])
    bp = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#systolic_blood_pressure_measurement_datum']['value'])
    gcs = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#glasgow_coma_scale_measurement_datum']['value'])

    if respiratoryRate >= 22:
        score += 1

    if gcs < 15:
        score += 1

    if bp <= 100:
        score += 1

    return score

def calcMEWS(person):
    person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#body_temperature_measurment_datum'] = convert.ensureCelsius(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#body_temperature_measurment_datum'])

    score = 0
    respiratoryRate = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#respiratory_rate_measurement_datum']['value'])
    oxySat = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#oxygen_saturation_measurement_datum']['value'])
    temp = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#body_temperature_measurment_datum']['value'])
    bp = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#systolic_blood_pressure_measurement_datum']['value'])
    pulse = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#heart_rate_measurement_datum']['value'])
    conciousness = (person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#AVPU_measurement_datum']['value'])
    urine = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#urine_output_measurement_datum']['value'])

    if respiratoryRate > 30:
        score +=3
    elif respiratoryRate >= 25:
        score +=2
    elif respiratoryRate >=20:
        score += 1 
    elif respiratoryRate >= 14:
        score += 0
    elif respiratoryRate >= 10:
        score += 1
    else:
        score += 2 

    if bp >= 200:
        score += 2 
    elif bp >= 160:
        score += 1
    elif bp >= 110:
        score += 0 
    elif bp >= 80:
        score += 1
    elif bp >= 70:
        score += 2
    else:
        score += 3

    if pulse >= 131:
        score += 3
    elif pulse >= 120:
        score += 2
    elif pulse >= 100:
        score += 1
    elif pulse >= 50:
        score += 0
    elif pulse >= 40:
        score += 1
    else:
        score += 2 

    if temp > 39:
        score += 2
    elif temp >= 38:
        score += 1
    elif temp >= 36:
        score += 0
    elif temp >= 35:
        score += 1
    else:
        score += 2 

    if urine > 300:
        score += 3
    elif urine >= 201:
        score += 2
    elif urine >= 30:
        score += 0
    elif urine >= 10:
        score +=1 
    else: 
        score += 3

    if conciousness == 'Unresponsive':
        score += 3
    elif conciousness == 'Pain':
        score += 2
    elif conciousness == 'Vocal':
        score += 1

    if oxySat < 88:
        score += 3
    elif oxySat <= 91:
        score += 2
    elif oxySat <= 95:
        score += 1

    return score

def calcNEWS(person):
    person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#body_temperature_measurment_datum'] = convert.ensureCelsius(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#body_temperature_measurment_datum'])

    score = 0
    respiratoryRate = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#respiratory_rate_measurement_datum']['value'])
    oxySat = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#oxygen_saturation_measurement_datum']['value'])
    supplementalOxy = (person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#supplemental_oxygen_use_measurement_datum']['value'])
    temp = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#body_temperature_measurment_datum']['value'])
    bp = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#systolic_blood_pressure_measurement_datum']['value'])
    pulse = float(person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#heart_rate_measurement_datum']['value'])
    conciousness = (person['http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#AVPU_measurement_datum']['value'])

    if respiratoryRate >= 25:
        score +=3
    elif respiratoryRate >= 21:
        score +=2
    elif respiratoryRate >=12:
        score += 0
    elif respiratoryRate >= 9:
        score += 1
    else:
        score += 3

    if oxySat <= 91:
        score += 3
    elif oxySat <= 93:
        score += 2
    elif oxySat < 96:
        score += 1

    if supplementalOxy == 'true':
        score += 2

    if temp >= 39.1:
        score += 2
    elif temp >= 38.1:
        score += 1
    elif temp >= 36.1:
        score += 0
    elif temp >= 35.1:
        score += 1
    else:
        score += 3

    if bp >= 220:
        score += 3
    elif bp >= 111:
        score += 0
    elif bp >= 101:
        score += 1
    elif bp >= 91:
        score += 2
    else:
        score += 3

    if pulse >= 131:
        score += 2
    elif pulse >= 111:
        score += 1
    elif pulse >= 91:
        score += 0
    elif pulse >= 51:
        score += 1
    elif pulse >= 41:
        score += 2
    else:
        score += 3

    if not conciousness == 'Alert':
        score += 3



    return(score)

def run(person, spec):
    meetsReqs = {}
    results = {} 
    for key in spec:
        hasRequirements = True
        for requirement in spec[key]['requirements']: 
            if requirement['uri'] not in person:
                hasRequirements = False

        meetsReqs[key] = hasRequirements


    if meetsReqs['NEWS']:
        results['NEWS'] = calcNEWS(person)
    if meetsReqs['MEWS']:
        results['MEWS'] = calcMEWS(person)
    if meetsReqs['qSOFA']:
        results['qSOFA'] = calcqSOFA(person)

    return results

