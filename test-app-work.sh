# BUILD APP

sam build --template-file template.test.yaml

# START APP

sam local start-api -p 8080 --docker-network b8c6fc7a3da9 --log-file logs.txt --profile ai
