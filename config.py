# Copyright 2022 The Casdoor Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from casdoor import CasdoorSDK

certificate = '''-----BEGIN CERTIFICATE-----
MIIE3TCCAsWgAwIBAgIDAeJAMA0GCSqGSIb3DQEBCwUAMCgxDjAMBgNVBAoTBWFk
bWluMRYwFAYDVQQDEw1jZXJ0LWJ1aWx0LWluMB4XDTI0MDUwOTAyNTYzM1oXDTQ0
MDUwOTAyNTYzM1owKDEOMAwGA1UEChMFYWRtaW4xFjAUBgNVBAMTDWNlcnQtYnVp
bHQtaW4wggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQC8Hc9VzH3m/RKK
0CNzxEoqPOQiFDXpN6WjqKDlOwN+OAw3npNB/BXbAE3HqW1ydWp2WImDE4KFdIg8
5ybWXwFbLmTr3WUcxzXVfcuY5wsPhjIHRjk3uGmrNdbgxXX0mJLkXGdejlMFclGO
T5H+xa5Azo6wpYx6y7x+DeAd4pso9dFrbc730kvq9DCzPPaSAC0aH+pHScRGu9zT
QCeipNuv2WwMSVGqqnY1CDge0j7E9Ro3SnhCfS7MArmcjNUXf2J1ruKQMlFaNswD
d567n9Awn8ZI2A41eCwinLoN7MhrXZLym+Ra0gKgxMayqOntmk9rJkSfdYSkB05J
e1yJ05XGECSq5JYe/dHWBEoAZ1Yi3HY1+kFOBxhZYqV5oMVDxpdODusXq1WIFpv0
ajzeZiUcGMzjJhp4QJIUhbi2XHAwvUJ3wYpCS2kNiqEu/ptEQJVxuES7cDIMOcwK
yG6GUjYiyurKtlNbGlljdNs44JwRP/xzXWwqY/vyQxFleR94GdkHHP/mlKyN/7h/
tbXtAySEBrmvZfB9PqcqXqv888gjbz0osd962km8kJlLzAE3SkzyMuQkVaoWRo/W
wUU0PoRtCwxWMp40dt/KVyb2GBCSru0074fgW2tz74QJxfYsyjBrhkW8Lr3mRpUS
jWzKNwzNyKMHyxp59Pp2stjWCJh2lQIDAQABoxAwDjAMBgNVHRMBAf8EAjAAMA0G
CSqGSIb3DQEBCwUAA4ICAQBbflZtY0arRXtBv2w0rFys3ETpnj4V5EJMnw+LdDtq
JZXi0vQon21SjB/Cycn+JVzyZN9FefNIUbRqdDgsGhWtSHCMVWoUFoyA7An4Ar5o
sJWfEfcE60bIOQn8KjFCLQkOx3NnKEmNXAkVo1KperZ0PkXcehC0hgrVmapr7aCj
OMfh2N6wwuIP2YTHW7I595LL0omEpfJ44BYlSqTzU6YO9UlQysyzxfK9fIWmxnRk
H5VJ2OocTliAA3lNQPgqmRoPu8+ifHTpLg1WqG9DpCD18ZPrqnkP8KStQTE1j/uG
XLvU62UFNOjvFOH4Kdx2yp/gUmU6lpk0MGwX493j+MlRk8lvllh9GANlHy2T4KAw
8KMGeNfGUU7Evho1keLCXRJ4xPUBJRdAftyxWzBzDBzQ83ED+Ga8Kk93pwh8O8ED
0yBH+i0Jh+gDyxs6pZiERIVqD/Gg05VwIpZr6x13NHllhGojZBAtQJX3OyP2YSig
XmFrLY/iUOWmDGT7Jb5RUosA2BD9XSCcULnrqPX/wGN7M8S72G6tJUdlhatnzTQ7
Mp1fETxtuPFzUifyKBqqEgBGsjmBtjM/uG7y9HOtm7DMJKASOQ2x6n8TOh3RccB8
MEuBoMxauXQxP+ZkO7p1ESIg8eq9fFZ6R/Ap8I/5sIj3lGQEjdgQJlcYz5E0YQSP
6g==
-----END CERTIFICATE-----'''

class Config:
    CASDOOR_SDK = CasdoorSDK(
        endpoint='http://10.3.11.208:8000',
        client_id='2d3877df0bdf2c421201',
        client_secret='616fdc5ec8b3ae3b55e21580406ab3c32acfe41b',
        certificate=certificate,
        org_name='fastapi_example',
        application_name='fastapi-example',
    )
    REDIRECT_URI = 'http://10.3.11.208:5000/api/signin'
    SECRET_TYPE = 'filesystem'
    SECRET_KEY = os.urandom(24)
