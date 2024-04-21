def dummy_logger():
    message = [{
        "message": 'George Kout_347033-404701-2_535000',
        "service_name": 'fusion toolset',
        "service_type":'abnormal detection',
        "timestamp": '2021-12-15T15:30:10'
    },
    {
        "message": 'FGRJYHN1234MM_XXX-809',
        "service_name": 'fusion toolset',
        "service_type": 'driver tampering',
        "timestamp": '2021-02-17T11:19:58'
    },
    {
        "message": 'The current transaction is characterized as suspicious and needs to be furtherly investigate',
        "service_name": 'advanced reasoner',
        "service_type": 'suspicious transactions',
        "timestamp": '2021-05-19T12:49:18'
    },
    {
        "message": 'GSM Jammed',
        "service_name": 'advanced reasoner',
        "service_type": 'gsm and antenna status',
        "timestamp": '2021-10-22T13:49:18'
    },
    {
        "message": 'GPS Antenna Removal',
        "service_name": 'advanced reasoner',
        "service_type": 'gsm and antenna status',
        "timestamp": '2021-10-22T13:49:18'
    },
    {
        "message": 'An opened door was detected but there is not observed any temperature difference as it"s equal to:0.0 Celcius',
        "service_name": 'advanced reasoner',
        "service_type": 'Door & Temperature Status',
        "timestamp": '2021-10-22T13:49:18'
    }
    ]

    return message

# for n in a:
#     print(n['service_type'])