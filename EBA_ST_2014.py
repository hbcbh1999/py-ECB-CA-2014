﻿# -*- coding: utf-8 -*-
"""
Created on Sun Nov 02 19:33:28 2014

@author: Kelly
@ver 0.2
"""

#Metadata

Scenario =[
'No breakdown by scenario',
'Actual figures',
'Baseline scenario',
'Adverse scenario',
]

Status=[
'No breakdown by status',
'Non defaulted assets',
'Defaulted assets',
]

Maturity=[

'No breakdown by maturity',
'[ 0 - 3M ]',
'[ 3M - 1Y ]',
'[ 1Y - 2Y ]',
'[ 2Y - 3Y ]',
'[3Y - 5Y ]',
'[5Y - 10Y ]',
'[10Y - more ]',
'Total',
]


Country=[

'Austria',
'Belgium',
'Bulgaria',
'Cyprus',
'Czech Republic',
'Denmark',
'Estonia',
'Finland',
'France',
'Germany',
'Greece',
'Hungary',
'Iceland',
'Ireland',
'Italy',
'Latvia',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Malta',
'Netherlands',
'Norway',
'Poland',
'Portugal',
'Romania',
'Slovakia',
'Slovenia',
'Spain',
'Sweden',
'United Kingdom',
'Brazil',
'Chile',
'China',
'CROATIA',
'Hong Kong',
'India',
'Japan',
'Mexico',
'Peru',
'Russian Federation',
'Switzerland',
'Turkey',
'United States',
'International organisations',
'Afghanistan',
'Albania',
'Algeria',
'American Samoa',
'Andorra',
'Angola',
'Anguilla',
'Antigua and Barbuda',
'Argentina',
'Armenia',
'Aruba',
'Australia',
'Azerbaijan',
'Bahamas',
'Bahrain',
'Bangladesh',
'Barbados',
'Belarus',
'Belize',
'Benin',
'Bermuda',
'Bhutan',
'Bolivia - Plurinational state of',
'Bonaire - Sint Eustatius and Saba',
'Bosnia and Herzegowina',
'Botswana',
'British Indian Ocean Territory',
'Brunei Darussalam',
'Burkina Faso',
'Burundi',
'Cambodia',
'Cameroon',
'Canada',
'Cape Verde',
'Cayman Islands',
'Central African Republic',
'Chad',
'Channel Islands',
'Colombia',
'Comoros',
'CONGO - The Democratic Republic of the',
'CONGO',
'Cook Islands',
'Costa Rica',
'Cote d_Ivoire',
'Cuba',
'Curacao',
'Djibouti',
'Dominica',
'Dominican Republic',
'Ecuador',
'Egypt',
'El Salvador',
'Equatorial Guinea',
'Eritrea',
'Ethiopia',
'Faroe Islands',
'Falkland Islands (MALVINAS)',
'Fiji',
'French Guiana',
'French Polynesia',
'Macedonia - The former Yugoslav Republic of',
'Gabon',
'Gambia',
'Georgia',
'Ghana',
'Gibraltar',
'Greenland',
'Grenada',
'Guadeloupe',
'Guam',
'Guatemala',
'Guinea',
'Guinea-Bissau',
'Guyana',
'Haiti',
'Holy See (Vatican City State)',
'Honduras',
'Indonesia',
'Iran (Islamic Republic of)',
'Iraq',
'Isle of Man',
'Israel',
'Jamaica',
'Jordan',
'Kazakhstan',
'Kenya',
'Kiribati',
'Korea Dem_People_Rep_of',
'Korea Republic_of',
'Kosovo',
'Kuwait',
'Kyrgyzstan',
'Lao P.D.R.',
'Lebanon',
'Lesotho',
'Liberia',
'Libya',
'Macao',
'Madagascar',
'Malawi',
'Malaysia',
'Maldives',
'Mali',
'Marshall Islands',
'Martinique',
'Mauritania',
'Mauritius',
'Mayotte',
'Micronesia - Federated States of',
'Moldova',
'Monaco',
'Mongolia',
'Montenegro',
'Montserrat',
'Morocco',
'Mozambique',
'Myanmar',
'Namibia',
'Nauru',
'Nepal',
'New Caledonia',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'Niue',
'Northern Mariana Islands',
'Oman',
'Pakistan',
'Palau',
'Panama',
'Papua New Guinea',
'Paraguay',
'Philippines',
'Pitcairn',
'Puerto Rico',
'Qatar',
'Reunion',
'Rwanda',
'Saint Helena',
'Saint Kitts and Nevis',
'Saint Lucia',
'Saint Martin',
'Saint Vincent and the Grenadines',
'Saint-Pierre and Miquelon',
'Samoa',
'San Marino',
'Sao Tome and Principe',
'Saudi Arabia',
'Senegal',
'Serbia',
'Seychelles',
'Sierra Leone',
'Singapore',
'Sint Maarten',
'Solomon Islands',
'Somalia',
'South Africa',
'South Sudan',
'Sri Lanka',
'Sudan',
'Suriname',
'Svalbard and Jan Mayen Islands',
'Swaziland',
'Syria',
'Taiwan Province of China',
'Tajikistan',
'Tanzania',
'Thailand',
'Timor-Leste',
'Togo',
'Tokelau',
'Tonga',
'Trinidad and Tobago',
'Tunisia',
'Turkmenistan',
'Turks and Caicos Islands',
'Tuvalu',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United States Minor Outlying Islands',
'Uruguay',
'Uzbekistan',
'Vanuatu',
'Venezuela',
'Vietnam',
'Wallis and Futuna Islands',
'West Bank and Gaza',
'Western Sahara',
'Yemen',
'Zambia',
'Zimbabwe',
'Other',
'Other Central and eastern Europe countries non EEA',
'Middle East',
'Latin America and the Caribbean',
'Africa',
'Other advanced economies non EEA',
]

Exposure=[

'Total / No breakdown by portfolio',
'Central banks and central governments',
'Institutions',
'Corporates',
'Retail',
'Equity',
'Securitisation',
'Other non-credit obligation assets',
'Corporates - Of Which: Specialised Lending',
'Corporates - Of Which: SME',
'Retail - Secured on real estate property',
'Retail - Secured on real estate property - Of Which: SME',
'Retail - Secured on real estate property - Of Which: non-SME ',
'Retail - Qualifying Revolving',
'Retail - Other Retail',
'Retail - Other Retail - Of Which: SME',
'Retail - Other Retail - Of Which: non-SME',
'Securitisation and re-securitisations positions deducted from capital',
]


Portfolio=[

'Total / No breakdown by portfolio',
'SA',
'F-IRB',
'A-IRB',
]

#Country_code	Bank_name	LEI_code

