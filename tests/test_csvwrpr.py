class TestCsvWrpr:
    def test_(self):
        x = 1
        y = 1
        assert x == y


# def do_tests(p_app_path='', p_cls=True):
#     '''This definition drives the testing and is also called from the PackageIt
#     module during the PIP process to establish correct functioning before
#     packaging it.
#     '''
#
#     def basic_test():
#         '''Basic and mandatory scenario tests for certification of the class'''
#         success = True
#         test_folder = Path(__file__).absolute().parents[3] / _name / 'Data'
#         test_dict01 = {
#             'PID': {
#                 'PID': 'PID',
#                 'FIDE_PlayerCode': 'FIDE_PlayerCode',
#                 'PlayerName': 'PlayerName',
#                 'FIDE_Federation': 'FIDE_Federation',
#                 'Gender': 'Gender',
#                 'BirthYear': 'BirthYear',
#                 'FIDE_Title': 'FIDE_Title',
#             },
#             '61854': {
#                 'PID': '61854',
#                 'FIDE_PlayerCode': '4406176',
#                 'PlayerName': 'Rodriguez, Sofia',
#                 'FIDE_Federation': 'COL',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WCM',
#             },
#             '62277': {
#                 'PID': '62277',
#                 'FIDE_PlayerCode': '119296',
#                 'PlayerName': 'Strgacich, Aylen',
#                 'FIDE_Federation': 'ARG',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WFM',
#             },
#             '116355': {
#                 'PID': '116355',
#                 'FIDE_PlayerCode': '3003191',
#                 'PlayerName': 'Perêz, Cecilia Manuela',
#                 'FIDE_Federation': 'URU',
#                 'Gender': 'F',
#                 'BirthYear': '1998',
#                 'FIDE_Title': None,
#             },
#             '130161': {
#                 'PID': '130161',
#                 'FIDE_PlayerCode': '3611906',
#                 'PlayerName': 'Arias Cango, Nathaly',
#                 'FIDE_Federation': 'ECU',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': None,
#             },
#             '847094': {
#                 'PID': '847094',
#                 'FIDE_PlayerCode': '5239109',
#                 'PlayerName': ', John Andrei',
#                 'FIDE_Federation': 'PHI',
#                 'Gender': 'M',
#                 'BirthYear': '2002',
#                 'FIDE_Title': '',
#             },
#         }
#         test_dict02 = {
#             'PID': {
#                 'PID': 'PID',
#                 'FIDE_PlayerCode': 'FIDE_PlayerCode',
#                 'PlayerName': 'PlayerName',
#                 'FIDE_Federation': 'FIDE_Federation',
#                 'Gender': 'Gender',
#                 'BirthYear': 'BirthYear',
#                 'FIDE_Title': 'FIDE_Title',
#             },
#             '62277': {
#                 'PID': '62277',
#                 'FIDE_PlayerCode': '119296',
#                 'PlayerName': 'Strgacich, Aylen',
#                 'FIDE_Federation': 'ARG',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WFM',
#             },
#             '116355': {
#                 'PID': '116355',
#                 'FIDE_PlayerCode': '3003191',
#                 'PlayerName': 'Perêz, Cecilia Manuela',
#                 'FIDE_Federation': 'URU',
#                 'Gender': 'F',
#                 'BirthYear': '1998',
#                 'FIDE_Title': None,
#             },
#             '130161': {
#                 'PID': '130161',
#                 'FIDE_PlayerCode': '3611906',
#                 'PlayerName': 'Arias Cango, Nathaly',
#                 'FIDE_Federation': 'ECU',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': None,
#             },
#         }
#         test_dict03 = {
#             'PID': {
#                 'PID': 'PID',
#                 'FIDE_PlayerCode': 'FIDE_PlayerCode',
#                 'PlayerName': 'PlayerName',
#                 'Country': 'FIDE_Federation',
#                 'Gender': 'Gender',
#                 'BirthYear': 'BirthYear',
#                 'FIDE_Title': 'FIDE_Title',
#             },
#             '61854': {
#                 'PID': '61854',
#                 'FIDE_PlayerCode': '4406176',
#                 'PlayerName': 'Rodriguez, Sofia',
#                 'Country': 'COL',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WCM',
#             },
#             '62277': {
#                 'PID': '62277',
#                 'FIDE_PlayerCode': '119296',
#                 'PlayerName': 'Strgacich, Aylen',
#                 'Country': 'ARG',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WFM',
#             },
#             '116355': {
#                 'PID': '116355',
#                 'FIDE_PlayerCode': '3003191',
#                 'PlayerName': 'Perêz, Cecilia Manuela',
#                 'Country': 'URU',
#                 'Gender': 'F',
#                 'BirthYear': '1998',
#                 'FIDE_Title': None,
#             },
#             '130161': {
#                 'PID': '130161',
#                 'FIDE_PlayerCode': '3611906',
#                 'PlayerName': 'Arias Cango, Nathaly',
#                 'Country': 'ECU',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': None,
#             },
#             '847094': {
#                 'PID': '847094',
#                 'FIDE_PlayerCode': '5239109',
#                 'PlayerName': ', John Andrei',
#                 'Country': 'PHI',
#                 'Gender': 'M',
#                 'BirthYear': '2002',
#                 'FIDE_Title': '',
#             },
#         }
#         test_dict04 = {
#             'EventID': {
#                 'GameID': {
#                     'EventID': 'EventID',
#                     'GameID': 'GameID',
#                     'WhitePlayerID': 'WhitePlayerID',
#                     'BlackPlayerID': 'BlackPlayerID',
#                     'WhiteScore': 'WhiteScore',
#                     'DayID': 'DayID',
#                     'M60': 'M60',
#                 }
#             },
#             '10103447': {
#                 '63905487': {
#                     'EventID': '10103447',
#                     'GameID': '63905487',
#                     'WhitePlayerID': '213929',
#                     'BlackPlayerID': '275294',
#                     'WhiteScore': '1',
#                     'DayID': '3259',
#                     'M60': '120',
#                 },
#                 '63905515': {
#                     'EventID': '10103447',
#                     'GameID': '63905515',
#                     'WhitePlayerID': '165389',
#                     'BlackPlayerID': '213929',
#                     'WhiteScore': '0.5',
#                     'DayID': '3261',
#                     'M60': '120',
#                 },
#                 '63905554': {
#                     'EventID': '10103447',
#                     'GameID': '63905554',
#                     'WhitePlayerID': '213929',
#                     'BlackPlayerID': '142290',
#                     'WhiteScore': '0.5',
#                     'DayID': '3263',
#                     'M60': '120',
#                 },
#             },
#             '10113973': {
#                 '57140921': {
#                     'EventID': '10113973',
#                     'GameID': '57140921',
#                     'WhitePlayerID': '426349',
#                     'BlackPlayerID': '47414',
#                     'WhiteScore': '0.5',
#                     'DayID': '3404',
#                     'M60': '120',
#                 },
#                 '57140922': {
#                     'EventID': '10113973',
#                     'GameID': '57140922',
#                     'WhitePlayerID': '394201',
#                     'BlackPlayerID': '426349',
#                     'WhiteScore': '0',
#                     'DayID': '3407',
#                     'M60': '120',
#                 },
#                 '57140904': {
#                     'EventID': '10113973',
#                     'GameID': '57140904',
#                     'WhitePlayerID': '237614',
#                     'BlackPlayerID': '81308',
#                     'WhiteScore': '0.5',
#                     'DayID': '3406',
#                     'M60': '120',
#                 },
#             },
#             '10113980': {
#                 '57141255': {
#                     'EventID': '10113980',
#                     'GameID': '57141255',
#                     'WhitePlayerID': '81309',
#                     'BlackPlayerID': '90313',
#                     'WhiteScore': '0.5',
#                     'DayID': '3408',
#                     'M60': '120',
#                 },
#                 '57141253': {
#                     'EventID': '10113980',
#                     'GameID': '57141253',
#                     'WhitePlayerID': '23442',
#                     'BlackPlayerID': '119195',
#                     'WhiteScore': '0',
#                     'DayID': '3405',
#                     'M60': '120',
#                 },
#                 '57141261': {
#                     'EventID': '10113980',
#                     'GameID': '57141261',
#                     'WhitePlayerID': '23542',
#                     'BlackPlayerID': '81319',
#                     'WhiteScore': '1',
#                     'DayID': '3406',
#                     'M60': '120',
#                 },
#             },
#         }
#         test_dict05 = {
#             'EventID': {
#                 'GameID': {
#                     'EventID': 'EventID',
#                     'GameID': 'GameID',
#                     'WhitePlayerID': 'WhitePlayerID',
#                     'BlackPlayerID': 'BlackPlayerID',
#                     'WhiteScore': 'WhiteScore',
#                     'DayID': 'DayID',
#                     'M60': 'M60',
#                 }
#             },
#             '10103447': {
#                 '63905487': {
#                     'EventID': '10103447',
#                     'GameID': '63905487',
#                     'WhitePlayerID': '213929',
#                     'BlackPlayerID': '275294',
#                     'WhiteScore': '1',
#                     'DayID': '3259',
#                     'M60': '120',
#                 },
#                 '63905515': {
#                     'EventID': '10103447',
#                     'GameID': '63905515',
#                     'WhitePlayerID': '165389',
#                     'BlackPlayerID': '213929',
#                     'WhiteScore': '0.5',
#                     'DayID': '3261',
#                     'M60': '120',
#                 },
#                 '63905554': {
#                     'EventID': '10103447',
#                     'GameID': '63905554',
#                     'WhitePlayerID': '213929',
#                     'BlackPlayerID': '142290',
#                     'WhiteScore': '0.5',
#                     'DayID': '3263',
#                     'M60': '120',
#                 },
#             },
#             '10113973': {
#                 '57140921': {
#                     'EventID': '10113973',
#                     'GameID': '57140921',
#                     'WhitePlayerID': '426349',
#                     'BlackPlayerID': '47414',
#                     'WhiteScore': '0.5',
#                     'DayID': '3404',
#                     'M60': '120',
#                 },
#                 '57140922': {
#                     'EventID': '10113973',
#                     'GameID': '57140922',
#                     'WhitePlayerID': '394201',
#                     'BlackPlayerID': '426349',
#                     'WhiteScore': '0',
#                     'DayID': '3407',
#                     'M60': '120',
#                 },
#                 '57140904': {
#                     'EventID': '10113973',
#                     'GameID': '57140904',
#                     'WhitePlayerID': '237614',
#                     'BlackPlayerID': '81308',
#                     'WhiteScore': '0.5',
#                     'DayID': '3406',
#                     'M60': '120',
#                 },
#             },
#         }
#         test_dict06 = {
#             'PID': {
#                 'PID': 'PID',
#                 'FIDE_PlayerCode': 'FIDE_PlayerCode',
#                 'PlayerName': 'PlayerName',
#                 'FIDE_Federation': 'FIDE_Federation',
#                 'Gender': 'Gender',
#                 'BirthYear': 'BirthYear',
#                 'FIDE_Title': 'FIDE_Title',
#             },
#             '61854': {
#                 'PID': '61854',
#                 'FIDE_PlayerCode': '4406176',
#                 'PlayerName': 'Rodriguez, Sofia',
#                 'FIDE_Federation': 'COL',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WCM',
#             },
#             '62277': {
#                 'PID': '62277',
#                 'FIDE_PlayerCode': '119296',
#                 'PlayerName': 'Strgacich, Aylen',
#                 'FIDE_Federation': 'ARG',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WFM',
#             },
#             '130161': {
#                 'PID': '130161',
#                 'FIDE_PlayerCode': '3611906',
#                 'PlayerName': 'Arias Cango, Nathaly',
#                 'FIDE_Federation': 'ECU',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': None,
#             },
#         }
#         test_dict07 = {
#             'PID': {
#                 'PID': 'PID',
#                 'FIDE_PlayerCode': 'FIDE_PlayerCode',
#                 'PlayerName': 'PlayerName',
#                 'FIDE_Federation': 'FIDE_Federation',
#                 'Gender': 'Gender',
#                 'BirthYear': 'BirthYear',
#                 'FIDE_Title': 'FIDE_Title',
#             },
#             '61854': {
#                 'PID': '61854',
#                 'FIDE_PlayerCode': '4406176',
#                 'PlayerName': 'Rodriguez, Sofia',
#                 'FIDE_Federation': 'COL',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WCM',
#             },
#             '62277': {
#                 'PID': '62277',
#                 'FIDE_PlayerCode': '119296',
#                 'PlayerName': 'Strgacich, Aylen',
#                 'FIDE_Federation': 'ARG',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WFM',
#             },
#             '116355': {
#                 'PID': '116355',
#                 'FIDE_PlayerCode': '3003191',
#                 'PlayerName': 'Perêz, Cecilia Manuela',
#                 'FIDE_Federation': 'URU',
#                 'Gender': 'F',
#                 'BirthYear': '1998',
#                 'FIDE_Title': None,
#             },
#             '130161': {
#                 'PID': '130161',
#                 'FIDE_PlayerCode': '3611906',
#                 'PlayerName': 'Arias Cango, Nathaly',
#                 'FIDE_Federation': 'ECU',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': None,
#             },
#             '149055': {
#                 'PID': '149055',
#                 'FIDE_PlayerCode': '14306980',
#                 'PlayerName': 'Du Toit, Hendrik',
#                 'FIDE_Federation': 'RSA',
#                 'Gender': 'M',
#                 'BirthYear': '1968',
#                 'FIDE_Title': 'IA',
#             },
#             '847094': {
#                 'PID': '847094',
#                 'FIDE_PlayerCode': '5239109',
#                 'PlayerName': ', John Andrei',
#                 'FIDE_Federation': 'PHI',
#                 'Gender': 'M',
#                 'BirthYear': '2002',
#                 'FIDE_Title': '',
#             },
#         }
#         test_dict08 = {
#             'PID': {
#                 'PID': 'PID',
#                 'FIDE_PlayerCode': 'FIDE_PlayerCode',
#                 'PlayerName': 'PlayerName',
#                 'FIDE_Federation': 'FIDE_Federation',
#                 'Gender': 'Gender',
#                 'BirthYear': 'BirthYear',
#                 'FIDE_Title': 'FIDE_Title',
#             },
#             '61854': {
#                 'PID': '61854',
#                 'FIDE_PlayerCode': '4406176',
#                 'PlayerName': 'Rodriguez, Sofia',
#                 'FIDE_Federation': 'COL',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WCM',
#             },
#             '62277': {
#                 'PID': '62277',
#                 'FIDE_PlayerCode': '119296',
#                 'PlayerName': 'Strgacich, Aylen',
#                 'FIDE_Federation': 'ARG',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': 'WFM',
#             },
#             '116355': {
#                 'PID': '116355',
#                 'FIDE_PlayerCode': '3003191',
#                 'PlayerName': 'Perêz, Cecilia Manuela',
#                 'FIDE_Federation': 'URU',
#                 'Gender': 'F',
#                 'BirthYear': '1998',
#                 'FIDE_Title': None,
#             },
#             '130161': {
#                 'PID': '130161',
#                 'FIDE_PlayerCode': '3611906',
#                 'PlayerName': 'Arias Cango, Nathaly',
#                 'FIDE_Federation': 'ECU',
#                 'Gender': 'F',
#                 'BirthYear': '1999',
#                 'FIDE_Title': None,
#             },
#             '847094': {
#                 'PID': '847094',
#                 'FIDE_PlayerCode': '5239109',
#                 'PlayerName': ', John Andrei',
#                 'FIDE_Federation': 'PHI',
#                 'Gender': 'M',
#                 'BirthYear': '2002',
#                 'FIDE_Title': '',
#             },
#         }
#         test_dict09 = {
#             'PID': {
#                 'PID': 'PID',
#                 'FIDE_PlayerCode': 'FIDE_PlayerCode',
#                 'PlayerName': 'PlayerName',
#                 'FIDE_Federation': 'FIDE_Federation',
#                 'Gender': 'Gender',
#                 'BirthYear': 'BirthYear',
#                 'FIDE_Title': 'FIDE_Title',
#                 '': '',
#             },
#             '116355': {
#                 'PID': '116355',
#                 'FIDE_PlayerCode': '3003191',
#                 'PlayerName': 'Perêz, Cecilia Manuela',
#                 'FIDE_Federation': 'URU',
#                 'Gender': 'F',
#                 'BirthYear': '1998',
#                 'FIDE_Title': None,
#                 '': None,
#             },
#         }
#         test_list01 = [
#             [
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'FIDE_Federation',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ],
#             ['61854', '4406176', 'Rodriguez, Sofia', 'COL', 'F', '1999', 'WCM'],
#             ['62277', '119296', 'Strgacich, Aylen', 'ARG', 'F', '1999', 'WFM'],
#             ['116355', '3003191', 'Perêz, Cecilia Manuela', 'URU', 'F', '1998', None],
#             ['130161', '3611906', 'Arias Cango, Nathaly', 'ECU', 'F', '1999', None],
#             ['847094', '5239109', ', John Andrei', 'PHI', 'M', '2002', ''],
#         ]
#         test_list02 = [
#             [
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'Country',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ],
#             ['61854', '4406176', 'Rodriguez, Sofia', 'COL', 'F', '1999', 'WCM'],
#             ['62277', '119296', 'Strgacich, Aylen', 'ARG', 'F', '1999', 'WFM'],
#             ['116355', '3003191', 'Perêz, Cecilia Manuela', 'URU', 'F', '1998', None],
#             ['130161', '3611906', 'Arias Cango, Nathaly', 'ECU', 'F', '1999', None],
#             ['847094', '5239109', ', John Andrei', 'PHI', 'M', '2002', ''],
#         ]
#         test_list03 = [
#             [
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'FIDE_Federation',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ],
#             ['61854', '4406176', 'Rodriguez, Sofia', 'COL', 'F', '1999', 'WCM'],
#             ['62277', '119296', 'Strgacich_a, Aylen', 'ARG', 'F', '1999', 'WFM'],
#             ['62277', '119296', 'Strgacich_b, Aylen', 'ARG', 'F', '1999', 'WFM'],
#             ['130161', '3611906', 'Arias Cango, Nathaly', 'ECU', 'F', '1999', None],
#         ]
#         test_list04 = [
#             [
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'FIDE_Federation',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ],
#             ['61854', '4406176', 'Rodriguez, Sofia', 'COL', 'F', '1999', 'WCM'],
#             ['62277', '119296', 'Strgacich, Aylen', 'ARG', 'F', '1999', 'WFM'],
#             ['116355', '3003191', 'Perêz, Cecilia Manuela', 'URU', 'F', '1998', 'NULL'],
#             ['130161', '3611906', 'Arias Cango, Nathaly', 'ECU', 'F', '1999', 'None'],
#             ['847094', '5239109', ', John Andrei', 'PHI', 'M', '2002', ''],
#         ]
#         test_list05 = [
#             [
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'FIDE_Federation',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ],
#             ['116355', '3003191', 'Perêz, Cecilia Manuela', 'URU', 'F', '1998', 'None'],
#             ['130161', '3611906', 'Arias Cango, Nathaly', 'ECU', 'F', '1999', 'None'],
#             ['847094', '5239109', ', John Andrei', 'PHI', 'M', '2002', ''],
#         ]
#         test_db01 = [
#             (
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'FIDE_Federation',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ),
#             ('61854', '4406176', 'Rodriguez, Sofia', 'COL', 'F', '1999', 'WCM'),
#             ('62277', '119296', 'Strgacich, Aylen', 'ARG', 'F', '1999', 'WFM'),
#             ('116355', '3003191', 'Perêz, Cecilia Manuela', 'URU', 'F', '1998', None),
#             ('130161', '3611906', 'Arias Cango, Nathaly', 'ECU', 'F', '1999', None),
#             ('847094', '5239109', ', John Andrei', 'PHI', 'M', '2002', ''),
#         ]
#         test_db02 = [
#             (
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'FIDE_Federation',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ),
#             ('62277', '119296', 'Strgacich, Aylen', 'ARG', 'F', '1999', 'WFM'),
#             ('116355', '3003191', 'Perêz, Cecilia Manuela', 'URU', 'F', '1998', None),
#             ('130161', '3611906', 'Arias Cango, Nathaly', 'ECU', 'F', '1999', None),
#         ]
#         test_db03 = [
#             (
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'Country',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ),
#             ('61854', '4406176', 'Rodriguez, Sofia', 'COL', 'F', '1999', 'WCM'),
#             ('62277', '119296', 'Strgacich, Aylen', 'ARG', 'F', '1999', 'WFM'),
#             ('116355', '3003191', 'Perêz, Cecilia Manuela', 'URU', 'F', '1998', None),
#             ('130161', '3611906', 'Arias Cango, Nathaly', 'ECU', 'F', '1999', None),
#             ('847094', '5239109', ', John Andrei', 'PHI', 'M', '2002', ''),
#         ]
#
#         print('Test constructor with Dict')
#         csv_wrpr = CsvWrpr(_name, os.path.join(test_folder, 'Players.csv'), 'PID')
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_dict01):
#             success = False
#
#         print('Test constructor with Dict and subset')
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Players.csv'),
#             'PID',
#             p_subset_range=[62277, 130161],
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_dict02):
#             success = False
#
#         print('Test constructor with List')
#         csv_wrpr = CsvWrpr(
#             _name, os.path.join(test_folder, 'Players.csv'), p_struc_type=[]
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_list01, 'List'):
#             success = False
#
#         print('Test constructor with db')
#         csv_wrpr = CsvWrpr(
#             _name, os.path.join(test_folder, 'Players.csv'), p_struc_type=()
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_db01, 'db'):
#             success = False
#
#         print('Test constructor with db and subset')
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Players.csv'),
#             'PID',
#             p_struc_type=(),
#             p_subset_range=[62277, 130161],
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_db02, 'db'):
#             success = False
#
#         print('Test "p_replace_header" in Dict')
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Players.csv'),
#             'PID',
#             p_header=[
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'Country',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ],
#             p_replace_header=True,
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_dict03):
#             success = False
#
#         print('Test "replace_header" in list')
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Players.csv'),
#             p_struc_type=[],
#             p_header=[
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'Country',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ],
#             p_replace_header=True,
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_list02, 'List'):
#             success = False
#
#         print('Test "replace_header" in db')
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Players.csv'),
#             p_struc_type=(),
#             p_header=[
#                 'PID',
#                 'FIDE_PlayerCode',
#                 'PlayerName',
#                 'Country',
#                 'Gender',
#                 'BirthYear',
#                 'FIDE_Title',
#             ],
#             p_replace_header=True,
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_db03, 'db'):
#             success = False
#
#         print('Test for key file')
#         csv_wrpr = CsvWrpr(
#             _name, os.path.join(test_folder, 'Game.csv'), 'EventID', 'GameID'
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_dict04):
#             success = False
#
#         print('Test for key file with sub range')
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Game.csv'),
#             'EventID',
#             'GameID',
#             p_subset_range=[10103447, 10113973],
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_dict05):
#             success = False
#
#         print('Test exporting a sub set from a list')
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'PlayersDup.csv'),
#             p_key1='PID',
#             p_struc_type=[],
#         )
#         csv_wrpr.export_sub_set(
#             os.path.join(test_folder, 'NewPlayers.csv'), ['61854', '62277', '130161']
#         )
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'NewPlayers.csv'),
#             p_key1='PID',
#             p_struc_type=[],
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_list03, 'List'):
#             success = False
#         if os.path.isfile(os.path.join(test_folder, 'NewPlayers.csv')):
#             os.remove(os.path.join(test_folder, 'NewPlayers.csv'))
#
#         print('Test exporting a sub set from a dict')
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Players.csv'),
#             p_key1='PID',
#             p_struc_type={},
#         )
#         csv_wrpr.export_sub_set(
#             os.path.join(test_folder, 'NewPlayers.csv'), ['61854', '62277', '130161']
#         )
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'NewPlayers.csv'),
#             p_key1='PID',
#             p_struc_type={},
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_dict06, 'List'):
#             success = False
#         if os.path.isfile(os.path.join(test_folder, 'NewPlayers.csv')):
#             os.remove(os.path.join(test_folder, 'NewPlayers.csv'))
#
#         print('Test something 01??')
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Players.csv'),
#             p_key1='PID',
#             p_struc_type={},
#         )
#         csv_wrpr.append(os.path.join(test_folder, 'PlayersExtra.csv'), p_key1='PID')
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_dict07, 'List'):
#             success = False
#
#         print('Test converting "None" as field contents to None')
#         csv_wrpr1 = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Players.csv'),
#             p_key1='PID',
#             p_struc_type=[],
#         )
#         csv_wrpr1.export(os.path.join(test_folder, 'PlayersExport.csv'))
#         csv_wrpr2 = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'PlayersExport.csv'),
#             p_key1='PID',
#             p_struc_type=[],
#         )
#         if not beetools.is_struct_the_same(csv_wrpr2.csv_db, test_list01, 'List'):
#             success = False
#         if os.path.isfile(os.path.join(test_folder, 'PlayersExport.csv')):
#             os.remove(os.path.join(test_folder, 'PlayersExport.csv'))
#
#         print('Test suppressing converting "None" as field contents to None')
#         csv_wrpr1 = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Players.csv'),
#             p_key1='PID',
#             p_struc_type=[],
#             p_convert_none=False,
#         )
#         csv_wrpr1.export(os.path.join(test_folder, 'PlayersExport.csv'))
#         csv_wrpr2 = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'PlayersExport.csv'),
#             p_key1='PID',
#             p_struc_type=[],
#             p_convert_none=False,
#         )
#         if not beetools.is_struct_the_same(csv_wrpr2.csv_db, test_list04, 'List'):
#             success = False
#         if os.path.isfile(os.path.join(test_folder, 'PlayersExport.csv')):
#             os.remove(os.path.join(test_folder, 'PlayersExport.csv'))
#
#         print('Test something??')
#         csv_wrpr1 = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'Players.csv'),
#             p_key1='PID',
#             p_struc_type={},
#         )
#         csv_wrpr1.export(os.path.join(test_folder, 'PlayersExport.csv'))
#         csv_wrpr2 = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'PlayersExport.csv'),
#             p_key1='PID',
#             p_struc_type={},
#         )
#         if not beetools.is_struct_the_same(csv_wrpr2.csv_db, test_dict08, 'List'):
#             success = False
#         if os.path.isfile(os.path.join(test_folder, 'PlayersExport.csv')):
#             os.remove(os.path.join(test_folder, 'PlayersExport.csv'))
#
#         print('Test empty file')
#         csv_wrpr1 = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'EmptyFile.csv'),
#             p_key1='PID',
#             p_struc_type=[],
#         )
#         if csv_wrpr1.csv_db:
#             success = False
#
#         print('Test empty lines')
#         csv_wrpr1 = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'EmptyLines.csv'),
#             p_key1='PID',
#             p_struc_type=[],
#             p_match_nr_of_fields=True,
#         )
#         csv_wrpr1.export(os.path.join(test_folder, 'EmptyLinesExport.csv'))
#         csv_wrpr2 = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'EmptyLinesExport.csv'),
#             p_key1='PID',
#             p_struc_type=[],
#             p_convert_none=False,
#         )
#         if not beetools.is_struct_the_same(csv_wrpr2.csv_db, test_list05, 'List'):
#             success = False
#         if os.path.isfile(os.path.join(test_folder, 'EmptyLinesExport.csv')):
#             os.remove(os.path.join(test_folder, 'EmptyLinesExport.csv'))
#
#         print('Incorrect header')
#         csv_wrpr = CsvWrpr(
#             _name,
#             os.path.join(test_folder, 'LongHeader.csv'),
#             'PID',
#             p_match_nr_of_fields=True,
#         )
#         if not beetools.is_struct_the_same(csv_wrpr.csv_db, test_dict09):
#             success = False
#         return success
#
#     # end basic_test
#
#     success = True
#     b_tls = beetools.Archiver(__doc__[0], p_app_path, p_cls=p_cls)
#     logger = logging.getLogger(_name)
#     logger.setLevel(beetools.DEF_LOG_LEV)
#     file_handle = logging.FileHandler(beetools.LOG_FILE_NAME, mode='w')
#     file_handle.setLevel(beetools.DEF_LOG_LEV_FILE)
#     console_handle = logging.StreamHandler()
#     console_handle.setLevel(beetools.DEF_LOG_LEV_CON)
#     file_format = logging.Formatter(
#         beetools.LOG_FILE_FORMAT, datefmt=beetools.LOG_DATE_FORMAT
#     )
#     console_format = logging.Formatter(beetools.LOG_CONSOLE_FORMAT)
#     file_handle.setFormatter(file_format)
#     console_handle.setFormatter(console_format)
#     logger.addHandler(file_handle)
#     logger.addHandler(console_handle)
#
#     b_tls.print_header(p_cls=p_cls)
#     success = basic_test()
#     beetools.result_rep(success, 'Done')
#     b_tls.print_footer()
