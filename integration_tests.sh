python3 -m pytest tests/integration --cov=modelcraft --cov-report=xml
bash <(curl -s https://codecov.io/bash) -c -F integration -t @.cc_token