Bank_name={
'529900ICA8XQYGIKR372' : 'BAWAG P.S.K. Bank für Arbeit und Wirtschaft und Österreichische Postsparkasse AG',
'529900GPOO9ISPD1EE83' : 'Raiffeisenlandesbank Niederösterreich-Wien AG',
'I6SS27Q1Q3385V753S50' : 'Raiffeisenlandesbank Oberösterreich AG',
'PQOH26KWDF7CG10L6792' : 'Erste Group Bank AG',
'EVOYOND2GGP3UHGGE885' : 'Raiffeisen Zentralbank Österreich AG',
'FJDBAXYL0TCMGLPQ4563' : 'Österreichische Volksbanken-AG with credit institutions affiliated according to Article 10 of the CR',
'D3K6HXMBBB6SK9OXH394' : 'Dexia NV*',
'A5GWLFH3KM7YV2SFQL84' : 'Belfius Banque SA',
'6B2PBRV1FCJDMR45RZ53' : 'KBC Group NV',
'LSGM84136ACA92XCN876' : 'AXA Bank Europe SA',
'A6NZLYKYN1UV7VVGFX65' : 'Investar (Holding of Argenta Bank- en Verzekeringsgroep)',
'CXUHEGU3MADZ2CEV7C11' : 'Hellenic Bank Public Company Ltd',
'5493007F6CE5P22TJ731' : 'Co-operative Central Bank Ltd',
'PQ0RAP85KK9Z75ONZW93' : 'Bank of Cyprus Public Company Ltd',
'EZKODONU5TYHW4PP1R34' : 'Aareal Bank AG',
'5299007S3UH5RKUYDA52' : 'Deutsche Apotheker- und Ärztebank eG',
'529900JZTYE3W7WQH904' : 'HASPA Finanzholding',
'PWEFG14QWWESISQ84C69' : 'IKB Deutsche Industriebank AG',
'529900Q1M1F4M8KMTM64' : 'KfW IPEX-Bank GmbH',
'0SK1ILSPWNVBNQWU0W18' : 'Landeskreditbank Baden-Württemberg-Förderbank',
'529900Z3J0N6S0F7CT25' : 'Landwirtschaftliche Rentenbank',
'529900GM944JT8YIRL63' : 'Münchener Hypothekenbank eG',
'52990002O5KK6XOGJ020' : 'NRW.Bank',
'529900USFSZYPS075O24' : 'Volkswagen Financial Services AG',
'529900S1KHKOEQL5CK20' : 'Wüstenrot Bausparkasse AG',
'QS0KV71ZZFYPT6POX557' : 'Wüstenrot Bank AG Pfandbriefbank',
'7LTWFZYICNSX8D621K86' : 'Deutsche Bank AG',
'851WYGNLUQLFZBSYGB56' : 'Commerzbank AG',
'B81CK4ESI35472RHJ606' : 'Landesbank Baden-Württemberg',
'529900HNOAA1KXQJUQ27' : 'DZ Bank AG Deutsche Zentral-Genossenschaftsbank',
'VDYMYTQGZZ6DU0912C88' : 'Bayerische Landesbank',
'DSNHHQ2B9X5N6OUJ1236' : 'Norddeutsche Landesbank-Girozentrale',
'52990082YOVOZIC8QX60' : 'Hypo Real Estate Holding AG',
'TUKDD90GPC79G1KOE162' : 'HSH Nordbank AG',
'DIZES5CFO5K3I5R58746' : 'Landesbank Hessen-Thüringen Girozentrale',
'GTQYZJON3I7SXRNJTT73' : 'Landesbank Berlin Holding AG',
'0W2PZJM8XOY22M4GG883' : 'DekaBank Deutsche Girozentrale',
'EFHQAFG69S4HKHLIZA14' : 'WGZ Bank AG Westdeutsche Genossenschafts-Zentralbank',
'MAES062Z21O4RZ2U7M96' : 'Danske Bank',
'3M5E1GQGKL17HI6CPN30' : 'Jyske Bank',
'GP5DT10VX1QRQUKVBK64' : 'Sydbank',
'52965FONQ5NZKP0WZL45' : 'Nykredit',
'549300GT0XFTFHGOIS94' : 'Banco Financiero y de Ahorros',
'635400CE9HHFB55PEY43' : 'Cajas Rurales Unidas',
'549300I84DXMIK4UUL30' : 'Catalunya Banc',
'549300OLBL49CW8CT155' : 'Caja de Ahorros y M.P. de Zaragoza',
'549300U4LIZV0REEQQ46' : 'Kutxabank',
'635400XT3V7WHLSFYY25' : 'Liberbank',
'54930056IRBXK0Q1FP96' : 'NCG Banco',
'5493007SJLLCTM6J6M37' : 'MPCA Ronda',
'5493006QMFDDMYWIAM13' : 'Banco Santander',
'K8MS7FD7N5Z2WQ51AZ71' : 'Banco Bilbao Vizcaya Argentaria',
'7CUNS533WID6K7DGFI87' : 'Caja de Ahorros y Pensiones de Barcelona',
'80H66LPTVDLM0P28XF25' : 'Banco Popular Español',
'SI5RG2M0WQQLZCXKRM20' : 'Banco de Sabadell',
'549300PY124PITBSWN73' : 'Banco Mare Nostrum',
'VWMYAEQSTOPNV0SUGU82' : 'Bankinter',
'7437003B5WFBOIEFY714' : 'OP-Pohjola Group',
'9695004ON2K947Z21B87' : 'Banque PSA Finance',
'969500STN7T9MRUMJ267' : 'BPI France (Banque Publique d’Investissement)',
'969500TVVZM86W7W5I94' : 'C.R.H. - Caisse de Refinancement de l’Habitat',
'969500R332FU13LE1433' : 'Groupe Crédit Mutuel',
'96950066U5XAAIRCPA78' : 'La Banque Postale',
'96950001WI712W7PQG45' : 'RCI Banque',
'549300HFEHJOXGE4ZE63' : 'Société de Financement Local',
'R0MUWSFPU8MPRO8K5P83' : 'BNP Paribas',
'969500TJ5KRTCJQWXH05' : 'Groupe Crédit Agricole',
'9695005MSX1OYEMGDF46' : 'Groupe BPCE',
'O2RNE8IBXP4R0TD8PU41' : 'Société Générale',
'JEUVK5RWVJEN8W0C9M24' : 'Eurobank Ergasias',
'5UMCZOEYKCVFAW8ZLO05' : 'National Bank of Greece',
'5299009N55YRQC69CN08' : 'Alpha Bank',
'M6AD1Y1KW32H8THQ6F76' : 'Piraeus Bank',
'529900W3MOO00A18X956' : 'OTP Bank Ltd',
'3U8WV1YX2VMUHH7Z1Q21' : 'Allied Irish Banks plc',
'Q2GQA2KF6XJ24W42G291' : 'The Governor and Company of the Bank of Ireland',
'635400DTNHVYGZODKQ93' : 'Permanent tsb plc.',
'F1T87K3OQ2OV1UORLH26' : 'Banca Carige S.P.A. - Cassa di Risparmio di Genova e Imperia',
'549300BDV4C410CYAQ76' : 'Banca Piccolo Credito Valtellinese',
'N747OI7JINV7RUUH6190' : "Banca Popolare Dell'Emilia Romagna - Società Cooperativa",
'8156009BC82130E7FC43' : 'Banca Popolare Di Milano - Società Cooperativa A Responsabilità Limitata',
'J48C8PCSJVUBR8KCW529' : 'Banca Popolare di Sondrio',
'V3AFM0G2D3A6E0QWDG59' : 'Banca Popolare di Vicenza - Società Cooperativa per Azioni',
'8156004B244AA70DE787' : 'Credito Emiliano S.p.A.',
'815600D79C96B9661149' : 'Iccrea Holding S.p.A',
'PSNL19R2RXX5U3QWHI44' : 'Mediobanca - Banca di Credito Finanziario S.p.A.',
'549300W9STRUCJ2DLU64' : 'Veneto Banca S.C.P.A.',
'2W8N8UU78PMDQKZENC08' : 'Intesa Sanpaolo S.p.A.',
'549300TRUWO2CD2G5692' : 'UniCredit S.p.A.',
'J4CP7MHCXR8DAQMKIL78' : 'Banca Monte dei Paschi di Siena S.p.A.',
'5493006P8PDBI8LC0O96' : 'Banco Popolare - Società Cooperativa',
'81560097964CBDAED282' : 'Unione Di Banche Italiane Società Cooperativa Per Azioni',
'R7CQUF1DQM73HUTV1078' : "Banque et Caisse d'Epargne de l'Etat",
'549300AUUQG072ATL746' : 'Precision Capital S.A. (Holding of Banque Internationale à Luxembourg and KBL European Private Banke',
'549300IHIJ7SCANBWN17' : 'ABLV Bank',
'529900RWC8ZYB066JF16' : 'Bank of Valletta plc',
'529900GGYMNGRQTDOO93' : 'Bank Nederlandse Gemeenten N.V.',
'JLP5FSPH9WPSHY3NIM24' : 'Nederlandse Waterschapsbank N.V.',
'3TK20IVIUJ8J3ZU0QE75' : 'ING Bank N.V.',
'DG3RU1DBUFHT4ZF9WN62' : 'Coöperatieve Centrale Raiffeisen-Boerenleenbank B.A.',
'BFXS5XCH7N0Y05NIXW11' : 'ABN AMRO Bank N.V.',
'724500A1FNICHSDF2I11' : 'SNS Bank N.V.',
'549300GKFG0RYRRQ1414' : 'DNB Bank Group',
'259400QHDOZWMJ103294' : 'ALIOR BANK SA',
'H8MIG1MMPR6JXUQVBM04' : 'BANK BPH SA',
'XLEZHWWOI4HFQDGL4793' : 'BANK HANDLOWY W WARSZAWIE SA',
'MKP1B7E76TN04CD85Z79' : 'BANK OCHRONY SRODOWISKA SA',
'2594000SEGUR418W2G08' : 'GETIN NOBLE BANK SA',
'P4GTT6GF1W40CVIMFR43' : 'POWSZECHNA KASA OSZCZEDNOSCI BANK POLSKI S.A. (PKO BANK POLSKI)',
'TO822O0VT80V06K0FH57' : 'Caixa Geral de Depósitos',
'JU1U6S0DG9YLT7N8ZV32' : 'Banco Comercial Português',
'3DM5DPGI3W6OU6GJ4N92' : 'Banco BPI',
'6SCPQ280AIY8EP3XFW53' : 'Nordea Bank AB (publ)',
'F3JS33DEI6XQ4ZBPTN86' : 'Skandinaviska Enskilda Banken AB (publ) (SEB)',
'NHBDILHZTYCNBV5UYZ31' : 'Svenska Handelsbanken AB (publ)',
'M312WZV08Y7LYUC71685' : 'Swedbank AB (publ)',
'549300BZ3GKOJ13V6F87' : 'SID - Slovenska izvozna in razvojna banka',
'5493001BABFV7P27OW30' : 'Nova Ljubljanska banka d. d.',
'549300J0GSZ83GTKBZ89' : 'Nova Kreditna Banka Maribor d.d.',
'2138005O9XJIJN4JPN90' : 'Royal Bank of Scotland Group plc',
'MLU0ZO3ML4LN2LL2TL39' : 'HSBC Holdings plc',
'G5GSEF7VJP5I7OUK5573' : 'Barclays plc',
'549300PPXHEU2JF0AM85' : 'Lloyds Banking Group plc',
'Bank_code' : 'Bank_name'
}


