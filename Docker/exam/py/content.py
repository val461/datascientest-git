import os
import requests
import json

api_address = 'my_api_from_compose'
api_port = 8000
pages = ['v1/sentiment','v2/sentiment']
user, password = 'alice','wonderland'
tests = [("life is beautiful",1),("that sucks",-1)]

for sentence, expected_result in tests:
    for k, page in enumerate(pages):
        params={
            'username': user,
            'password': password,
            'sentence': sentence
        }
        # requête
        r = requests.get(
            url=f'http://{api_address}:{api_port}/{page}',
            params=params
        )
        result = json.loads(r.content)['score']

        # affichage des résultats
        if result * expected_result > 0:
            test_status = 'SUCCESS'
        else:
            test_status = 'FAILURE'

        result_description = {1:'positive',-1:'negative'}
        output = f'''
        ============================
            Content test
        ============================

        request done at "/{page}"
        {params}

        Expected result: {result_description[expected_result]};
        actual result: {result}

        ==>  {test_status}

        '''
        print(output)
        if os.environ.get('LOG') == 1:
            with open('log/api_test.log', 'a') as file:
                file.write(output)
