import os
import requests

api_address = '127.0.0.1'
api_port = 8000
pages = ['v1/sentiment','v2/sentiment']
tests = [('alice','wonderland',[200,200]),('bob','builder',[200,403])]

for user, password, expected_results in tests:
    for k, page in enumerate(pages):
        params={
            'username': user,
            'password': password,
            'sentence': 'not a negative sentence'
        }
        # requête
        r = requests.get(
            url=f'http://{api_address}:{api_port}/{page}',
            params=params
        )
        # statut de la requête
        status_code = r.status_code

        # affichage des résultats
        expected_result = expected_results[k]
        if status_code == expected_result:
            test_status = 'SUCCESS'
        else:
            test_status = 'FAILURE'

        output = f'''
        ============================
            Authentication test
        ============================

        request done at "/{page}"
        {params}

        Expected result = {expected_result};
        actual result = {status_code}

        ==>  {test_status}

        '''
        print(output)
        if os.environ.get('LOG') == 1:
            with open('api_test.log', 'a') as file:
                file.write(output)