Country_code = {
'529900ICA8XQYGIKR372' : 'AT',
'529900GPOO9ISPD1EE83' : 'AT',
'I6SS27Q1Q3385V753S50' : 'AT',
'PQOH26KWDF7CG10L6792' : 'AT',
'EVOYOND2GGP3UHGGE885' : 'AT',
'FJDBAXYL0TCMGLPQ4563' : 'AT',
'D3K6HXMBBB6SK9OXH394' : 'BE',
'A5GWLFH3KM7YV2SFQL84' : 'BE',
'6B2PBRV1FCJDMR45RZ53' : 'BE',
'LSGM84136ACA92XCN876' : 'BE',
'A6NZLYKYN1UV7VVGFX65' : 'BE',
'CXUHEGU3MADZ2CEV7C11' : 'CY',
'5493007F6CE5P22TJ731' : 'CY',
'PQ0RAP85KK9Z75ONZW93' : 'CY',
'EZKODONU5TYHW4PP1R34' : 'DE',
'5299007S3UH5RKUYDA52' : 'DE',
'529900JZTYE3W7WQH904' : 'DE',
'PWEFG14QWWESISQ84C69' : 'DE',
'529900Q1M1F4M8KMTM64' : 'DE',
'0SK1ILSPWNVBNQWU0W18' : 'DE',
'529900Z3J0N6S0F7CT25' : 'DE',
'529900GM944JT8YIRL63' : 'DE',
'52990002O5KK6XOGJ020' : 'DE',
'529900USFSZYPS075O24' : 'DE',
'529900S1KHKOEQL5CK20' : 'DE',
'QS0KV71ZZFYPT6POX557' : 'DE',
'7LTWFZYICNSX8D621K86' : 'DE',
'851WYGNLUQLFZBSYGB56' : 'DE',
'B81CK4ESI35472RHJ606' : 'DE',
'529900HNOAA1KXQJUQ27' : 'DE',
'VDYMYTQGZZ6DU0912C88' : 'DE',
'DSNHHQ2B9X5N6OUJ1236' : 'DE',
'52990082YOVOZIC8QX60' : 'DE',
'TUKDD90GPC79G1KOE162' : 'DE',
'DIZES5CFO5K3I5R58746' : 'DE',
'GTQYZJON3I7SXRNJTT73' : 'DE',
'0W2PZJM8XOY22M4GG883' : 'DE',
'EFHQAFG69S4HKHLIZA14' : 'DE',
'MAES062Z21O4RZ2U7M96' : 'DK',
'3M5E1GQGKL17HI6CPN30' : 'DK',
'GP5DT10VX1QRQUKVBK64' : 'DK',
'52965FONQ5NZKP0WZL45' : 'DK',
'549300GT0XFTFHGOIS94' : 'ES',
'635400CE9HHFB55PEY43' : 'ES',
'549300I84DXMIK4UUL30' : 'ES',
'549300OLBL49CW8CT155' : 'ES',
'549300U4LIZV0REEQQ46' : 'ES',
'635400XT3V7WHLSFYY25' : 'ES',
'54930056IRBXK0Q1FP96' : 'ES',
'5493007SJLLCTM6J6M37' : 'ES',
'5493006QMFDDMYWIAM13' : 'ES',
'K8MS7FD7N5Z2WQ51AZ71' : 'ES',
'7CUNS533WID6K7DGFI87' : 'ES',
'80H66LPTVDLM0P28XF25' : 'ES',
'SI5RG2M0WQQLZCXKRM20' : 'ES',
'549300PY124PITBSWN73' : 'ES',
'VWMYAEQSTOPNV0SUGU82' : 'ES',
'7437003B5WFBOIEFY714' : 'FI',
'9695004ON2K947Z21B87' : 'FR',
'969500STN7T9MRUMJ267' : 'FR',
'969500TVVZM86W7W5I94' : 'FR',
'969500R332FU13LE1433' : 'FR',
'96950066U5XAAIRCPA78' : 'FR',
'96950001WI712W7PQG45' : 'FR',
'549300HFEHJOXGE4ZE63' : 'FR',
'R0MUWSFPU8MPRO8K5P83' : 'FR',
'969500TJ5KRTCJQWXH05' : 'FR',
'9695005MSX1OYEMGDF46' : 'FR',
'O2RNE8IBXP4R0TD8PU41' : 'FR',
'JEUVK5RWVJEN8W0C9M24' : 'GR',
'5UMCZOEYKCVFAW8ZLO05' : 'GR',
'5299009N55YRQC69CN08' : 'GR',
'M6AD1Y1KW32H8THQ6F76' : 'GR',
'529900W3MOO00A18X956' : 'HU',
'3U8WV1YX2VMUHH7Z1Q21' : 'IE',
'Q2GQA2KF6XJ24W42G291' : 'IE',
'635400DTNHVYGZODKQ93' : 'IE',
'F1T87K3OQ2OV1UORLH26' : 'IT',
'549300BDV4C410CYAQ76' : 'IT',
'N747OI7JINV7RUUH6190' : 'IT',
'8156009BC82130E7FC43' : 'IT',
'J48C8PCSJVUBR8KCW529' : 'IT',
'V3AFM0G2D3A6E0QWDG59' : 'IT',
'8156004B244AA70DE787' : 'IT',
'815600D79C96B9661149' : 'IT',
'PSNL19R2RXX5U3QWHI44' : 'IT',
'549300W9STRUCJ2DLU64' : 'IT',
'2W8N8UU78PMDQKZENC08' : 'IT',
'549300TRUWO2CD2G5692' : 'IT',
'J4CP7MHCXR8DAQMKIL78' : 'IT',
'5493006P8PDBI8LC0O96' : 'IT',
'81560097964CBDAED282' : 'IT',
'R7CQUF1DQM73HUTV1078' : 'LU',
'549300AUUQG072ATL746' : 'LU',
'549300IHIJ7SCANBWN17' : 'LV',
'529900RWC8ZYB066JF16' : 'MT',
'529900GGYMNGRQTDOO93' : 'NL',
'JLP5FSPH9WPSHY3NIM24' : 'NL',
'3TK20IVIUJ8J3ZU0QE75' : 'NL',
'DG3RU1DBUFHT4ZF9WN62' : 'NL',
'BFXS5XCH7N0Y05NIXW11' : 'NL',
'724500A1FNICHSDF2I11' : 'NL',
'549300GKFG0RYRRQ1414' : 'NO',
'259400QHDOZWMJ103294' : 'PL',
'H8MIG1MMPR6JXUQVBM04' : 'PL',
'XLEZHWWOI4HFQDGL4793' : 'PL',
'MKP1B7E76TN04CD85Z79' : 'PL',
'2594000SEGUR418W2G08' : 'PL',
'P4GTT6GF1W40CVIMFR43' : 'PL',
'TO822O0VT80V06K0FH57' : 'PT',
'JU1U6S0DG9YLT7N8ZV32' : 'PT',
'3DM5DPGI3W6OU6GJ4N92' : 'PT',
'6SCPQ280AIY8EP3XFW53' : 'SE',
'F3JS33DEI6XQ4ZBPTN86' : 'SE',
'NHBDILHZTYCNBV5UYZ31' : 'SE',
'M312WZV08Y7LYUC71685' : 'SE',
'549300BZ3GKOJ13V6F87' : 'SI',
'5493001BABFV7P27OW30' : 'SI',
'549300J0GSZ83GTKBZ89' : 'SI',
'2138005O9XJIJN4JPN90' : 'UK',
'MLU0ZO3ML4LN2LL2TL39' : 'UK',
'G5GSEF7VJP5I7OUK5573' : 'UK',
'549300PPXHEU2JF0AM85' : 'UK',
}


