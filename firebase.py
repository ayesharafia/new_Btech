

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# datab = firestore.client()


# cred = credentials.Certificate({
#   "type": "service_account",
#   "project_id": "djangoproject-6ecde",
#   "private_key_id": "11abbc0dc536f3015cbb63d0c1dbfe5b5ef9f354",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDAsRp4RD8TLwSl\nlZpBEaj0aQmIUlJJko8Ls6B/3UZaefQsjT3ZebZEcRA0W+ieKXTcO3M4X9rgyjz2\nnjJSigsaZfQuAehCpOhIXZBI6JnfI+cPGvdLTtoPc014Hco7IgNoCg8lZOqcxgnj\n/Wv9ceKkXibHyN+2HDlwx20fhrWKV0xqdBD6ttVwVio3ENLFTfDwzVAH5oBCZcwF\n9Strnp61oPx2weTY++FovRwKPaqfLGYvzvDYr7EY9mAcRR9WmycpRsya38Xmrn+q\nlHYRI+n39ueRh4HDqHArPF+/xS/xk5UjZIHWhLXbiuRSilAqhpIArXtaTIpRLosO\nsLlk6DlhAgMBAAECggEAPu746rO7eAwAtAYG8d6PNHhD1UKxvnbAAn3h2zENY8p1\n7cEZpLhER9k3hipIcLOwh6dhC9X+ujFDNPbZD60nUDFhTU9xKKcMeGoakD1r1/21\nXvEbOHzh6m7pq+Pq42JKA4ZZiQiLObXSkCR6SzYRZEad2t1n92YDeqqfoM7R5wLn\np2scmGODTcbIl6qQEkXrYD4GpaB0vySW5EfitoLK6WpSMhbmMlXM36z0IChk2//H\nj1ASvH3ruVNH3WK/9tyfgyqZwxsYkylD53by5ZkelUWXsY3wjsZb8jeOh6aoi303\nGYBpy71ropY7fIR5wLXmtlf43zTsLYSkus7Tx5Xw+wKBgQDvLsd395tyyuZOgRt3\nGoIIEr9BNuyA1gBJjlTl7oT1Zr08DpkLEhj/XUfb4PgxESeH2L6QTSofhjC/t9RM\nva5zELVjofNQzgSlyCyxG8yEAeEdIkHE9J1EQhuwrJPd5thHxgDO4sFvTZgQUuHJ\nYYS2FQz2414E3799p+2mkXafCwKBgQDOPYA8zkQVUJKwCHglGeZmRGL/9cVEZWnt\nsO+AT0fxIEdCIJC1c4Y+V1XABnw1xCSOXJ4rZkavkoJAxPON6L7L0Lv6FnkIxs96\nEDPMZBkEqUHewMv+i351UiMoG9TibbFBMVuxtN42FFDemSqqyGnUQ1WPl2A+yh02\nXw8b3OO8wwKBgGLBCsSirEEaOzsAnYlwnW2d5++SMNYFBbtZE/6Xm7gDAnDwigoD\nH+UX65qCaZdAwPSa7huAcLrxWeFekj5ZNtT1eh8399FOLqcQXjuGAcwjRoIT6dnb\nMa/EJ9CrgKXnMTd5Lk49W6aMABQFVIokRHo1eNPbDq+ufk7wbfQPLU3/AoGAbT7g\nndT49X1vpjVmRujYRZW2BzWNn/RETzbpNsNILW7WsC2F2cfu9TjX4FbPFr/mSU7A\nLecITFpECsEI7kO6RUY1PH0I8eA16MeKWJsxMWnizXa82AHWI5k1rDpJ4wMN4KWf\nl5tiFa1fRPpHQp3UiS59tQkPX1M6dCGYZD72l3cCgYB7CCMeNYTD+aZ+/azql76x\n5zuJzOIlo23v0t6qJROd8WUIykQ20KLX+OeRP3b+ulhblt0gOoOSG1/fsSPJi4yO\nIOwdUQcMrzkLQoLvS0d2nUKS7HadPZYuZZNGqAsTrB1rWaGTN9AYKbllRwlpLBVZ\nVy+knPDZzJWakc6dzGMTbw==\n-----END PRIVATE KEY-----\n",
#   "client_email": "firebase-adminsdk-axde3@djangoproject-6ecde.iam.gserviceaccount.com",
#   "client_id": "113152190958391580936",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-axde3%40djangoproject-6ecde.iam.gserviceaccount.com"
# }
# )

# firebase_admin.initialize_app(cred)

# doc_ref = datab.collection(u'usersInfo').document(u'ID1')
# doc_ref.set({
#     u'first': u'Ayesha',
#     u'last': u'Rafia',
# })
# doc_ref = datab.collection(u'usersInfo').document(u'ID2')
# doc_ref.set({
#         u'firstname': u'Stella',
#         u'lastname': u'John'
# })