BankbyCountry ={
'AT' : '529900ICA8XQYGIKR372',
'AT' : '529900GPOO9ISPD1EE83',
'AT' : 'I6SS27Q1Q3385V753S50',
'AT' : 'PQOH26KWDF7CG10L6792',
'AT' : 'EVOYOND2GGP3UHGGE885',
'AT' : 'FJDBAXYL0TCMGLPQ4563',
'BE' : 'D3K6HXMBBB6SK9OXH394',
'BE' : 'A5GWLFH3KM7YV2SFQL84',
'BE' : '6B2PBRV1FCJDMR45RZ53',
'BE' : 'LSGM84136ACA92XCN876',
'BE' : 'A6NZLYKYN1UV7VVGFX65',
'CY' : 'CXUHEGU3MADZ2CEV7C11',
'CY' : '5493007F6CE5P22TJ731',
'CY' : 'PQ0RAP85KK9Z75ONZW93',
'DE' : 'EZKODONU5TYHW4PP1R34',
'DE' : '5299007S3UH5RKUYDA52',
'DE' : '529900JZTYE3W7WQH904',
'DE' : 'PWEFG14QWWESISQ84C69',
'DE' : '529900Q1M1F4M8KMTM64',
'DE' : '0SK1ILSPWNVBNQWU0W18',
'DE' : '529900Z3J0N6S0F7CT25',
'DE' : '529900GM944JT8YIRL63',
'DE' : '52990002O5KK6XOGJ020',
'DE' : '529900USFSZYPS075O24',
'DE' : '529900S1KHKOEQL5CK20',
'DE' : 'QS0KV71ZZFYPT6POX557',
'DE' : '7LTWFZYICNSX8D621K86',
'DE' : '851WYGNLUQLFZBSYGB56',
'DE' : 'B81CK4ESI35472RHJ606',
'DE' : '529900HNOAA1KXQJUQ27',
'DE' : 'VDYMYTQGZZ6DU0912C88',
'DE' : 'DSNHHQ2B9X5N6OUJ1236',
'DE' : '52990082YOVOZIC8QX60',
'DE' : 'TUKDD90GPC79G1KOE162',
'DE' : 'DIZES5CFO5K3I5R58746',
'DE' : 'GTQYZJON3I7SXRNJTT73',
'DE' : '0W2PZJM8XOY22M4GG883',
'DE' : 'EFHQAFG69S4HKHLIZA14',
'DK' : 'MAES062Z21O4RZ2U7M96',
'DK' : '3M5E1GQGKL17HI6CPN30',
'DK' : 'GP5DT10VX1QRQUKVBK64',
'DK' : '52965FONQ5NZKP0WZL45',
'ES' : '549300GT0XFTFHGOIS94',
'ES' : '635400CE9HHFB55PEY43',
'ES' : '549300I84DXMIK4UUL30',
'ES' : '549300OLBL49CW8CT155',
'ES' : '549300U4LIZV0REEQQ46',
'ES' : '635400XT3V7WHLSFYY25',
'ES' : '54930056IRBXK0Q1FP96',
'ES' : '5493007SJLLCTM6J6M37',
'ES' : '5493006QMFDDMYWIAM13',
'ES' : 'K8MS7FD7N5Z2WQ51AZ71',
'ES' : '7CUNS533WID6K7DGFI87',
'ES' : '80H66LPTVDLM0P28XF25',
'ES' : 'SI5RG2M0WQQLZCXKRM20',
'ES' : '549300PY124PITBSWN73',
'ES' : 'VWMYAEQSTOPNV0SUGU82',
'FI' : '7437003B5WFBOIEFY714',
'FR' : '9695004ON2K947Z21B87',
'FR' : '969500STN7T9MRUMJ267',
'FR' : '969500TVVZM86W7W5I94',
'FR' : '969500R332FU13LE1433',
'FR' : '96950066U5XAAIRCPA78',
'FR' : '96950001WI712W7PQG45',
'FR' : '549300HFEHJOXGE4ZE63',
'FR' : 'R0MUWSFPU8MPRO8K5P83',
'FR' : '969500TJ5KRTCJQWXH05',
'FR' : '9695005MSX1OYEMGDF46',
'FR' : 'O2RNE8IBXP4R0TD8PU41',
'GR' : 'JEUVK5RWVJEN8W0C9M24',
'GR' : '5UMCZOEYKCVFAW8ZLO05',
'GR' : '5299009N55YRQC69CN08',
'GR' : 'M6AD1Y1KW32H8THQ6F76',
'HU' : '529900W3MOO00A18X956',
'IE' : '3U8WV1YX2VMUHH7Z1Q21',
'IE' : 'Q2GQA2KF6XJ24W42G291',
'IE' : '635400DTNHVYGZODKQ93',
'IT' : 'F1T87K3OQ2OV1UORLH26',
'IT' : '549300BDV4C410CYAQ76',
'IT' : 'N747OI7JINV7RUUH6190',
'IT' : '8156009BC82130E7FC43',
'IT' : 'J48C8PCSJVUBR8KCW529',
'IT' : 'V3AFM0G2D3A6E0QWDG59',
'IT' : '8156004B244AA70DE787',
'IT' : '815600D79C96B9661149',
'IT' : 'PSNL19R2RXX5U3QWHI44',
'IT' : '549300W9STRUCJ2DLU64',
'IT' : '2W8N8UU78PMDQKZENC08',
'IT' : '549300TRUWO2CD2G5692',
'IT' : 'J4CP7MHCXR8DAQMKIL78',
'IT' : '5493006P8PDBI8LC0O96',
'IT' : '81560097964CBDAED282',
'LU' : 'R7CQUF1DQM73HUTV1078',
'LU' : '549300AUUQG072ATL746',
'LV' : '549300IHIJ7SCANBWN17',
'MT' : '529900RWC8ZYB066JF16',
'NL' : '529900GGYMNGRQTDOO93',
'NL' : 'JLP5FSPH9WPSHY3NIM24',
'NL' : '3TK20IVIUJ8J3ZU0QE75',
'NL' : 'DG3RU1DBUFHT4ZF9WN62',
'NL' : 'BFXS5XCH7N0Y05NIXW11',
'NL' : '724500A1FNICHSDF2I11',
'NO' : '549300GKFG0RYRRQ1414',
'PL' : '259400QHDOZWMJ103294',
'PL' : 'H8MIG1MMPR6JXUQVBM04',
'PL' : 'XLEZHWWOI4HFQDGL4793',
'PL' : 'MKP1B7E76TN04CD85Z79',
'PL' : '2594000SEGUR418W2G08',
'PL' : 'P4GTT6GF1W40CVIMFR43',
'PT' : 'TO822O0VT80V06K0FH57',
'PT' : 'JU1U6S0DG9YLT7N8ZV32',
'PT' : '3DM5DPGI3W6OU6GJ4N92',
'SE' : '6SCPQ280AIY8EP3XFW53',
'SE' : 'F3JS33DEI6XQ4ZBPTN86',
'SE' : 'NHBDILHZTYCNBV5UYZ31',
'SE' : 'M312WZV08Y7LYUC71685',
'SI' : '549300BZ3GKOJ13V6F87',
'SI' : '5493001BABFV7P27OW30',
'SI' : '549300J0GSZ83GTKBZ89',
'UK' : '2138005O9XJIJN4JPN90',
'UK' : 'MLU0ZO3ML4LN2LL2TL39',
'UK' : 'G5GSEF7VJP5I7OUK5573',
'UK' : '549300PPXHEU2JF0AM85',
}



SDDLabel ={
992801 : 'Operating profit before impairments',
992802 : 'Impairment losses on financial and non-financial assets in the banking book',
992803 : 'Common Equity Tier 1 capital (1)',
992804 : 'Total Risk Exposure (1)',
992805 : 'Common Equity Tier 1 ratio, % (1)',
992806 : '3 yr cumulative operating profit before impairments',
992807 : '3 yr cumulative impairment losses on financial and non-financial assets in the banking book',
992808 : '3 yr cumulative losses from the stress in the trading book',
992809 : 'Valuation losses due to sovereign shock after tax and prudential filters',
992810 : 'Common EU wide CET1 Threshold',
992811 : 'Total amount of instruments with mandatory conversion into ordinary shares upon a fixed date in the 2014 -2016 period (cumulative conversions)',
992812 : 'Total Additional Tier 1 and Tier 2 instruments eligible as regulatory capital under the CRR provisions that convert into Common Equity Tier 1 or are written down upon a trigger event',
992813 : 'Total Additional Tier 1 and Tier 2 instruments eligible as regulatory capital under the CRR provisions that convert into Common Equity Tier 1 or are written down upon a trigger event - Of which: eligible instruments whose trigger is above CET1 capital ratio in the adverse scenario',
992901 : 'LTV %',
992902 : 'Exposure values',
992903 : 'Risk exposure amounts',
992904 : 'Value adjustments and provisions',
992905 : 'Impairment rate',
992906 : 'Stock of Provisions',
992907 : 'Coverage Ratio - Default Stock',
993001 : 'Net interest income',
993002 : 'Net trading income',
993003 : 'Net trading income - of which trading losses from stress scenarios',
993004 : 'Other operating income',
993005 : 'Operating profit before impairments',
993006 : 'Impairment of financial assets',
993007 : 'Impairment of financial assets other than instruments designated at fair value through P&L',
993008 : 'Impairment Financial assets designated at fair value through P&L',
993009 : 'Impairment on non financial assets',
993010 : 'Operating profit after impairments from stress scenarios',
993011 : 'Other Income and expenses',
993012 : 'Pre-Tax profit',
993013 : 'Tax',
993014 : 'Net income',
993015 : 'Net income - Attributable to owners of the parent',
993016 : 'Net income_Attributable to owners of the parent - of which carried over to capital through retained earnings',
993017 : 'Net income_Attributable to owners of the parent - of which distributed as dividends',
993101 : 'Risk exposure amount for credit risk',
993102 : 'Risk exposure amount for credit risk - of which Securitisation and re-securitisations',
993103 : 'Risk exposure amount for credit risk - of which Other credit risk',
993104 : 'Risk exposure amount for market risk',
993105 : 'Risk exposure amount for operational risk',
993106 : 'Transitional floors for Risk exposure amount',
993107 : 'Total Risk exposure amount',
993108 : 'AQR Adjustments (for SSM countries only)',
993201 : 'Securitisation_Exposure values - Banking Book',
993202 : 'Securitisation_Exposure values - Trading Book (excl. correlation trading positions under CRM)',
993203 : 'Securitisation_Exposure values - Correlation Trading Portfolio (CRM)',
993204 : 'Securitisation_Exposure values - Total',
993205 : 'Securitisation_Risk exposure values - Banking Book',
993206 : 'Securitisation_Risk exposure values - Trading Book (excl. correlation trading positions under CRM)',
993207 : 'Securitisation_Risk exposure values - Total',
993208 : 'Securitisation_Impairments - Hold to Maturity porfolio',
993209 : 'Securitisation_Impairments - Available for Sale porfolio',
993210 : 'Securitisation_Impairments - Total',
993301 : 'GROSS DIRECT LONG EXPOSURES (accounting value gross of provisions)',
993302 : 'GROSS DIRECT LONG EXPOSURES - of which: loans and advances',
993303 : 'NET DIRECT POSITIONS (gross exposures (long) net of cash short positions of sovereign debt to other counterpaties only where there is a maturity matching)',
993304 : 'NET DIRECT POSITIONS - of which: AFS banking book',
993305 : 'NET DIRECT POSITIONS - of which: FVO (designated at fair value through profit&loss) banking book',
993306 : 'NET DIRECT POSITIONS - of which: Financial assets held for trading',
993307 : 'DIRECT SOVEREIGN EXPOSURES IN DERIVATIVES - Derivatives with positive fair value at 31/12/2013 - Notional value',
993308 : 'DIRECT SOVEREIGN EXPOSURES IN DERIVATIVES - Derivatives with positive fair value at 31/12/2013 - Fair-value at 31/12/2013 ',
993309 : 'DIRECT SOVEREIGN EXPOSURES IN DERIVATIVES - Derivatives with negative fair value at 31/12/2013 - Notional value',
993310 : 'DIRECT SOVEREIGN EXPOSURES IN DERIVATIVES - Derivatives with negative fair value at 31/12/2013 - Fair-value at 31/12/2013 ',
993311 : 'INDIRECT SOVEREIGN EXPOSURES - Derivatives with positive fair value at 31/12/2013 - Notional value',
993312 : 'INDIRECT SOVEREIGN EXPOSURES - Derivatives with positive fair value at 31/12/2013 - Fair-value at 31/12/2013 ',
993313 : 'INDIRECT SOVEREIGN EXPOSURES - Derivatives with negative fair value at 31/12/2013 - Notional value',
993314 : 'INDIRECT SOVEREIGN EXPOSURES - Derivatives with negative fair value at 31/12/2013 - Fair-value at 31/12/2013 ',
993401 : 'A - OWN FUNDS',
993402 : 'A.1 - COMMON EQUITY TIER 1 CAPITAL (net of deductions and after applying transitional adjustments)',
993403 : 'A.1.1 - Capital instruments eligible as CET1 Capital (including share premium and net own capital instruments)',
993404 : 'A.1.1.1 -   Of which: CET1 instruments subscribed by Government',
993405 : 'A.1.2 - Retained earnings',
993406 : 'A.1.3 - Accumulated other comprehensive income',
993407 : 'A.1.3.1 -   Of which: arising from unrealised gains/losses from Sovereign exposure in AFS portfolio',
993408 : 'A.1.3.2 -   Of which: arising from unrealised gains/losses from the rest of AFS portfolio',
993409 : 'A.1.4 - Other Reserves',
993410 : 'A.1.5 - Funds for general banking risk',
993411 : 'A.1.6 - Minority interest given recognition in CET1 capital',
993412 : 'A.1.7 - Adjustments to CET1 due to prudential filters excluding those from unrealised gains/losses from AFS portfolio',
993413 : 'A.1.8 - Adjustments to CET1 due to prudential filters from unrealised gains/losses from Sovereign Exposure in AFS portfolio',
993414 : 'A.1.9 - (-) Intangible assets (including Goodwill) ',
993415 : 'A.1.10 - (-) DTAs that rely on future profitability and do not arise from temporary differences net of associated DTLs ',
993416 : 'A.1.11 - (-) IRB shortfall of credit risk adjustments to expected losses',
993417 : 'A.1.12 - (-) Defined benefit pension fund assets',
993418 : 'A.1.13 - (-) Reciprocal cross holdings in CET1 Capital',
993419 : 'A.1.14 - (-) Excess deduction from AT1 items over AT1 Capital',
993420 : 'A.1.15 - (-) Deductions related to assets which can alternatively be subject to a 1.250% risk weight',
993421 : 'A.1.15.1 -   Of which: from securitisation positions (-)',
993422 : 'A.1.16 - (-) Holdings of CET1 capital instruments of financial sector entities where the institiution does not have a significant investment',
993423 : 'A.1.17 - (-) Deductible DTAs that rely on future profitability and arise from temporary differences',
993424 : 'A.1.18 - (-) Holdings of CET1 capital instruments of financial sector entities where the institiution has a significant investment',
993425 : 'A.1.19 - (-) Amount exceding the 17.65% threshold ',
993426 : 'A.1.20 - Transitional adjustments',
993427 : 'A.1.20.1 - Transitional adjustments due to grandfathered CET1 Capital instruments (+/-)',
993428 : 'A.1.20.2 - Transitional adjustments due to additional minority interests (+/-)',
993429 : 'A.1.20.3 - Other transitional adjustments to CET1 Capital excl. adjustments for Sovereign exposure in AFS (+/-)',
993430 : 'A.2 - ADDITIONAL TIER 1 CAPITAL (net of deductions and after transitional adjustments)',
993431 : 'A.2.1 - Of which: (+) Other existing support government measures',
993432 : 'A.3 - TIER 1 CAPITAL (net of deductions and after transitional adjustments)',
993433 : 'A.4 - TIER 2 CAPITAL (net of deductions and after transitional adjustments)',
993434 : 'B - TOTAL RISK EXPOSURE AMOUNT',
993435 : 'B.1 - of which: stemming from exposures that fall below the 10% / 15% limits for CET1 deduction (+)',
993436 : 'B.2 - of which: stemming from from CVA capital requirements (+)',
993437 : 'B.3 - of which: stemming from higher asset correlation parameter against exposures to large financial institutions under IRB the IRB approaches to credit risk (+)',
993438 : 'B.4 - of which: stemming from the application of the supporting factor to increase lending to SMEs (-)',
993439 : 'B.5 - of which: stemming from the effect of exposures that were previously part of Risk Exposure amount and receive a deduction treatment under CRR/CRDIV (-)',
993440 : 'B.6 - of which: others subject to the discretion of National Competent Authorities',
993441 : 'C.1 - Common Equity Tier 1 Capital ratio',
993442 : 'C.2 - Tier 1 Capital ratio',
993443 : 'C.3 - Total Capital ratio',
993444 : 'D - Common Equity Tier 1 Capital Threshold',
993445 : 'E - Total amount of instruments with mandatory conversion into ordinary shares upon a fixed date in the 2014 -2016 period (cumulative conversions)',
993446 : 'F - Total Additional Tier 1 and Tier 2 instruments eligible as regulatory capital under the CRR provisions that convert into Common Equity Tier 1 or are written down upon a trigger event',
993447 : 'F.1 - Of which: eligible instruments whose trigger is above CET1 capital ratio in the adverse scenario',
993448 : 'G - Fully Loaded Common Equity Tier 1 Capital ratio',
993501 : 'Restructuring scenarios - CET1 impact',
993502 : 'Restructuring scenarios - Risk exposure amount impact',
993601 : 'Restructuring scenarios - COMMON EQUITY TIER 1 CAPITAL (net of deductions and after applying transitional adjustments)',
993602 : 'Restructuring scenarios - TOTAL RISK EXPOSURE AMOUNT',
993603 : 'Restructuring scenarios - COMMON EQUITY TIER 1 RATIO',
993705 : 'Capital Measures_3Q2014 - Raising of capital instruments eligible as CET1 capital (+)',
993707 : 'Capital Measures_3Q2014 - Repayment of CET1 capital- buybacks (-)',
993701 : 'Capital Measures_3Q2014,Capital Measures_3Q2014 - Conversion to CET1 of hybrid instruments becoming effective between 1 January and 30 September 2014 (+)',
993703 : "Capital Measures_3Q2014,Capital Measures_3Q2014 - Net issuance of Additional Tier 1 and T2 Instruments with a trigger at or above bank's post stress test CET1 ratio in the adverse scenario during the stress test horizon (+/-)",
993702 : "Capital Measures_3Q2014,Capital Measures_3Q2014 - Net issuance of Additional Tier 1 and T2 Instrument with a trigger below bank's post stress test CET1 ratio in the adverse scenario during the stress test horizon (+/-)",
}

SDDTemplate = {
28 : 'Summary',
29 : 'CREDIT RISK',
30 : 'Evolution of P&L',
31 : 'RWA',
33 : 'Sovereign',
34 : 'Capital',
35 : 'Restruct Scenarios - Impact',
36 : 'Restruct Scenarios',
37 : 'Capital Measures_3Q2014',
}




SDDItemsBy = {
992801	: [	'Period',	'Scenario',							],
992802	: [	'Period',	'Scenario',							],
992803	: [	'Period',	'Scenario',							],
992804	: [	'Period',	'Scenario',							],
992805	: [	'Period',	'Scenario',							],
992806	: [	'Period',	'Scenario',							],
992807	: [	'Period',	'Scenario',							],
992808	: [	'Period',	'Scenario',							],
992809	: [	'Period',	'Scenario',							],
992810	: [	'Period',	'Scenario',							],
992811	: [	'Period',	'Scenario',							],
992812	: [	'Period',	'Scenario',							],
992813	: [	'Period',	'Scenario',							],
992901	: [	'Period',	'Scenario',	'Country',	'Country_rank',			'Exposure',		],
992902	: [	'Period',	'Scenario',	'Country',	'Country_rank',	'Status',	'Portfolio',	'Exposure',		],
992903	: [	'Period',	'Scenario',	'Country',	'Country_rank',	'Status',	'Portfolio',	'Exposure',		],
992904	: [	'Period',	'Scenario',	'Country',	'Country_rank',	'Status',	'Portfolio',	'Exposure',		],
992905	: [	'Period',	'Scenario',	'Country',	'Country_rank',			'Exposure',		],
992906	: [	'Period',	'Scenario',	'Country',	'Country_rank',			'Exposure',		],
992907	: [	'Period',	'Scenario',	'Country',	'Country_rank',			'Exposure',		],
993001	: [	'Period',	'Scenario',							],
993002	: [	'Period',	'Scenario',							],
993003	: [	'Period',	'Scenario',							],
993004	: [	'Period',	'Scenario',							],
993005	: [	'Period',	'Scenario',							],
993006	: [	'Period',	'Scenario',							],
993007	: [	'Period',	'Scenario',							],
993008	: [	'Period',	'Scenario',							],
993009	: [	'Period',	'Scenario',							],
993010	: [	'Period',	'Scenario',							],
993011	: [	'Period',	'Scenario',							],
993012	: [	'Period',	'Scenario',							],
993013	: [	'Period',	'Scenario',							],
993014	: [	'Period',	'Scenario',							],
993015	: [	'Period',	'Scenario',							],
993016	: [	'Period',	'Scenario',							],
993017	: [	'Period',	'Scenario',							],
993101	: [	'Period',	'Scenario',							],
993102	: [	'Period',	'Scenario',							],
993103	: [	'Period',	'Scenario',							],
993104	: [	'Period',	'Scenario',							],
993105	: [	'Period',	'Scenario',							],
993106	: [	'Period',	'Scenario',							],
993107	: [	'Period',	'Scenario',							],
993108	: [	'Period',	'Scenario',							],
993201	: [	'Period',	'Scenario',							],
993202	: [	'Period',	'Scenario',							],
993203	: [	'Period',	'Scenario',							],
993204	: [	'Period',	'Scenario',							],
993205	: [	'Period',	'Scenario',							],
993206	: [	'Period',	'Scenario',							],
993207	: [	'Period',	'Scenario',							],
993208	: [	'Period',	'Scenario',							],
993209	: [	'Period',	'Scenario',							],
993210	: [	'Period',	'Scenario',							],
993301	: [	'Period',		'Country',					'Maturity',	],
993302	: [	'Period',		'Country',					'Maturity',	],
993303	: [	'Period',		'Country',					'Maturity',	],
993304	: [	'Period',		'Country',					'Maturity',	],
993305	: [	'Period',		'Country',					'Maturity',	],
993306	: [	'Period',		'Country',					'Maturity',	],
993307	: [	'Period',		'Country',					'Maturity',	],
993308	: [	'Period',		'Country',					'Maturity',	],
993309	: [	'Period',		'Country',					'Maturity',	],
993310	: [	'Period',		'Country',					'Maturity',	],
993311	: [	'Period',		'Country',					'Maturity',	],
993312	: [	'Period',		'Country',					'Maturity',	],
993313	: [	'Period',		'Country',					'Maturity',	],
993314	: [	'Period',		'Country',					'Maturity',	],
993401	: [	'Period',	'Scenario',							],
993402	: [	'Period',	'Scenario',							],
993403	: [	'Period',	'Scenario',							],
993404	: [	'Period',	'Scenario',							],
993405	: [	'Period',	'Scenario',							],
993406	: [	'Period',	'Scenario',							],
993407	: [	'Period',	'Scenario',							],
993408	: [	'Period',	'Scenario',							],
993409	: [	'Period',	'Scenario',							],
993410	: [	'Period',	'Scenario',							],
993411	: [	'Period',	'Scenario',							],
993412	: [	'Period',	'Scenario',							],
993413	: [	'Period',	'Scenario',							],
993414	: [	'Period',	'Scenario',							],
993415	: [	'Period',	'Scenario',							],
993416	: [	'Period',	'Scenario',							],
993417	: [	'Period',	'Scenario',							],
993418	: [	'Period',	'Scenario',							],
993419	: [	'Period',	'Scenario',							],
993420	: [	'Period',	'Scenario',							],
993421	: [	'Period',	'Scenario',							],
993422	: [	'Period',	'Scenario',							],
993423	: [	'Period',	'Scenario',							],
993424	: [	'Period',	'Scenario',							],
993425	: [	'Period',	'Scenario',							],
993426	: [	'Period',	'Scenario',							],
993427	: [	'Period',	'Scenario',							],
993428	: [	'Period',	'Scenario',							],
993429	: [	'Period',	'Scenario',							],
993430	: [	'Period',	'Scenario',							],
993431	: [	'Period',	'Scenario',							],
993432	: [	'Period',	'Scenario',							],
993433	: [	'Period',	'Scenario',							],
993434	: [	'Period',	'Scenario',							],
993435	: [	'Period',	'Scenario',							],
993436	: [	'Period',	'Scenario',							],
993437	: [	'Period',	'Scenario',							],
993438	: [	'Period',	'Scenario',							],
993439	: [	'Period',	'Scenario',							],
993440	: [	'Period',	'Scenario',							],
993441	: [	'Period',	'Scenario',							],
993442	: [	'Period',	'Scenario',							],
993443	: [	'Period',	'Scenario',							],
993444	: [	'Period',	'Scenario',							],
993445	: [	'Period',	'Scenario',							],
993446	: [	'Period',	'Scenario',							],
993447	: [	'Period',	'Scenario',							],
993448	: [	'Period',	'Scenario',							],
993501	: [	'Period',	'Scenario',							],
993502	: [	'Period',	'Scenario',							],
993601	: [	'Period',	'Scenario',							],
993602	: [	'Period',	'Scenario',							],
993603	: [	'Period',	'Scenario',							],
993705	: [	'Period',								],
993707	: [	'Period',								],
993701	: [	'Period',								],
993703	: [	'Period',								],
993702	: [	'Period',								],
993706	: [	'Period',								],
993704	: [	'Period',								],
}







LEI2ECB = {
'F1T87K3OQ2OV1UORLH26':	'ITCARI'	,
'549300BDV4C410CYAQ76':	'ITCRVA'	,
'N747OI7JINV7RUUH6190':	'ITBPER'	,
'8156009BC82130E7FC43':	'ITBPM'	,
'J48C8PCSJVUBR8KCW529':	'ITBPS'	,
'V3AFM0G2D3A6E0QWDG59':	'ITBPV'	,
'8156004B244AA70DE787':	'ITCRED'	,
'815600D79C96B9661149':	'ITICCH'	,
'PSNL19R2RXX5U3QWHI44':	'ITMDB'	,
'549300W9STRUCJ2DLU64':	'ITVENE'	,
'2W8N8UU78PMDQKZENC08':	'ITISP'	,
'549300TRUWO2CD2G5692':	'ITUCG'	,
'J4CP7MHCXR8DAQMKIL78':	'ITMPS'	,
'5493006P8PDBI8LC0O96':	'ITBAPO'	,
'81560097964CBDAED282':	'ITUBI'	,
#grece
'JEUVK5RWVJEN8W0C9M24':	'GREURO'	,
'5UMCZOEYKCVFAW8ZLO05':	'GRNBG'	,
'5299009N55YRQC69CN08':	'GRALPH'	,
'M6AD1Y1KW32H8THQ6F76':	'GRPIRE'	,
}


